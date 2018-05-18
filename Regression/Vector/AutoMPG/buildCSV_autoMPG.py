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
    '/home/dcs_2017/Documents/domtest/regression/vector/auto_mpg.csv', quotechar='"')
# Drop nominal variable
data.drop(['car_name'], axis=1, inplace=True)

# Remove unwanted characters
data = data.apply(pd.to_numeric, args=('coerce',))
data = data.fillna(data.mean())


## Normalize Data ##
data_to_norm = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year',
                'origin']

data[data_to_norm] = (data[data_to_norm].apply(
    lambda x: (x - x.mean()) / (x.max() - x.min())))

# Perform train/test split
train, test = train_test_split(data)

# Remove label column from test (query) file
test.drop(['mpg'], axis=1, inplace=True)


# Concatenate columns into flat vector
train_to_vector = train.ix[:, ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year',
                               'origin']]
train_to_vector['data'] = train_to_vector.apply(lambda x: '|'.join(
    x.dropna().astype(str).values), axis=1)
test['data'] = test.apply(lambda x: '|'.join(
    x.dropna().astype(str).values), axis=1)

train = pd.concat([train_to_vector['data'], train['mpg']], axis=1)

## Check file length ##
print('\nLength of train file:  ' + str(len(train)))
print('\nLength of test file:   ' + str(len(test)))


# Export clean CSVs
train.to_csv(
    '/home/dcs_2017/Documents/domtest/regression/vector/auto_train.csv', index=False)
# remove label column for test
test_header = ["data"]
test.to_csv(
    '/home/dcs_2017/Documents/domtest/regression/vector/auto_test.csv', columns=test_header, index=False)
