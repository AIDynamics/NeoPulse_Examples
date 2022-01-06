# Introduction
These sample .nml files are for training a regression model using image data in [NeoPulse® AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
Data for these examples are from the [DrivFace](https://archive.ics.uci.edu/ml/datasets/DrivFace/#) dataset.

The DrivFace dataset features 640x480 pixel color images across 4 drivers (2 women and 2 men) in real-life driving scenarios.

This tutorial uses regression to predict a bounding box for the face.

To run this example, first you will need to download and pre-process the raw data for the task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

If the script fails, make sure that you have installed all the package dependencies of this script which are: `shutil, pathlib, random, pandas, requests, zipfile, and imageio`.

Missing packages can be installed using pip:
```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -path /absolute/path/to/drivface.nml
```
In NML file, relative path of .csv file is declared in the line:
```bash
bind = "training_data.csv" ;
```


# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials* section of the [AIDynamics® Developer Portal](https://www.aidynamics.com/ai-developer)


For more information on using the ImageDataGenerator visit the [Data section] of the NeoPulse® AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)

# Tutorial Files
**build_csv.py:** Script creates list of training files and writes training full image paths and corresponding vectors to a training CSV file.

# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.
