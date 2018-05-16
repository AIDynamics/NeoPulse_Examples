import os
import shutil

import pandas as pd
from sklearn.datasets import load_files


def load_data(direc, save_as):
    data = load_files(direc)
    pd_form = {"Review": data.data, "Label": data.target}
    pd.DataFrame(pd_form).to_csv(save_as, index=False)


def load_query(direc, save_as):
    data = load_files(direc)
    pd_form = {"Review": data.data}
    pd.DataFrame(pd_form).loc[1:5, :].to_csv(save_as, index=False)

if __name__ == "__main__":

    os.mkdir('aclImdb/unsup')
    os.rename('aclImdb/train/unsup', 'aclImdb/unsup/data')
    load_data("aclImdb/train", "train_data.csv")
    load_data("aclImdb/test", "test_data.csv")
    load_query("aclImdb/unsup", "query_data.csv")
    with open('combined_data.csv', 'w') as wfd:
        shutil.copyfileobj(open('train_data.csv', 'r'), wfd)
        tmp = open('test_data.csv', 'r')
        tmp.readline()
        shutil.copyfileobj(tmp, wfd)
