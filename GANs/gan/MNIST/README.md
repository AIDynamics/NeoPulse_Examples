# Introduction
These sample .nml files are for training a gan model using image data in [NeoPulse™ AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
The data for this task can be found at: http://yann.lecun.com/exdb/mnist/
To run this example, first you will need to download and pre-process the raw data for the MNIST task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

If the script fails, make sure that you have installed all the package dependencies of this script which are: `gzip, os, shutil, pathlib, numpy, requests, imageio, and python-mnist`.

Missing packages can be installed using pip:
```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -f /DM-Dash/NeoPulse_Examples/GANs/gan/MNIST/mnist_gan.nml
```
The paths in the NML scripts in this directory assume that you have cloned this repository into the /DM-Dash directory of your machine. If you have put it somewhere else, you'll need to move the NML files into a location under the /DM-Dash directory, and change the path in the line:
```bash
bind = "/DM-Dash/NeoPulse_Examples/GANs/gan/MNIST/training_data.csv" ;
```

# Tutorial Files
**build_csv.py:** Script creates list of training files and writes training full image paths and a vector of noise to a training CSV file.

**mnist_gan.nml:** Full self-defined architecture without any automation.

**mnist_gan_auto.nml:** Features full use of the auto keyword to automatically generate the entire architecture and set hyperparameters as default values.

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials & Guides* section of the [DimensionalMechanics™ Developer Portal](https://dimensionalmechanics.com/ai-developer-portal)

For more information on using the ImageDataGenerator visit the [Data section] of the NeoPulse™ AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)

# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.
