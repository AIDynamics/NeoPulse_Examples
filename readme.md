# Introduction
This is a tutorial image classification using CIFAR-10, CIFAR-100, and MNIST in [NeoPulse™ AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

[CIFAR-10](http://www.cs.toronto.edu/~kriz/cifar.html), an image classification dataset contains 60000 32X32 color images with 6000 images per class. There are 50000 training images and 10000 test images.

[CIFAR-100](http://www.cs.toronto.edu/~kriz/cifar.html) is very similar to CIFAR-10 except it contains 100 classes with 600 images per class (500 training and 100 testing). The 100 classes are under 20 superclasses ('coarse labels').

[MNIST](yann.lecun.com/exdb/mnist/) is a database of handwritten digits often used for pattern recognition. The dataset contains 60000 28X28 greyscale images. 50000 training images and 10000 test images are included.

# Tutorial Videos
Tutorial videos are available in the *Tutorials & Guides* section of the [DimensionalMechanics™ Developer Portal](https://dimensionalmechanics.com/ai-developer-portal)

# Tutorial Files
The following NeoPulse™ Modeling Language (NML) scripts can be used to train CIFAR-10, CIFAR-100, and MNIST datasets in NeoPulse™ AI Studio. Each file demonstrates a different level of direct hints in building a model architecture (more details on [direct hints](https://docs.neopulse.ai/NML-Oracle-direct/)):

**build_csv.py:** This program extracts data, writes images and labels to CSV file, and saves images to disk.  

**cifar10_full_auto.nml:** Demonstrates using [full auto architecture](https://docs.neopulse.ai/NML-architecture/)

**cifar10_call_auto.nml:** Demonstrates using call-level auto.

**cifar10_choice_auto.nml:** Demonstrates using choice syntax.

**cifar10_dist_auto.nml:** Demonstrates distribution syntax

CIFAR-100 and MNIST files follow the exact format as the files above.

# Download
Files in this repository are easily accessible by [cloning this link](https://github.com/DimensionalMechanics/NeoPulse-Examples.git):

# License
Tutorial materials are published under DimensionalMechanics™ license. See license for commercial, academic, and personal usage.

You are welcome to modify these tutorial files. If citing please link to this repository.
