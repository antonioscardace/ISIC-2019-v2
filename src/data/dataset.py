from pandas import read_csv
from PIL import Image

from torch.utils.data import Dataset

#------------------------------------------------------#
# Defining a Dictionary to map text labels to numbers. #
# 0 = Benign Tumor;                                    #
# 1 = Malignant Tumor;                                 #
#------------------------------------------------------#

LABELS = {
    'NV': 0,
    'DF': 0,
    'MEL': 1,
    'BCC': 1,
    'SCC': 1
}

#-------------------------------------------------------------------#
# Custom Dataset class for our Skin Lesions Dataset (CSV + Images). #
# It implements the three required methods.                         #
#-------------------------------------------------------------------#

class SkinDataset(Dataset):
    
    def __init__(self, images_path, csv_path, transforms=None):
        self.examples = read_csv(csv_path, index_col=0)
        self.images_dir = images_path
        self.transforms = transforms
            
    def __len__(self) -> int:
        return len(self.examples)
    
    def __getitem__(self, index: int) -> tuple[Image.Image, int]:
        file_name = self.examples.iloc[index]['image']
        label = self.examples.iloc[index]['label']
        
        image = Image.open(self.images_dir + file_name + '.jpg')
        if image.mode != 'RGB': image = image.convert('RGB')
        if self.transforms is not None: image = self.transforms(image)

        return image, LABELS[label]