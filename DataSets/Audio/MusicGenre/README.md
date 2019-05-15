# Introduction
These sample .nml files are for training a classification model using audio data in [NeoPulse™ AI Studio](https://aws.amazon.com/marketplace/pp/B074NDG36S/ref=vdr_rf).

# Data
Data for this example is from the [Music Genres Dataset](http://opihi.cs.uvic.ca/sound/genres.tar.gz). The dataset features 100 audio samples from 10 music genres.
To run this example, first you will need to download and pre-process the raw data for the music classification task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

If the script fails, make sure that you have installed all the package dependencies of this script which are listed at the top of the script:
`tarfile, shutil, pathlib, requests, natsort, and random`. Missing packages can be installed using pip:

```bash
$ pip install <package_name>
```

Once you've downloaded and pre-processed the data, you can start training using any of the NML scripts provided. To begin training:
```bash
$ neopulse train -p <project_name> -f /full/path/to/music_classification_auto.nml
```

<b>NOTE: Audio files are big! Be careful with your batch size, or you may get out of memory (OOM) errors. If that happens, reduce the batch size.</b>

# Tutorial Videos and Guides
Tutorial videos are available in the *Tutorials & Guides* section of the [DimensionalMechanics™ Developer Portal](https://dimensionalmechanics.com/ai-developer-portal)
For more information on using the AudioDataGenerator visit the [Data section] of the NeoPulse™ AI Studio Documentation(https://docs.neopulse.ai/NML-source/#data)


# License
Tutorial materials are published under the MIT license. See LICENSE for commercial, academic, and personal use.

You are welcome to modify these tutorial files. If citing please link to this repository.