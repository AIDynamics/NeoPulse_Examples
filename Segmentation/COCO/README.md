# Introduction
These sample .nml files are for training a BlendMask model using image data in [NeoPulse® AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
The data for this task can be found at: http://images.cocodataset.org/annotations/
To run this example, first you will need to download the raw data for the COCO2017 task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

Note: The default setting of build_csv.py only generates 200 images and labels in the dataset. If user would like to get the whole COCO2017 dataset, please change line 15 in build_csv.py, setting "WholeCOCO" to True and run again.

If the script fails, make sure that you have installed all the package dependencies of this script which are: `gzip, os, shutil, pathlib, numpy, requests, imageio, and python-mnist`.

Missing packages can be installed using pip:
```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -path /absolute/path/to/BlendMask_one_line.nml
```
In NML file, relative path of .csv file is declared in the line:
```bash
bind = "training_data.csv" ;
```

# Tutorial Files
**build_csv.py:** Script creates list of training files and writes training full image paths and corresponding labels to a training CSV file.

**BlendMask_one_line.nml:** Training Resnet50 Based blendmask against COCO2017 Dataset.

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials* section of the [AIDynamics® Developer Portal](https://www.aidynamics.com/ai-developer)


For more information on using the ImageDataGenerator visit the [Data section] of the NeoPulse® AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)

# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.
