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
the /DM-Dash directory of your instance. If you have put it somewhere else, you'll need to move the NML files into a location under the /DM-Dash directory, and change the path in the line:
```bash
bind = "/DM-Dash/NeoPulse_Examples/Classification/Image/MNIST/training_data.csv" ;
```
