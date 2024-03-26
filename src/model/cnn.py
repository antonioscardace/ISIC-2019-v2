from torch import nn

#------------------------------------------------#
# Defines the Convolutional Neural Network (CNN) #
#------------------------------------------------#

class SkinClassifierNet(nn.Module):

    def __init__(self, input_channels: int = 3, out_classes: int = 2):
        super(SkinClassifierNet, self).__init__()
        
        self.feature_extractor = nn.Sequential(
            # Conv1
            nn.Conv2d(input_channels, 32, 3, padding='same'), # Input: 64 x 64 x 3. Output: 64 x 64 x 32 
            nn.MaxPool2d(2), # Input: 64 x 64 x 32. Output: 32 x 32 x 32
            nn.ReLU(),

            # Conv2
            nn.BatchNorm2d(32),
            nn.Conv2d(32, 64, 3, padding='same'), # Input: 32 x 32 x 32. Output: 32 x 32 x 64
            nn.MaxPool2d(2), # Input: 32 x 32 x 64. Output: 16 x 16 x 64
            nn.ReLU(),

            # Conv3
            nn.BatchNorm2d(64),
            nn.Conv2d(64, 128, 3, padding='same'), # Input: 16 x 16 x 64. Output: 16 x 16 x 128
            nn.MaxPool2d(3), # Input: 16 x 16 x 128. Output: 8 x 8 x 128
            nn.ReLU(),
            
            # Conv4
            nn.BatchNorm2d(128),
            nn.Conv2d(128, 256, 3, padding='same'), # Input: 8 x 8 x 128. Output: 8 x 8 x 256
            nn.MaxPool2d(5), # Input: 8 x 8 x 256. Output: 4 x 4 x 256
            nn.ReLU()
        )

        self.classifier = nn.Sequential(
            # FC5
            nn.Dropout(0.5),
            nn.BatchNorm1d(4096),
            nn.Linear(4096, 2048), 
            nn.ReLU(),
            
            # FC6
            nn.Dropout(0.5),
            nn.BatchNorm1d(2048),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            
            # FC7
            nn.Linear(1024, out_classes)
        )

    def forward(self, x):
        x = self.feature_extractor(x)
        x = self.classifier(x.view(x.shape[0], -1))
        return x