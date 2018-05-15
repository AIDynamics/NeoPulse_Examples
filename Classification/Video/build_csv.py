def download_data():
    import requests
    import shutil
    from pathlib import Path
    from zipfile import ZipFile
    '''
    Check if raw data is present. If not, download data from the official site.
    '''

    Path('raw_data').mkdir(parents=True, exist_ok=True)

    URL = 'http://www.nada.kth.se/cvap/actions/'
    file_list = ['boxing.zip', 'handwaving.zip', 'handclapping.zip', 'jogging.zip', 'running.zip', 'walking.zip']
    for f in file_list:
        if not Path('raw_data/' + f).is_file():
            r = requests.get(URL + f, stream=True)
            with open('raw_data/' + f, 'wb') as f_z:
                shutil.copyfileobj(r.raw, f_z)

            extract_path = 'videos/' + f.split('.')[0]
            Path(extract_path).mkdir(parents=True, exist_ok=True)
            with ZipFile('raw_data/' + f, 'r') as zf:
                zf.extractall(extract_path)


def flatten(l):
    return [item for sublist in l for item in sublist]


def build_list(data_path, validation_split):
    from pathlib import Path
    from natsort import humansorted
    from random import shuffle
    class_paths = humansorted([str(p) for p in Path(data_path).iterdir() if p.is_dir()])

    train = []
    valid = []
    for c, p in enumerate(class_paths):
        line_list = []
        for f in Path(p).iterdir():
            line_list.append(str(f.absolute()) + ',' + str(c) + '\n')

        shuffle(line_list)
        split_index = int(validation_split * len(line_list))
        train.append(line_list[:-split_index])
        valid.append(line_list[-split_index:])

    train = flatten(train)
    valid = flatten(valid)

    shuffle(train)
    shuffle(valid)

    return train.append(valid)


def write_data(validation_split):
    from natsort import humansorted
    from pathlib import Path
    data_path = 'videos/'

    class_names = humansorted([str(p).split('/')[1] for p in Path(data_path).iterdir() if p.is_dir()])
    with open('label_names.txt', 'w') as of:
        of.write('Class,Label\n')
        for index, label in enumerate(class_names):
            of.write(str(index) + ',' + str(label) + '\n')

    csv_list = build_list(data_path, validation_split)
    with open('training_data.csv', 'w') as of:
        of.write('Video,Class\n')
        for line in csv_list:
            of.write(line)


if __name__ == '__main__':
    validation_split = 0.2
    # Download data if necessary
    download_data()
    # Write the data to PNG files, and create a csv file for NeoPulse AI Studio
    write_data(validation_split)
