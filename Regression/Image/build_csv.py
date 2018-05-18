import shutil
from pathlib import Path
from random import shuffle
from zipfile import ZipFile

import imageio
import pandas as pd
import requests


def download_data():
    '''
    Check if raw data is present. If not, download data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00378/'
    file_list = ['DrivFace.zip']
    for f in file_list:
        if not Path('raw_data/' + f).is_file():
            r = requests.get(URL + f, stream=True)
            with open('raw_data/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)

            with ZipFile('raw_data/' + f, 'r') as zf:
                zf.extractall('raw_data/')
            with ZipFile('raw_data/DrivFace/DrivImages.zip', 'r') as zf:
                zf.extractall()


def write_csv():
    '''
    Load raw csv file, pre-process it, and write training_data.csv for NeoPulse
    '''
    df = pd.read_csv('raw_data/DrivFace/drivPoints.txt')
    file_list = [str(p.resolve()) for p in Path('DrivImages').iterdir()]
    shuffle(file_list)
    with open('training_data.csv', 'w') as of:
        of.write('Image,Vector\n')
        for f in file_list:
            image_id = f.split('/')[-1].replace('.jpg', '')
            vec = []
            for col in ['xF', 'yF', 'wF', 'hF']:
                vec.append(df.loc[df['fileName'] == image_id][col].values[0])

            of.write(f + ',' + '|'.join([str(p) for p in vec]) + '\n')


if __name__ == '__main__':
    download_data()
    write_csv()

#
#
# def train_test_split(df, train_percent=.8, test_percent=.2, seed=None):
#     np.random.seed(seed)
#     perm = np.random.permutation(df.index)
#     m = len(df.index)
#     train_end = int(train_percent * m)
#     test_end = int(test_percent * m) + train_end
#     train = df.ix[perm[:train_end]]
#     test = df.ix[perm[train_end:test_end]]
#     return train, test
#
#
# # Import data
# data = pd.read_csv(
#     '/home/dcs_2017/Documents/domtest/regression/image/drivPoints.txt', quotechar='"')
#
# # Append correct filename
# data['fileName'] = '/DM-Dash/domtest/regression/image/DrivImages/' + \
#     data['fileName'].astype(str) + '.jpg'
#
# ## Normalize Data ##
# data_to_norm = ['ang', 'xF', 'xF', 'yF', 'wF', 'hF', 'xRE',
#                 'yRE', 'xLE', 'yLE', 'xN', 'yN', 'xRM', 'yRM', 'xLM', 'yLM']
#
# data[data_to_norm] = (data[data_to_norm].apply(
#     lambda x: (x - x.mean()) / (x.max() - x.min())))
#
# # Perform train/test split
# train, test = train_test_split(data)
#
# # Remove unnecessary columns
# train.drop(['subject', 'imgNum'], axis=1, inplace=True)
# test.drop(['subject', 'imgNum', 'label'], axis=1, inplace=True)
#
#
# # Concatenate columns into flat vector
# train_to_vector = train.ix[:, ['ang', 'xF', 'xF', 'yF', 'wF', 'hF', 'xRE',
#                                'yRE', 'xLE', 'yLE', 'xN', 'yN', 'xRM', 'yRM', 'xLM', 'yLM']]
# train_to_vector['data'] = train_to_vector.apply(lambda x: '|'.join(
#     x.dropna().astype(str).values), axis=1)
# test['data'] = test.apply(lambda x: '|'.join(
#     x.dropna().astype(str).values), axis=1)
#
# train = pd.concat([train['fileName'], train['label']], axis=1)
#
# ## Check file length ##
# print('\nLength of train file:  ' + str(len(train)))
# print('\nLength of test file:   ' + str(len(test)))
#
#
# # Export clean CSVs
# train.to_csv(
#     '/home/dcs_2017/Documents/domtest/regression/image/drive_train.csv', index=False)
# # remove label column for test
# test_header = ["fileName"]
# test.to_csv(
#     '/home/dcs_2017/Documents/domtest/regression/image/drive_test.csv', columns=test_header, index=False)
