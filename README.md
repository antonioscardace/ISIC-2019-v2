# ISIC-2019-v2 | Skin Tumors Classification

_Personal Machine Learning Project_<br/>
_[Antonio Scardace](https://linktr.ee/antonioscardace)_ @ _Dept of Math and Computer Science, University of Catania_

[![CodeFactor](https://www.codefactor.io/repository/github/antonioscardace/ISIC-2019-v2/badge/main)](https://www.codefactor.io/repository/github/antonioscardace/ISIC-2019-v2/overview/main)
[![License](https://img.shields.io/github/license/antonioscardace/ISIC-2019-v2.svg)](https://github.com/antonioscardace/ISIC-2019-v2/blob/master/LICENSE)
[![Open Issues](https://img.shields.io/github/issues/antonioscardace/isic-2019-v2.svg?maxAge=2592000)](https://github.com/antonioscardace/isic-2019-v2/issues)

## Introduction

The project aims to analyse and classify skin lesions by their images. The idea comes from the paper named **[Skin Lesion Analysis Toward Melanoma Detection 2018: A Challenge Hosted by the International Skin Imaging Collaboration (ISIC)](https://arxiv.org/abs/1902.03368)**. This dataset contains the training data for the ISIC 2019 challenge.

<img src="docs/images/examples.jpg" alt="Examples"/>

The dataset has been downloaded from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/isic-2019). It contains **25,331 images** available for the classification of dermoscopic images among 8 different diagnostic categories: 
* Melanocytic nevus _(NV)_ **(50.83%)**
* Melanoma _(MEL)_ **(17.85%)**
* Basal cell carcinoma _(BCC)_ **(13.12%)**
* Benign keratosis (solar lentigo / seborrheic keratosis / lichen planus-like keratosis) _(BKL)_ **(10.36%)**
* Actinic keratosis _(AK)_ **(03.42%)**
* Squamous cell carcinoma _(SCC)_ **(02.48%)**
* Vascular lesion _(VASC)_ **(01.00%)**
* Dermatofibroma _(DF)_ **(0.94%)**

Specifically, I focused my attention just on the tumours' images. Thus, I analysed **19,080 images** among 5 different diagnostic categories among the cited above. As a first version of the project, I can classify the images as **Benign Tumors** or **Malignant Tumors**. They are divided as follows: 
* Melanocytic nevus _(NV)_ **(55.72%)** - _(BENIGN)_
* Melanoma _(MEL)_ **(22.78%)** - _(MALIGNANT)_
* Basal cell carcinoma _(BCC)_ **(17.01%)** - _(MALIGNANT)_
* Squamous cell carcinoma _(SCC)_ **(03.26%)** - _(MALIGNANT)_
* Dermatofibroma _(DF)_ **(01.23%)** - _(BENIGN)_

## Project Structure

```
.
├── /settings.yml     # It is the configuration file.
├── /data/images/     # The dataset images.
├── /data/raw/        # The original immutable dataset CSV files.
├── /data/interim/    # Intermediate data that has been transformed.
├── /data/processed/  # The final, canonical dataset for training and testing.
├── /src/data/        # Classes to define and work with the dataset.
├── /src/model/       # Classes to define the CNN, train and test the model.
├── /src/utils/       # Classes to help the project development.
├── /models/          # Serialized files of the trained model.
└── /notebooks/       # Notebooks users use to build the dataset and train/test the model.
```

## Machine Learning

The Dataset was divided into a Training Set **(85%)**, and a Test Set **(15%)**.<br/>
I did Data Augmentation on the Training Set to improve the model performance.

I implemented a CNN composed of 4 Convolutional Layers and 3 Fully Connected Layers. To reduce the overfitting risk, I used Dropout layers before the first two FC layers. Batch-Normalization is also used before each layer, except the last, to accelerate the model convergence.

The final model has an accuracy of **78.41%** on the Test Set.<br/>
However, the most significant class, Malignant Tumors, is the most precise: **88.57%**.

<img src="docs/images/cmatrix.png" alt="Test Confusion Matrix"/>

## Demo Example

<img src="docs/snaps/demo.png" alt="Demo"/>

## Getting Started

So that the repository is successfully cloned and the project runs smoothly, a few steps need to be followed.

#### Requisites

* A good amount of cores (GPU is better) and RAM.
* Free disk space (> 10GB) is required.
* ``anaconda``, ``pytorch``, and ``torchvision`` are required.

#### Installation and Use

```sh
   $ git clone https://github.com/antonioscardace/ISIC-2019-v2.git
   $ cd YOUR_PATH/ISIC-2019-v2/
   $ mkdir models
``` 

Now download the dataset from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/isic-2019) and put images in [/data/images/](/data/images/). <br/>
Then, you can use any notebook in [/notebooks/](/notebooks/).

## Credits

You can find them in [/docs/credits.txt](/docs/credits.txt).
