import os
import glob
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


# video
path = "/home/dcs_2017/Documents/Examples/Classification/video/humanactions/"
new_path = '/DM-Dash/domtest/classification/'
# labels = ['boxing', 'handclapping', 'handwaving',
#           'jogging', 'running', 'walking']
labels = ['0', '1', '2', '3', '4', '5']
# # audio
# path = "/home/dcs_2017/Documents/Examples/Classification/audio/genres/"
# labels = ['0', '1', '2', '3',
#           '4', '5', '6', '7', '8', '9']
data = csv_data(path)

data = [d.replace(
    '/home/dcs_2017/Documents/Examples/Classification/', new_path) for d in data]
csv_dataset = csv_labels(data, labels)[1]

count = 1
with open('video_data.csv', 'w') as of:
    of.write('Data,Label\n')
    for ind, line in enumerate(csv_dataset):
        of.write(line[0] + ',' + line[1] + '\n')
        count += 1

with open('query.csv', 'w') as of:
    of.write('Data\n')
    for ind, line in enumerate(csv_dataset):
        of.write(line[0] + '\n')
        count += 1
