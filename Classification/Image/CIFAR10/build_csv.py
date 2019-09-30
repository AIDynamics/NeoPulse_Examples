import pickle
import shutil
import tarfile
from pathlib import Path
from random import shuffle

import numpy as np
import requests
from imageio import imwrite
from natsort import humansorted


def download_data():
    '''
    Check if raw CIFAR-10 data is present. If not, download data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'https://www.cs.toronto.edu/~kriz/'
    file_list = ['cifar-10-python.tar.gz']
    for f in file_list:
        if not Path('raw_data/' + f).is_file():
            r = requests.get(URL + f, stream=True)
            with open('raw_data/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)

        tarfile.open('raw_data/' + f).extractall('raw_data/')


def listdir_files(d):
    return [str(p) for p in Path(d).iterdir() if p.is_file()]


def unpickle(file_name):
    '''
    Unpickle the given file and return the data.
    '''
    with open(file_name, mode='rb') as f:
        data = pickle.load(f, encoding='bytes')
    return data


def convert_images(raw):
    '''
    Convert images from the CIFAR-10 format and return a 4-dim array with
    shape: [number_of_images_per_batch, height, width, channel]
    The pixel values are integers between 0 and 255.
    There are 10000, 32x32 3 channel images per batch, in row major order.
    '''
    return np.reshape(np.array(raw), (10000, 32, 32, 3), order='F')


def load_data(filename):
    '''
    Load a pickled data-file from the CIFAR-10 data-set
    and return the converted images and class-number
    for each image.
    '''
    # Load the pickled data-file.
    data = unpickle(filename)
    # Get the raw images.
    raw_images = data[b'data']
    # Convert the images.
    images = convert_images(raw_images)
    # Get the class-numbers for each image. Convert to numpy-array.
    labels = np.array(data[b'labels'])
    return images, labels


def write_data(validation_split):
    '''
    Unpickle the raw data.
    Write class index and label names.
    Write the images to png files.
    Write the csv file for NeoPulse AI Studio.
    '''
    data_path = 'raw_data/cifar-10-batches-py/'
    image_path = 'images/'

    Path(image_path).mkdir(parents=True, exist_ok=True)

    file_names = humansorted(listdir_files(data_path))
    data_files = file_names[1:6] + file_names[-1:]
    data = file_names[1:] + file_names[:1]

    names = unpickle(file_names[0])

    with open('label_names.txt', 'w') as of:
        of.write('Class,Label\n')
        for index, label in enumerate(names[b'label_names']):
            of.write(str(index) + ',' + str(label) + '\n')

    csv_lines = []
    count = 0

    for file_name in data_files:
        image_list, labels = load_data(file_name)
        for ind, image in enumerate(image_list):
            file_path = image_path + str(count) + '.png'
            imwrite(file_path, image)
            csv_lines.append(str(Path(file_path)) + ',' + str(labels[ind]) + '\n')
            count += 1

    shuffle(csv_lines)

    split_index = int(validation_split * len(csv_lines))

    train = csv_lines[:-split_index]
    valid = csv_lines[-split_index:]

    # write training csv
    with open('training_data.csv', 'w') as of:
        of.write('Image,Class\n')
        for l in train:
            of.write(l)



    # write querying csv
    with open('query.csv', 'w') as of:
        of.write('Image\n')

        for l in valid:
            of.write(l.split(',')[0] + '\n')


if __name__ == '__main__':

    # Download data if necessary
    download_data()
    # Write the data to PNG files, and create a csv file for NeoPulse AI Studio
    write_data(0.2)
