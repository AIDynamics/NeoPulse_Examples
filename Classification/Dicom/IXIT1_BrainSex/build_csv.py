import os
import shutil
import tarfile
from pathlib import Path
from random import shuffle

import requests

import pandas as pd
from natsort import humansorted


def download_data():
    '''
    Check if raw IXI dicom data is present. If not, download data from the
    official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    nii_URL = 'http://biomedic.doc.ic.ac.uk/brain-development/downloads/IXI/IXI-T1.tar'
    xls_URL = 'http://biomedic.doc.ic.ac.uk/brain-development/downloads/IXI/IXI.xls'

    nii_f = 'IXI_T1.tar.gz'
    xls_f = 'IXI.xls'

    if not Path('raw_data/' + nii_f).is_file():
        r = requests.get(nii_URL, stream=True)
        with open('raw_data/' + nii_f, 'wb') as f_z:
            shutil.copyfileobj(r.raw, f_z)

    Path('images').mkdir(parents=True, exist_ok=True)
    tarfile.open('raw_data/' + nii_f).extractall('images/')

    if not Path('raw_data/' + xls_f).is_file():
        r = requests.get(xls_URL, stream=True)
        with open('raw_data/' + xls_f, 'wb') as f_z:
            shutil.copyfileobj(r.raw, f_z)


def write_file(validation_split):

    xls = pd.ExcelFile("raw_data/IXI.xls")
    df = xls.parse('Table')
    img_plist = os.listdir("images")

    pdict = {}

    csv_lines = []

    cwd = Path.cwd()

    for img_p in img_plist:
        if img_p[:3] == "IXI":
            pdict[int(img_p[3:6])] = img_p

    for index, row in df.iterrows():
        IXI_id = int(row['IXI_ID'])
        sex_id = row['SEX_ID (1=m, 2=f)']
        sex_id -= 1
        if IXI_id in pdict:
            csv_lines.append("{0},{1}\n".format("images/" + pdict[IXI_id], sex_id))

    shuffle(csv_lines)

    split_index = int(validation_split * len(csv_lines))

    train = csv_lines[:-split_index]
    valid = csv_lines[-split_index:]

    # Write the training CSV file.
    with open('training_data.csv', 'w') as of:
        of.write('data,label\n')
        for l in train:
            of.write(l)
        for l in valid:
            of.write(l)

    # Write the querying CSV file.
    with open('querying_data.csv', 'w') as of:
        of.write('data\n')
        for l in valid:
            of.write(l.split(',')[0] + '\n')


if __name__ == '__main__':

    # Download data if necessary
    download_data()

    # Write files with 20% validation split
    write_file(0.2)
