# Introduction
These sample .nml files are for training a classification model using dicom(Digital Imaging and Communications in Medicine) data in [NeoPulse® AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
Data for this example is from the [IXI-T1 Dataset](http://biomedic.doc.ic.ac.uk/brain-development/downloads/IXI/IXI-T1.tar). The dataset contains 591 human brain 3D MR Images with T1 weighted, and corresponding gender label of each image, male or female.
To run this example, first you will need to download and pre-process the raw data for the dicom classification task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

If the script failes, make sure that you have installed all the package dependencies of this script which are listed at the top of the script:
`tarfile, shutil, pathlib, requests, natsort, pandas and random`. Missing packages can be installed using pip:

```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -path /absolute/path/to/dicom_sex.nml
```
In NML file, relative path of .csv file is declared in the line:
```bash
bind = "training_data.csv" ;
```

<b>NOTE: Dicom files are big! Be careful with your batch size, or you may get out of memory (OOM) errors. If that happens, reduce the batch size.</b>

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials* section of the [AIDynamics® Developer Portal](https://www.aidynamics.com/ai-developer)

For more information on using the AudioDataGenerator visit the [Data section] of the NeoPulse® AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)


# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.

You are welcome to modify these tutorial files. If citing please link to this repository.
