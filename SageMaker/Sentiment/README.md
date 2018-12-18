# Introduction
This is an example exercise to run on Amazon SageMaker. These files will demonstrate the usage of the NeoPulse® Modeling Language and the AI oracle of the NeoPulse® Framework Algorithm, now available to run on both [CPU](https://aws.amazon.com/marketplace/pp/prodview-die5a2b34vjii) and [GPU](https://aws.amazon.com/marketplace/pp/prodview-7fngm7wimrfwy) instances.

# Tutorial Files
This tutorial contains several files, the use of which will be explained in the directions below. They are described at a high level here.

**README.md:** This file.

**build_csv.py:** This python script downloads the [IMBD dataset](http://ai.stanford.edu/~amaas/data/sentiment) and builds a CSV file containing the data that is ready to use to train a model.

**sentiment_full_auto.nml:** Features full use of the auto keyword to automatically generate the entire architecture for a model, as well as several hyper paramters.

**sentiment_call_auto.nml:** Features an examples of the use of the auto keyword to automatically select different layer parameters.

**sentiment_choice_auto.nml:** Features an example of the use of the auto keyword to probabilistically choose between different parameters or hyperparameters.

**sentiment_dist_auto.nml:** Features and example of the use of the auto keyword to sample a uniform distribution of parameters or hyperparameters

**sentiment_multi-GPU.nml:** Features an example of how to use the multi-GPU functionality (for use on instances with more than one GPU).

# Tutorial Instructions

To use this tutorial, you will need an [AWS account](https://aws.amazon.com/free/) with access to [Amazon SageMaker](https://aws.amazon.com/sagemaker/). You will need to have generated [AWS IAM credentials](https://aws.amazon.com/iam/) that allow programmatic access via the [AWS Command Line Interface](https://aws.amazon.com/cli/) or you will upload the data to Amazon S3 using the console.

Documentation for how to use the NeoPulse® Framework Algorithm on AWS SageMaker from the AWS console is [available here.](https://docs.neopulse.ai/NP-SageMaker/) Succesfully completing this tutorial will download the raw data, pre-process it, and upload the data and an NML script for training to Amazon S3. 

# Data
The data for this example can be found at: http://ai.stanford.edu/~amaas/data/sentiment. To run this example, first you will need to download and pre-process the raw data for the task using the included ```build_csv.py``` script:

```bash
$ python build_csv.py
```

If the script fails, make sure that you have installed all the package dependencies of this script which are: `natsort, pandas, requests, and sklearn`.

Missing packages may be installed using pip:
```bash
$ pip install <package_name>
```

The script will download the tarball archive to the directory <b>raw_data</b>, extract the tarball to a directory <b>aclImdb</b>, and parse the raw data to create the file <b>training_data.csv</b>.

Now we'll create a directory to sync to S3, so that only the necessary data and NML files get synced (to save on storage costs):

```bash
$ mkdir s3_bucket; cp training_data.csv s3_bucket
```

Now we'll copy the NML script that we want to execute in SageMaker. Make sure that the file you copy into the directory is named <b>train.nml</b> as this is what the NeoPulse® Framework Algorithm will look for to begin training.

```bash
$ cp sentiment_full_auto.nml s3_bucket/train.nml
```

Now sync the directory to S3:

```bash
$ cd s3_bucket
$ aws s3 sync . s3://<your_bucket_name>
```

<b>NOTE: You can also use the AWS console to sync the directory as shown in the [documentation](https://docs.neopulse.ai/NP-SageMaker/).

Now you are ready to use Amazon SageMaker to train your model. Head to the SageMaker console, and start your training job.

# License
Tutorial materials are published under the MIT license. See LICENSE for terms for commercial, academic, and personal use.
