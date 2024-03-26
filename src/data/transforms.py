from torchvision import transforms
from torch import Tensor

#--------------------------------------------------------------------------#
# This class is helpful for data augmentation and data loading.            #
# The Data Augmentation consists of adding a Random Rotation to the image. #         
# The Data Loading resizes and converts images to Tensor.                  #
#--------------------------------------------------------------------------#

class Transforms:

    @staticmethod
    def get_data_loading() -> Tensor:
        return transforms.Compose([
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
            transforms.Normalize([0.5949, 0.5940, 0.5966], [0.0807, 0.0809, 0.0811])
        ])

    @staticmethod
    def get_data_and_augment() -> Tensor:
        return transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(), 
            transforms.RandomRotation((10, 80)),
            transforms.AugMix(),
            Transforms.get_data_loading()
        ])