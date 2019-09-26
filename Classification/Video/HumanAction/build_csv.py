import shutil
from pathlib import Path
from random import shuffle
from zipfile import ZipFile

import requests
from natsort import humansorted


def download_data():
    '''
    Check if raw data is present. If not, download data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'http://www.nada.kth.se/cvap/actions/'
    file_list = ['boxing.zip', 'handwaving.zip', 'handclapping.zip', 'jogging.zip', 'running.zip', 'walking.zip']
    for f in file_list:
        if not Path('raw_data/' + f).is_file():
            r = requests.get(URL + f, stream=True)
            with open('raw_data/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)

            extract_path = 'videos/' + f.split('.')[0]
            Path(extract_path).mkdir(parents=True, exist_ok=True)
            with ZipFile('raw_data/' + f, 'r') as zf:
                zf.extractall(extract_path)


def flatten(l):
    '''
    Flatten a list of lists.
    '''
    return [item for sublist in l for item in sublist]


def build_list(data_path, validation_split):
    '''
    Sample training and validation data sets, shuffle them, and return a
    single list in order: training_data, validation_data
    '''
    class_paths = humansorted([str(p) for p in Path(data_path).iterdir() if p.is_dir()])

    train = []
    valid = []
    for c, p in enumerate(class_paths):
        line_list = []
        for f in Path(p).iterdir():
            line_list.append(str(f.absolute()) + ',' + str(c) + '\n')

        shuffle(line_list)
        split_index = int(validation_split * len(line_list))
        train.append(line_list[:-split_index])
        valid.append(line_list[-split_index:])

    train = flatten(train)
    valid = flatten(valid)

    shuffle(train)
    shuffle(valid)

    return (train, valid)


def write_data(validation_split):
    '''
    Randomly sample training and validation datasets and write them to a csv file.
    Also, write the label names and class indexes to a text file.
    '''
    data_path = 'videos/'

    class_names = humansorted([str(p).split('/')[1] for p in Path(data_path).iterdir() if p.is_dir()])
    with open('label_names.txt', 'w') as of:
        of.write('Class,Label\n')
        for index, label in enumerate(class_names):
            of.write(str(index) + ',' + str(label) + '\n')

    (train, valid) = build_list(data_path, validation_split)
    with open('training_data.csv', 'w') as of:
        of.write('Video,Class\n')
        for line in train:
            of.write(line)

    with open('query.csv', 'w') as of:
        of.write('Video\n')
        for line in valid:
            of.write(line.split(',')[0] + '\n')    


if __name__ == '__main__':
    validation_split = 0.2
    # Download data if necessary
    download_data()
    # Write the data to PNG files, and create a csv file for NeoPulse AI Studio
    write_data(validation_split)
