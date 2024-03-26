import numpy
import torch

from torch.utils.data import DataLoader

from tqdm import tqdm

from src.model.cnn import SkinClassifierNet
from src.model.model import Model

#-----------------------------#
# Subclass of the main Model. #
# It just tests the model.    #
#-----------------------------#

class ModelTesting(Model):

    def __init__(self, device: str, model_path: str, model: SkinClassifierNet = None):
        super().__init__(device, model_path, model)

    # It tests the model. 
    # It returns the list of predicted labels and the list of correct labels.

    def test(self, test_loader: DataLoader) -> tuple[numpy.ndarray, numpy.ndarray]:
        
        predictions = []
        true_labels = []

        with torch.no_grad():
            for i, (images, labels) in tqdm(enumerate(test_loader), total=len(test_loader)):

                x = images.to(self._device)
                y = labels.to(self._device)
                outputs = self._model(x)

                y_pred = outputs.to('cpu').max(1)[1].numpy()
                y_true = y.to('cpu').numpy()

                predictions.extend(list(y_pred))
                true_labels.extend(list(y_true))

        return numpy.array(predictions), numpy.array(true_labels)