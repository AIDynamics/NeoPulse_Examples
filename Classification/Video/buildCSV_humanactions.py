import os
import numpy as np
import pandas as pd
import itertools


def csv_data(path):
    data_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            data_list.append(os.path.join(root, name))
            data_list = sorted(data_list)
    return data_list


def csv_labels(data_list, labels):  # assumes equal number of data items per label
    times = round(len(data_list) / len(labels))
    label_list = list(itertools.chain.from_iterable(
        itertools.repeat(x, times) for x in labels))
    csv_dataset = list(zip(data_list, label_list))
    return label_list, csv_dataset


def train_test_split(df, train_percent=.8, test_percent=.2, seed=None):
    np.random.seed(seed)
    perm = np.random.permutation(df.index)
    m = len(df.index)
    train_end = int(train_percent * m)
    test_end = int(test_percent * m) + train_end
    train = df.ix[perm[:train_end]]
    test = df.ix[perm[train_end:test_end]]
    return train, test


path = "/home/dcs_2017/Documents/domtest/classification/video/humanactions/"
new_path = '/DM-Dash/'

# Specify category labels
# old_labels = ['boxing', 'handclapping', 'handwaving',
#           'jogging', 'running', 'walking']
labels = ['0', '1', '2', '3', '4', '5']

# Read in data from paths
data = csv_data(path)

# Replace old path with new path (where data will reside on instance)
data = [d.replace(
    '/home/dcs_2017/Documents/', new_path) for d in data]

# Create raw CSV dataset
csv_dataset = csv_labels(data, labels)

# Import data into Pandas DataFrame
raw_data = pd.read_csv(
    '/home/dcs_2017/Documents/domtest/classification/video/video_data.csv', quotechar='"')


# Perform train/test split for training data
train, test = train_test_split(raw_data)

## Check file length ##
print('\nLength of train file:  ' + str(len(train)))
print('\nLength of test file:   ' + str(len(test)))

# Export clean CSVs

train.to_csv(
    '/home/dcs_2017/Documents/domtest/classification/video/video_train_TEST.csv')
# remove label column for test

test.to_csv(
    '/home/dcs_2017/Documents/domtest/classification/video/video_test_TEST.csv')
