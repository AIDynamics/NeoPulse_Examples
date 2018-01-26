# Introduction
These sample .nml files are for training a classification model using image data in [NeoPulse™ AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
Data for these examples are from the [CIFAR 10 and 100](https://www.cs.toronto.edu/~kriz/cifar.html) and [MNIST](http://yann.lecun.com/exdb/mnist/) datasets. 

The CIFAR-10 dataset features 60,000 32x32 color images among 10 classes (6,000 images per class). CIFAR-100 version features 100 classes (600 images per class). 50,000 images are for training and 10,000 are reserved for testing. 

The MNIST dataset features 60,000 handwritten digits with 10,000 reserved for test. More information on the datasets and data formats can be found at the links above.

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials & Guides* section of the [DimensionalMechanics™ Developer Portal](https://dimensionalmechanics.com/ai-developer-portal)

For more information on using the AudioDataGenerator visit the [Data section] of the NeoPulse™ AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)

# Tutorial Files

**cifar10_full_auto.nml:** This classification model features full use of the auto keyword to automatically generate the entire architecture.

**cifar10_call_auto.nml:** This classification model features the use of auto to automatically select an architecture later.
**cifar10_choice_auto.nml:** This classification model features use of the auto keyword to automatically select from a range of values for a given parameter.

**cifar10_dist_auto.nml:** This classification model features use of the auto keyword to automatically select a value from a specified distribution of values (e.g. gaussian). 

CIFAR-100 and MNIST example NML code follows the same structure.

# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.

You are welcome to modify these tutorial files. If citing please link to this repository.
