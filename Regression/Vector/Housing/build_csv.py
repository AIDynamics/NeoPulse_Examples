import os
import numpy as np
import itertools
import pandas as pd


from sklearn.datasets import load_boston

def write_csv_file(train_test_split=0.2):

    boston = load_boston()
    data = boston.data[:, :12]
    price = boston.data[:, 12]

    data_lines = ['|'.join([str(e) for e in linedata]) for linedata in data]

    split_index = int(train_test_split * len(data_lines))

    training_data_lines = data_lines[split_index:]
    training_price = price[split_index:]
    querying_data_lines = data_lines[:split_index]
    querying_price = price[:split_index]


    with open('training_data.csv', 'w') as wf:
        wf.write("Data,Price\n")
        for lid in range(len(training_data_lines)):
            wf.write("{},{}\n".format(training_data_lines[lid], training_price[lid]))

    with open('query.csv', 'w') as wf:
        wf.write("Data\n")
        for line in querying_data_lines:
            wf.write(line + '\n')



write_csv_file()



'''


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
    '/home/dcs_2017/Documents/domtest/regression/text/ex1data2.txt', quotechar='"')

## Normalize Data ##
data = (data.apply(
    lambda x: (x - x.mean()) / (x.max() - x.min())))

# Perform train/test split
train, test = train_test_split(data)

# Remove category labels from test (query) file
test.drop(['price'], axis=1, inplace=True)


# Concatenate columns into flat vector
train_to_vector = data.ix[:, ['sqft', 'bdrms']]

train_to_vector['Data'] = train_to_vector.apply(lambda x: '|'.join(
    x.dropna().astype(str).values), axis=1)
test['Data'] = test.apply(lambda x: '|'.join(
    x.dropna().astype(str).values), axis=1)

train = pd.concat([train_to_vector['Data'], data['price']], axis=1)

## Check file length ##
print('\nLength of train file:  ' + str(len(train)))
print('\nLength of test file:   ' + str(len(test)))


# Export clean CSVs
train.to_csv(
    'training_data.csv', index=False)

test_header = ["Data"]
test.to_csv(
    'query.csv', columns=test_header, index=False)
'''

