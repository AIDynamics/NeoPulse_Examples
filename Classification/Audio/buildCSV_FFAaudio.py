import os
import numpy as np
import itertools
import pandas as pd
from natsort import humansorted


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


path = "/home/dcs_2017/Documents/domtest/classification/audio/genres/"
new_path = "/DM-Dash/"

# Specify category labels
# genres = ['blues', 'classical', 'country',
#           'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Read data from data folders
music_list = csv_data(path)

# Replace old path with new path (where data will reside on instance)
music_list = [d.replace(
    '/home/dcs_2017/Documents/', new_path) for d in music_list]

# Create raw CSV dataset
csv_dataset = csv_labels(music_list, labels)

# Import data
data = pd.DataFrame(list(csv_dataset[1]), columns=['Data', 'Labels'])

# Perform train/test split
train, test = train_test_split(data)

# Remove labels for test(query) file
test.drop(['Labels'], axis=1, inplace=True)

## Check file length ##
print('\nLength of train file:  ' + str(len(train)))
print('\nLength of test file:   ' + str(len(test)))

# Export clean CSVs

train.to_csv(
    '/home/dcs_2017/Documents/domtest/classification/audio/audio_train_TEST.csv', index=False)

test.to_csv(
    '/home/dcs_2017/Documents/domtest/classification/audio/audio_test_TEST.csv', index=False)
