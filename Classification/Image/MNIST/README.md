# Introduction
These sample .nml files are for training a classification model using audio data in [NeoPulse™ AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
The data for this task can be found at: http://yann.lecun.com/exdb/mnist/
To run this example, first you will need to download and pre-process the raw data for the MNIST task using the included ```build_mnist.py``` script:

```bash
$ python build_mnist.py
```

If the script failes, make sure that you have installed all the package dependencies of this script which are listed at the top of the script:
`gzip, os, shutil, pathlib, numpy, requests, imageio, and python-mnist`. Missing packages can be installed using pip:

```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -f /DM-Dash/NeoPulse_Examples/Classification/Image/MNIST/mnist_full_auto.nml
```
The paths in the NML scripts in this directory assume that you have cloned this repository into
the /DM-Dash directory of your machine. If you have put it somewhere else, you'll need to move the NML files into a location under the /DM-Dash directory, and change the path in the line:
```bash
bind = "/DM-Dash/NeoPulse_Examples/Classification/Image/MNIST/training_data.csv" ;
```

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials & Guides* section of the [DimensionalMechanics™ Developer Portal](https://dimensionalmechanics.com/ai-developer-portal)
For more information on using the AudioDataGenerator visit the [Data section] of the NeoPulse™ AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)


# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.

You are welcome to modify these tutorial files. If citing please link to this repository.