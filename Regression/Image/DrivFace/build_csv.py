import shutil
from pathlib import Path
from random import shuffle
from zipfile import ZipFile

import imageio
import pandas as pd
import requests


def download_data():
    '''
    Check if raw data is present. If not, download data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00378/'
    f = 'DrivFace.zip'

    if not Path('raw_data/' + f).is_file():
        r = requests.get(URL + f, stream=True)
        with open('raw_data/' + f, 'wb') as f_z:
            shutil.copyfileobj(r.raw, f_z)

        with ZipFile('raw_data/' + f, 'r') as zf:
            zf.extractall('raw_data/')
        with ZipFile('raw_data/DrivFace/DrivImages.zip', 'r') as zf:
            zf.extractall()


def write_csv(validation_split):
    '''
    Load raw csv file, pre-process it, and write training_data.csv for NeoPulse
    '''
    df = pd.read_csv('raw_data/DrivFace/drivPoints.txt')
    file_list = [str(p) for p in Path('DrivImages').iterdir()]
    shuffle(file_list)

    csv_lines = []

    for f in file_list:
        image_id = f.split('/')[-1].replace('.jpg', '')
        vec = []
        for col in ['xF', 'yF', 'wF', 'hF']:
            vec.append(df.loc[df['fileName'] == image_id][col].values[0])

        csv_lines.append(f + ',' + '|'.join([str(p) for p in vec]) + '\n')

    shuffle(csv_lines)

    split_index = int(validation_split * len(csv_lines))

    train = csv_lines[:-split_index]
    valid = csv_lines[-split_index:]

    # Write the training CSV file.
    with open('training_data.csv', 'w') as of:
        of.write('data,label\n')
        for l in train:
            of.write(l)

    # Write the querying CSV file.
    with open('query.csv', 'w') as of:
        of.write('data\n')
        for l in valid:
            of.write(l.split(',')[0] + '\n')


if __name__ == '__main__':
    download_data()
    write_csv(0.2)
