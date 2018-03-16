import os
import numpy as np
import itertools
import pandas as pd


def train_test_split(df, train_percent=.8, test_percent=.2, seed=None):
    np.random.seed(seed)
    perm = np.random.permutation(df.index)
    m = len(df.index)
    train_end = int(train_percent * m)
    test_end = int(test_percent * m) + train_end
    train = df.ix[perm[:train_end]]
    test = df.ix[perm[train_end:test_end]]
    return train, test


# Import data
data = pd.read_csv(
    '/home/dcs_2017/Documents/domtest/regression/image/drivPoints.txt', quotechar='"')

# Append correct filename
data['fileName'] = '/DM-Dash/domtest/regression/image/DrivImages/' + \
    data['fileName'].astype(str) + '.jpg'

## Normalize Data ##
data_to_norm = ['ang', 'xF', 'xF', 'yF', 'wF', 'hF', 'xRE',
                'yRE', 'xLE', 'yLE', 'xN', 'yN', 'xRM', 'yRM', 'xLM', 'yLM']

data[data_to_norm] = (data[data_to_norm].apply(
    lambda x: (x - x.mean()) / (x.max() - x.min())))

# Perform train/test split
train, test = train_test_split(data)

# Remove unnecessary columns
train.drop(['subject', 'imgNum'], axis=1, inplace=True)
test.drop(['subject', 'imgNum', 'label'], axis=1, inplace=True)


# Concatenate columns into flat vector
train_to_vector = train.ix[:, ['ang', 'xF', 'xF', 'yF', 'wF', 'hF', 'xRE',
                               'yRE', 'xLE', 'yLE', 'xN', 'yN', 'xRM', 'yRM', 'xLM', 'yLM']]
train_to_vector['data'] = train_to_vector.apply(lambda x: '|'.join(
    x.dropna().astype(str).values), axis=1)
test['data'] = test.apply(lambda x: '|'.join(
    x.dropna().astype(str).values), axis=1)

train = pd.concat([train['fileName'], train['label']], axis=1)

## Check file length ##
print('\nLength of train file:  ' + str(len(train)))
print('\nLength of test file:   ' + str(len(test)))


# Export clean CSVs
train.to_csv(
    '/home/dcs_2017/Documents/domtest/regression/image/drive_train.csv', index=False)
# remove label column for test
test_header = ["fileName"]
test.to_csv(
    '/home/dcs_2017/Documents/domtest/regression/image/drive_test.csv', columns=test_header, index=False)
