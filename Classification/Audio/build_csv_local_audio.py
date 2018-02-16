import os
import glob
import zipfile
import optparse
import numpy as np
import itertools
from natsort import humansorted

music_list = []
home = "/home/dcs_2017/Documents/Examples/Classification/audio/genres/"
for root, dirs, files in os.walk(home, topdown=False):
    for name in files:
        music_list.append(os.path.join(root, name))
music_list = sorted(music_list)

# generate labels
genres = ['blues', 'classical', 'country',
          'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
genre_list = list(itertools.chain.from_iterable(
    itertools.repeat(x, 100) for x in genres))

# combine list to build CSV list
music_dataset = list(zip(music_list, genre_list))


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


count = 1
with open('data.csv', 'w') as of:
    of.write('Data,Label\n')
    for ind, line in enumerate(music_dataset):
        of.write(line[0] + ',' + line[1] + '\n')
        count += 1
