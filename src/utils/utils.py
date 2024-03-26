import torch

from torch.utils.data import DataLoader
from pandas import DataFrame
from typing import List
    
#-------------------------------------------------------------------------#
# For each metadata sample, I add the label field.                        #
# This field is taken from the corresponding row of the ground truth CSV. #
#-------------------------------------------------------------------------#

def merge_metadata_label(metadata: DataFrame, labels: DataFrame) -> DataFrame:

    for _, diagnosis in labels.iterrows():
        for label in labels:
            if diagnosis[label] == 1.0:
                metadata.loc[metadata['image'] == diagnosis['image'], 'label'] = label

    return metadata

#-----------------------------------------------------------------------#
# Calculates mean and standard deviation for each image of the dataset. #
# It is useful to normalize the dataset and train the model.            #
#-----------------------------------------------------------------------#

def get_dataset_mean_std(data_loader: DataLoader) -> tuple[List[float], List[float]]:

    mean = [0.0, 0.0, 0.0]
    std = [0.0, 0.0, 0.0]
    num_images = len(data_loader)

    for image, label in data_loader:
        for i in range(3):
            mean[i] += torch.mean(image[0][0][i]).item() 
            std[i] += torch.std(image[0][0][i]).item()

    return [m / num_images for m in mean], [s / num_images for s in std]