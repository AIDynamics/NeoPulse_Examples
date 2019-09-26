import gzip
import shutil
from pathlib import Path

import numpy as np
import requests
from imageio import imwrite
from mnist import MNIST


def download_data():
    '''
    Check if raw MNIST data is present. If not, download MNIST data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'http://yann.lecun.com/exdb/mnist/'
    file_list = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz']
    for f in file_list:
        if not Path('raw_data/' + f.replace('.gz', '')).is_file():
            r = requests.get(URL + f, stream=True)
            with open('raw_data/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)
            with gzip.open('raw_data/' + f, 'rb') as f_z:
                with open('raw_data/' + f.replace('.gz', ''), 'wb') as f_u:
                    shutil.copyfileobj(f_z, f_u)


def convert_images(raw):
    '''
    Convert images from the MNIST format and return a 4-dim array with
    shape: [number_of_images_per_batch, height, width, channel]
    The pixel values are integers between 0 and 255.
    There are 10000, 28x28 1 channel images per batch, in row major order.
    '''

    return np.reshape(np.array(raw), (-1, 28, 28, 1)).astype('uint8')


def write_csv_file():
    '''
    Save images as PNG files (lossless).
    Write absolute path to image files and class label to training_data.csv
    training_data.csv should be of length 70001, with the first line containing the header.
    The test images are written at the end, i.e. the last 10000 lines correspond to the test set.
    '''

    mndata = MNIST('raw_data')
    train_img, train_labels = mndata.load_training()
    train_images = convert_images(train_img)
    test_img, test_labels = mndata.load_testing()
    test_images = convert_images(test_img)

    Path('images').mkdir(parents=True, exist_ok=True)

    # writing training csv
    with open('training_data.csv', 'w') as of:
        of.write('Image\n')

        for index, image in enumerate(train_images):
            img_file = 'images/mnist_train_' + str(index) + '.png'
            imwrite(img_file, image)
            of.write(str(Path(img_file)) + '\n')

    
    # writing querying csv
    with open('query.csv', 'w') as of:
        of.write('Image\n')

        for index, image in enumerate(test_images):
            img_file = 'images/mnist_test_' + str(index) + '.png'
            imwrite(img_file, image)
            of.write(str(Path(img_file)) + '\n')
    

if __name__ == '__main__':

    # Download data if necessary
    download_data()

    # Write the data to PNG files, and create a csv file for NeoPulse AI Studio
    write_csv_file()
