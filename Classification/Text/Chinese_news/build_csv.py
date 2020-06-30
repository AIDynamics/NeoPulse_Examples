import shutil
import tarfile
from pathlib import Path

import pandas as pd
import requests
from natsort import humansorted
from sklearn.datasets import load_files
from subprocess import run, PIPE

from io import StringIO


def download_data():
    """
    Check if raw IMDB data is present. If not, download data from the official site.
    """

    URL = "https://drive.google.com/uc?authuser=0&id=1Jg3EcJEB48-B_dGeOGMoLzJg_HjSnY67&export=download"
    if not Path("training_data.csv").is_file():
        r = requests.get(URL, stream=True)
        with open("training_data.csv", "wb") as f_z:
            shutil.copyfileobj(r.raw, f_z)

    cp = run(["head", "-n2", "training_data.csv"], stdout=PIPE, stderr=PIPE)
    df = pd.read_csv(StringIO(cp.stdout.decode("utf-8")))
    del df["label"]
    df.to_csv("query.csv", header=True, index=False)


if __name__ == "__main__":

    download_data()
