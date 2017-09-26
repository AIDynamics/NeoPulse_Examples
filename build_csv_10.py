import optparse
import os
import pickle
import numpy as np
from natsort import humansorted
from PIL import Image


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


def unpickle(file_name):
    """
    Unpickle the given file and return the data.
    """
    with open(file_name, mode='rb') as f:
        data = pickle.load(f, encoding='bytes')
    return data


def convert_images(raw):
    """
    Convert images from the CIFAR-10 format and return a 4-dim array with
    shape: [number_of_images_per_batch, height, width, channel]
    The pixel values are integers between 0 and 255.
    There are 10000, 32x32 3 channel images per batch, in row major order.
    """
    return np.reshape(np.array(raw), (10000, 32, 32, 3), order='F')


def load_data(filename):
    """
    Load a pickled data-file from the CIFAR-10 data-set
    and return the converted images and class-number
    for each image.
    """
    # Load the pickled data-file.
    data = unpickle(filename)
    # Get the raw images.
    raw_images = data[b'data']
    # Convert the images.
    images = convert_images(raw_images)
    # Get the class-numbers for each image. Convert to numpy-array.
    # changed 'labels' to 'fine_labels'
    labels = np.array(data[b'labels'])
    return images, labels


if __name__ == '__main__':

    usage = '''
    python %prog batch_directory image_directory

    This program decodes the python version of the cifar-10 dataset
    (located in batch_directory) into .jpg files
    (located in image_directory) and produces two csv files:
        data.csv
        label_names.csv
    where data.csv contains the full path to the image with its class number,
    and label_names.csv contains each label name and corresponding class number.
    The first 50000 rows are the training set and the last 10000 are the
    test set.'''

    parser = optparse.OptionParser(usage=usage)

    (options, args) = parser.parse_args()
    option_dict = vars(options)

    data_path = os.path.abspath(args[0])
    image_path = os.path.abspath(args[1])

    if not os.path.isdir(image_path):
        os.mkdir(image_path)

    file_names = humansorted(listdir_fullpath(data_path))
    data_files = file_names[1:6] + file_names[-1:]
    # data = file_names[1:] + file_names[:1]

    names = unpickle(file_names[0])

    with open('label_names.txt', 'w') as of:
        of.write('Class,Label\n')
        for index, label in enumerate(names[b'labels']):
            of.write(str(index) + ',' + str(label) + '\n')

    count = 1
    with open('data.csv', 'w') as of:
        of.write('Image,Class\n')
        for index, file_name in enumerate(data_files):
            image_list, labels = load_data(file_name)
            for ind, image in enumerate(image_list):
                file_path = os.path.join(image_path, str(count) + '.jpg')
                Image.fromarray(image).save(file_path)
                of.write(file_path + ',' + str(labels[ind]) + '\n')
                count += 1
