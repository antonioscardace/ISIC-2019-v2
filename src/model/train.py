import torch
from torch.utils.data import DataLoader

from tqdm import tqdm

from src.model.cnn import SkinClassifierNet
from src.model.model import Model

#-------------------------------------------------------------------#
# Subclass of the main Model.                                       #
# It is the light version of the class which just trains the model. #
#-------------------------------------------------------------------#

class ModelTraining(Model):

    def __init__(self, device: str, model_path: str, model: SkinClassifierNet):
        super().__init__(device, model, model_path)

    # It trains the model.
    # Being the light version of the class, it doesn't log losses and accuracies.

    def fit(self, criterion, optimizer, epochs: int, train_loader: DataLoader) -> None:
        
        for epoch in range(epochs):
            title = 'Epoch [%d]' % (epoch + 1)
            self._model.train()

            with torch.set_grad_enabled(True):
                for _, (images, labels) in tqdm(enumerate(train_loader), title, len(train_loader)):
                    
                    x = images.to(self._device)
                    y = labels.to(self._device)
                    outputs = self._model(x)

                    loss = criterion(outputs, y)
                    loss.backward()
                    optimizer.step()
                    optimizer.zero_grad()

            self.save()