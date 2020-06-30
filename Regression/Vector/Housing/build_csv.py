import itertools
import os

import numpy as np
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


if __name__ == '__main__':
    write_csv_file()
