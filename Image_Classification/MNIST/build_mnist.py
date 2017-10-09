import optparse
import os
import numpy as np
from natsort import humansorted
from PIL import Image
from mnist import MNIST


def convert_images(raw):
    """
    Convert images from the MNIST format and return a 4-dim array with
    shape: [number_of_images_per_batch, height, width, channel]
    The pixel values are integers between 0 and 255.
    There are 10000, 28x28 1 channel images per batch, in row major order.
    """
    return np.reshape(np.array(raw), (-1, 28, 28, 1))


mndata = MNIST('/path/to/data/files')
train_img, train_labels = mndata.load_training()
images = convert_images(train_img)
test_img, test_labels = mndata.load_testing()

with open('label_names.txt', 'w') as of:
    of.write('Class,Label\n')
    for index, label in enumerate(train_labels):
        of.write(str(index) + ',' + str(label) + '\n')

count = 1
with open('data.csv', 'w') as of:
    of.write('Integer,Label\n')
    for ind, image in enumerate(train_img):
        file_path = os.path.join(
            'path', str(count) + '.jpg')
        Image.frombytes('L', (28, 28), images).save(file_path)
        of.write(file_path + ',' + str(train_labels[ind]) + '\n')
        count += 1
