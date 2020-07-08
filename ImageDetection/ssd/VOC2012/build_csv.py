import gzip
import shutil
from pathlib import Path
import tarfile
import os

import numpy as np
import requests
from imageio import imwrite
from xml.etree import ElementTree
import json


def download_data():
    '''
    Check if raw VOC2012 data and VGG pre_trained model are present. If not, download VOC2012 data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL_voc = 'http://host.robots.ox.ac.uk/pascal/VOC/voc2012/'
    f = 'VOCtrainval_11-May-2012.tar'
    if not Path('raw_data/' + f).is_file():
        r = requests.get(URL_voc + f, stream=True)
        with open('raw_data/' + f, 'wb') as f_z:
            shutil.copyfileobj(r.raw, f_z)
        tarfile.open('raw_data/' + f).extractall()

    Path('pre_trained_model').mkdir(parents=True, exist_ok=True)
    URL_vgg = 'https://drive.google.com/uc?authuser=0&id=1sBmajn6vOE7qJ8GnxUJt4fGPuffVUZox&export=download'
    f_vgg = 'vgg_16.h5'
    if not Path('pre_trained_model/' + f).is_file():
        r_vgg = requests.get(URL_vgg + f_vgg, stream=True)
        with open('pre_trained_model/' + f_vgg, 'wb') as f_k:
            shutil.copyfileobj(r_vgg.raw, f_k)

def write_csv_file():
    '''
    Write absolute path to image files and bounding box labels to training_data.csv.
    '''

    xml_path = Path("VOCdevkit/VOC2012/Annotations/")
    image_folder = Path("VOCdevkit/VOC2012/JPEGImages/")

    label2id = {"aeroplane" : 0,
                "bicycle" : 1,
                "bird" : 2,
                "boat" : 3,
                "bottle" : 4,
                "bus" : 5,
                "car" : 6,
                "cat" : 7,
                "chair" : 8,
                "cow" : 9,
                "diningtable" :10,
                "dog" : 11,
                "horse" : 12,
                "motorbike" : 13,
                "person" : 14,
                "pottedplant" : 15,
                "sheep" : 16,
                "sofa" : 17,
                "train" : 18,
                "tvmonitor" : 19}

    with open('training_data.csv', 'w') as of:
        of.write('image,label\n')
        filenames = os.listdir(str(xml_path))
        for index, filename in enumerate(filenames):
            tree = ElementTree.parse(str(xml_path / filename))
            root = tree.getroot()
            bounding_boxes = []
            size_tree = root.find('size')
            width = float(size_tree.find('width').text)
            height = float(size_tree.find('height').text)
            for object_tree in root.findall('object'):
                for bounding_box in object_tree.iter('bndbox'):
                    xmin = float(bounding_box.find('xmin').text)/width
                    ymin = float(bounding_box.find('ymin').text)/height
                    xmax = float(bounding_box.find('xmax').text)/width
                    ymax = float(bounding_box.find('ymax').text)/height

                class_name = object_tree.find('name').text
                class_id = label2id[class_name]
                bounding_box = [xmin, ymin, xmax, ymax, class_id]
                bounding_boxes.append(bounding_box)
            image_name = root.find('filename').text
            image_path = str((image_folder / image_name))
            jstring = json.dumps(bounding_boxes)
            of.write(image_path + ",\"" + jstring + "\"\n")
    
    with open('query.csv', 'w') as of:
        of.write('image\n')
        filenames = os.listdir(str(xml_path))

        # Gets the first 20 rows
        num = 20
        
        for index, filename in enumerate(filenames):
            if index >= num:
                break
            tree = ElementTree.parse(str(xml_path / filename))
            root = tree.getroot()
            image_name = root.find('filename').text
            image_path = str((image_folder / image_name))
            of.write(image_path + "\n")


if __name__ == '__main__':

    # Download data if necessary
    download_data()

    # create a csv file for NeoPulse AI Studio
    write_csv_file()
