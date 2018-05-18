# Introduction
These sample .nml files are for training a regression model using image data in [NeoPulse™ AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
Data for these examples are from the [DrivFace](https://archive.ics.uci.edu/ml/datasets/DrivFace/#) dataset.

The DrivFace dataset features 640x480 pixel color images across 4 drivers (2 women and 2 men) in real-life driving scenarios.

This tutorial uses regression to predict a bounding box for the face.

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials & Guides* section of the [DimensionalMechanics™ Developer Portal](https://dimensionalmechanics.com/ai-developer-portal)

For more information on using the ImageDataGenerator visit the [Data section] of the NeoPulse™ AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)

# Tutorial Files
**build_csv.py:** Script creates list of training files and writes training full image paths and corresponding vectors to a training CSV file.

**drive_auto.nml:** Features full use of the auto keyword to automatically generate the entire architecture.

# License
Tutorial materials are published under the MIT license. See license for commercial, academic, and personal use.
