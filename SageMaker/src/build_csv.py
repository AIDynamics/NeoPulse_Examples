import shutil
import tarfile
from pathlib import Path

import pandas as pd
import requests
from natsort import humansorted
from sklearn.datasets import load_files

import zipfile

def download_data():
    '''
    Check if raw IMDB data is present. If not, download data from the official site.
    '''
    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'http://ai.stanford.edu/~amaas/data/sentiment/'
    file_list = ['aclImdb_v1.tar.gz']
    for f in file_list:
        if not Path('raw_data/' + f).is_file():
            r = requests.get(URL + f, stream=True)
            with open('raw_data/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)

            tarfile.open('raw_data/' + f).extractall()

def write_training_data():
    '''
    Write a csv file containing the text and labels.
    '''
    CSV_FILE = 'data/training/training_data.csv'
    tr_df = pd.DataFrame()
    shutil.move('aclImdb/train/unsup', '.')
    for d in humansorted([str(p) for p in Path('aclImdb').iterdir() if p.is_dir()], reverse=True):
        data = load_files(d)
        pd_form = {"Review": data.data, "Label": data.target}
        tr_df = tr_df.append(pd.DataFrame(pd_form))
    tr_df.to_csv(CSV_FILE, index=False)

    # Clean up raw data
    shutil.move('unsup', 'aclImdb/train')
    shutil.rmtree('aclImdb')
    shutil.rmtree('raw_data')
    
def write_inference_data():
    '''
    Write a csv file that contains only the validation data without labels for inference
    '''
    # Remove first column that contains the label and take the last 25000 records
    in_df = pd.read_csv("data/training/training_data.csv",header='infer')
    in_df.drop('Label', axis=1,inplace=True)
    in_df = in_df.iloc[25000:]

    # Write batch inference CSV file
    in_df.to_csv("data/transform/full_query.csv", index=False, header=True)

    # Write real-time inference CSV file
    in_df.iloc[:10].to_csv("data/transform/short_query.csv", index=False, header=True)
    
    # ZIP the CSV files
    with zipfile.ZipFile("data/transform/batch_inference.zip","w") as zf:
        zf.write("data/transform/full_query.csv", "query.csv",compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile("data/transform/realtime_inference.zip","w") as zf:
        zf.write("data/transform/short_query.csv", "query.csv",compress_type=zipfile.ZIP_DEFLATED)

