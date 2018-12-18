import shutil
import tarfile
from pathlib import Path

import pandas as pd
import requests
from natsort import humansorted
from sklearn.datasets import load_files


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


def write_data(dir, save_as):
    '''
    Write a csv file containing the text and labels.
    '''
    df = pd.DataFrame()
    shutil.move('aclImdb/train/unsup', '.')
    for d in humansorted([str(p) for p in Path(dir).iterdir() if p.is_dir()], reverse=True):
        print(d)
        data = load_files(d)
        pd_form = {"Review": data.data, "Label": data.target}
        df = df.append(pd.DataFrame(pd_form))
    shutil.move('unsup', 'aclImdb/train')
    df.to_csv(save_as, index=False)


def load_query(direc, save_as):
    data = load_files(direc)
    pd_form = {"Review": data.data}
    pd.DataFrame(pd_form).loc[1:5, :].to_csv(save_as, index=False)

if __name__ == "__main__":

    download_data()

    write_data('aclImdb', 'training_data.csv')
