import torch

from src.model.cnn import SkinClassifierNet

#-----------------------------------#
# Main class to managing the model. #
#-----------------------------------#

class Model:

    def __init__(self, device: str, model_path: str, model: SkinClassifierNet = None):
        self._device = device
        self._model = model
        self._model_path = model_path

        if model is not None:
            self._model.to(self._device)

    def save(self) -> None:
        torch.save(self._model.state_dict(), self._model_path)

    def load(self) -> None:
        self._model = SkinClassifierNet()
        self._model.load_state_dict(torch.load(self._model_path))
        self._model.to(self._device).eval()