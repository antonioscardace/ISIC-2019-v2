import torch

from PIL import Image

from src.data.transforms import Transforms
from src.model.cnn import SkinClassifierNet
from src.model.model import Model

#--------------------------------------------------------#
# Subclass of the main Model.                            #
# Given an image, it predicts the label using the model. #
#--------------------------------------------------------#

class ModelPredict(Model):

    def __init__(self, device: str, model_path: str, model: SkinClassifierNet = None):
        super().__init__(device, model_path, model)

    # Given an image, it uses the model to predict the correct label. 
    # It is useful for the user's GUI.
    # It returns the correct label and its confidence.

    def predict(self, image: Image) -> tuple[int, float]:
        
        if image.mode != 'RGB': image = image.convert('RGB')
        transforms = Transforms.get_data_loading()
        image = transforms(image).unsqueeze(0)

        with torch.no_grad():
            x = image.to(self._device)
            output = self._model(x)

            scaled_output = torch.nn.Softmax(1)(output)
            confidence, pred_label = torch.max(scaled_output, 1)
            return pred_label.item(), confidence.item()