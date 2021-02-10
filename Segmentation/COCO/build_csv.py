import os
import json
import requests
import shutil
from pathlib import Path
import gzip
from zipfile import ZipFile

###################################################
##                                               ##
##        Parts need to customize from here      ##
##                                               ##
###################################################

WholeCOCO = False
num_training_samples = 200
num_query_samples = 10

# csv path
train_csv_path = 'training_data.csv'
valid_csv_path = 'valid.csv'
query_csv_path = 'query.csv'


###################################################
##                                               ##
##        Parts need to customize ends here      ##
##                                               ##
###################################################

# annotations files path

train_anno_path = "annotations/instances_train2017.json"
valid_anno_path = "annotations/instances_val2017.json"

# folder path save images
train_image_folder = "COCO2017_train"
valid_image_folder = "COCO2017_valid"

# folder path save images
train_image_folder = "COCO2017_train"
valid_image_folder = "COCO2017_valid"

def download_annotation():

    URL = 'http://images.cocodataset.org/annotations/'
    file_list = ['annotations_trainval2017.zip']
    Path('annotations').mkdir(parents=True, exist_ok=True)
    for f in file_list:
        if not Path('annotations/' + f).is_file():
            r = requests.get(URL + f, stream=True)
            with open('annotations/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)           
            
            with ZipFile('annotations/' + f, 'r') as zf:
                zf.extractall("./")


def download_img_from_annotation_dict(d, img_folder_path):
    """
    TODO: download COCO train/valid dataset and save images in "img_folder_path"
    Inputs:
        - d: dict, dictionary read from COCO train/valid json file
        - img_folder_path: str, image folder COCO dataset will be saved.
    Outputs:
        - img_size: dict, dictionary mapping from image_id to image size in the format of [width,height]
    """

    Path(img_folder_path).mkdir(parents=True, exist_ok=True)

    if WholeCOCO:
        img_list = d['images']
    else:
        img_list = d['images'][:num_training_samples]
    img_size = dict()

    for img_item in img_list: 
        r = requests.get(img_item['coco_url'], stream=True)
        # save image to the folder
        with open(img_folder_path + '/{}.jpg'.format(img_item['id']),'wb') as wf:
            shutil.copyfileobj(r.raw, wf)

        img_size[img_item['id']] = [int(img_item['width']), int(img_item['height'])]

    return img_size

def get_instance_csv_from_annotation_dict(d, img_size, csv_path, img_folder_path):
    """
    TODO: get label of segmentation, bounding box and class_id, write the label
          in a csv file under "csv_path".
    Inputs:
        - d: dict, dictionary read from COCO train/valid json file.
        - img_size: dict, dictionary mapping from image_id to image size in the format of [width,height]
        - csv_path: str, the path of csv file saved labels
        - img_folder_path: str, image folder COCO dataset saved.  

    """

    img2label = dict()

    anno_list = d['annotations']

    # build img2label dict
    for anno_item in anno_list:
        img_id = anno_item['image_id']

        if not img_id in img_size.keys():
            continue

        if not (img_id in img2label):
            img2label[img_id] = []
        
        img2label[img_id].append(formating_annotation_item(anno_item, img_size[img_id]))

    with open(csv_path,'w') as wf:
        wf.write('Image,Label\n')

        for kk in img2label.items():
            label_str = json.dumps(kk[1])
            wf.write('{0}/{1}.jpg,\"{2}\"\n'.format(img_folder_path,kk[0],label_str.replace("\"","\'")))

    return

def formating_annotation_item(anno_item, img_size_list):
    """
    TODO: get formated labels for training from COCO raw labels.
    Inputs:
        - anno_item: dict, COCO raw label for one instance.
        - img_size: dict, dictionary mapping from image_id to image size in the format of [width,height]
    Outputs:
        - new_dict: dict, formated label for one instance.

    """

    new_dict = {}

    # formating segmentation annotation
    if anno_item["iscrowd"] == 0:
        segm_sets = anno_item["segmentation"]

        new_segm_sets = []

        for segm in segm_sets:
            for segm_i in range(len(segm)):
                segm[segm_i] = int(segm[segm_i])/int(img_size_list[segm_i%2])

            new_segm_sets.append(segm)

        new_dict["segmentation"] = new_segm_sets
    else:
        new_dict["segmentation"] = anno_item["segmentation"]

    # formating bbox annotation

    l,t,w,h = anno_item["bbox"]
    l = int(l)
    t = int(t)
    w = int(w)
    h = int(h)

    l_norm = l / img_size_list[0]
    t_norm = t / img_size_list[1]
    r_norm = (l + w) / img_size_list[0]
    b_norm = (t + h) / img_size_list[1]

    new_dict["bbox"] = [l_norm, t_norm, r_norm, b_norm]

    # formating class id

    new_dict["class_id"] = anno_item["category_id"]

    return new_dict

def build_query_csv(from_csv='training_data.csv', output_csv='query.csv', query_num_samples=10):
    lines = []
    with open(from_csv, 'r') as rf:
        lines=rf.readlines()
    with open(output_csv, 'w') as wf:
        for lid in range(min(len(lines), query_num_samples+1)):
            wf.write('{}\n'.format(lines[lid].split(',')[0]))




if __name__ == "__main__":
    # loading annotation json files
    if not Path(train_anno_path).is_file():
        download_annotation()
    with open(train_anno_path,'r') as rf1:
        s_train = rf1.read()

    if WholeCOCO:
        with open(valid_anno_path,'r') as rf2:
            s_valid = rf2.read()

    dict_train = json.loads(s_train)
    if WholeCOCO:
        dict_valid = json.loads(s_valid)

    # build training csv

    dict_img_size = download_img_from_annotation_dict(dict_train, train_image_folder)
    get_instance_csv_from_annotation_dict(dict_train, dict_img_size, train_csv_path, train_image_folder)

    # build validation csv

    if WholeCOCO:
        dict_img_size = download_img_from_annotation_dict(dict_valid, valid_image_folder)
        get_instance_csv_from_annotation_dict(dict_valid, dict_img_size, valid_csv_path, valid_image_folder)

    # build query csv

    build_query_csv(from_csv=train_csv_path, output_csv=query_csv_path, query_num_samples=num_query_samples)

