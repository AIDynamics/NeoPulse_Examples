# Introduction
These sample .nml files are for training a classification model using Text data in [NeoPulse® AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf). Neopulse text model support multiple languages, like Chinese, Japanese, Korean etc. This examples classify Chinese news into 10 classes, "sports":0, "science and technology": 1, "stocks": 2, "entertainment": 3, "politics": 4, "society": 5, "education": 6, "finance": 7, "house and home": 8, "games": 9

# Data
The data for this task can be found at: http://thuctc.thunlp.org/
To run this example, first you will need to download and pre-process the raw data for the task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

If the script fails, make sure that you have installed all the package dependencies of this script which are: `shutil, tarfile, pathlib, pandas, requests, natsort, and sklearn`.

Missing packages can be installed using pip:
```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -path /absolute/path/to/cnews.nml
```
In NML file, relative path of .csv file is declared in the line:
```bash
bind = "training_data.csv" ;
```

# Tutorial Files
**build_csv.py:** Script creates list of training files and writes training full image paths and corresponding labels to a training CSV file.

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials* section of the [AIDynamics® Developer Portal](https://www.aidynamics.com/ai-developer)


For more information on using the AudioDataGenerator visit the [Data section] of the NeoPulse® AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)

# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.
