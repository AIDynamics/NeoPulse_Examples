import os
import numpy as np
import itertools
import pandas as pd
from random import shuffle
from pathlib import Path
import requests
import shutil


def download_data():
    '''
    Check if raw data is present. If not, download data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/'
    f = 'auto-mpg.data'

    if not Path('raw_data/' + f).is_file():
        r = requests.get(URL + f, stream=True)
        with open('raw_data/' + f, 'wb') as f_z:
            shutil.copyfileobj(r.raw, f_z)

def write_csv_file(validation_split=0.1):

    csv_lines = []

    with open('raw_data/auto-mpg.data', 'r') as rf:
        raw_lines = rf.readlines()

        for line in raw_lines:
            valid = True
            line = line.replace("\t"," ")
            elems = [e for e in line.split(' ') if e not in [" ", "","\t"] and e.replace(".","",1).isdigit()]

            if len(elems) == 8:

                c_data = '|'.join(elems[1:8])
                c_mpg = elems[0]
                csv_lines.append("{},{}".format(c_data, c_mpg))

    shuffle(csv_lines)

    split_index = int(validation_split * len(csv_lines))
    training_lines = csv_lines[split_index:]
    querying_lines = csv_lines[:split_index]


    with open('training_data.csv', 'w') as wf:
        wf.write("data,mpg\n")
        for line in training_lines:
            wf.write(line + '\n')

    with open('query.csv', 'w') as wf:
        wf.write("data\n")
        for line in querying_lines:
            wf.write(line.split(',')[0] + '\n')


if __name__ == '__main__':

    # Download data if necessary
    download_data()

    # Write files with 20% validation split
    write_csv_file(0.2)
