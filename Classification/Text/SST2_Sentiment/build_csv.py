import os
import zipfile
import urllib.request as urllib
import pandas as pd
from pathlib import Path
import shutil


def download_data():
    """
    Check if raw data is ppresent. If not, download it.
    """
    
    URL = 'https://dl.fbaipublicfiles.com/glue/data/SST-2.zip'
    file_list = ['train.tsv']
    data_dir = 'SST-2'
    for f in file_list:
        if not Path(data_dir + '/' + f).is_file():
            cwd = os.getcwd()
            data_file = os.path.join(cwd, 'SST-2.zip')
            
            urllib.urlretrieve(URL, data_file)
            with zipfile.ZipFile(data_file) as zip_ref:
                zip_ref.extractall(cwd)
            os.remove(data_file)

def write_training_data():
    """
    Write a csv file containing the text and labels.
    """

    CSV_FILE = 'training_data.csv'
    TSV_FILE = 'train.tsv'
    cwd = os.getcwd()
    data_file = os.path.join(cwd, 'SST-2', TSV_FILE)

    tr_df = pd.read_csv(data_file, sep='\t', header=0)
    tr_df.to_csv(CSV_FILE, index=False)


def write_inference_data():
    """
    Write a csv file that contains only the validation data without labels for inference
    """

    CSV_FILE = 'query.csv'
    TSV_FILE = 'test.tsv'
    cwd = os.getcwd()
    data_file = os.path.join(cwd, 'SST-2', TSV_FILE)

    val_df = pd.read_csv(data_file, sep='\t', header=0)
    
    # Remove index column
    del val_df['index']

    val_df.to_csv(CSV_FILE, index=False)

if __name__ == '__main__':
    download_data()

    write_training_data()
    write_inference_data()
    
    # Remove downloaded files    
    path = os.path.join(os.getcwd(), 'SST-2')
    shutil.rmtree(path)
