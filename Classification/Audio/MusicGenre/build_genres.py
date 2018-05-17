def download_data():
    '''
    Check if raw music genre data is present. If not, download data from the
    official site.
    '''
    import requests
    import tarfile
    import shutil
    from pathlib import Path

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'http://opihi.cs.uvic.ca/sound/'
    f = 'genres.tar.gz'
    if not Path('raw_data/' + f).is_file():
        r = requests.get(URL + f, stream=True)
        with open('raw_data/' + f, 'wb') as f_z:
            shutil.copyfileobj(r.raw, f_z)
        tarfile.open('raw_data/' + f).extractall()


def flatten(l):
    return [item for sublist in l for item in sublist]


def write_file(validation_split):
    '''
    Iterate through genres and write csv file using the supplied validation_split.

    1. Data from each genre is shuffled and then sampled into the training
       and validation sets respectively.
    2. Both the training and validation sets are then re-shuffled to intermix
       the different genres.
    3. The resulting
    '''
    from pathlib import Path
    from natsort import humansorted
    from random import shuffle

    train = []
    valid = []

    # Sort the genres alphabetically.
    genres = humansorted([str(p) for p in Path('genres').iterdir()])
    with open('label_names.txt', 'w') as of:
        of.write('Class,Label\n')
        for index, d in enumerate(genres):
            of.write(str(index) + ',' + d.split('/')[-1] + '\n')
            # Construct lines for the csv file in the form:
            # /path/to/audio/file.au,class_number
            # where class_number is the index of each genre class.
            csv_lines = humansorted(['/DM-Dash/NeoPulse_Examples/Classification/Audio/' + str(p) + ',' + str(index) + '\n' for p in Path(d).iterdir()])
            # shuffle the list:
            shuffle(csv_lines)
            # calculate the index on which to split the list into training/validation
            # and then add to the respective lists.
            split_index = int(validation_split * len(csv_lines))
            train.append(csv_lines[:-split_index])
            valid.append(csv_lines[-split_index:])

    # Flatten and shuffle the resulting lists.
    train = flatten(train)
    valid = flatten(valid)
    shuffle(train)
    shuffle(valid)

    # Write the CSV file.
    with open('training_data.csv', 'w') as of:
        of.write('Audio File,Genre\n')
        for l in train:
            of.write(l)
        for l in valid:
            of.write(l)


if __name__ == '__main__':

    # Download data if necessary
    download_data()

    # Write files with 20% validation split
    write_file(0.2)
