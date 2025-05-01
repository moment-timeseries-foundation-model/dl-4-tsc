import torch
from torch.nn import Module


class ResNet(Module):
    def __init__(
        self, 
        output_directory,
        input_shape, 
        n_classes, 
        n_feature_maps, 
        verbose=False, 
        random_seed=42):
        """
        Initialize the ResNet model.

        Parameters
        ---------- 
        output_directory: str
            Directory to save the model and load the model from.

        input_shape: tuple
            Shape of the input time series (n_channels, n_time_steps).

        n_classes: int
            Number of classes for classification tasks.

        n_feature_maps: int
            Number of feature maps for the convolutional layers.

        verbose: bool
            If True, print out information during training and evaluation.

        random_seed: int
            Random seed for reproducibility.
        """
        pass

    def forward(self, x):
        """
        Forward pass of the model.

        Parameters
        ----------
        x: torch.Tensor
            Input tensor of shape (batch_size, n_channels, n_time_steps).
        
        Returns
        -------
        torch.Tensor
            Output tensor of shape (batch_size, n_classes).
        """
        batch_size = x.size(0)
        n_classes = 2
        return torch.zeros(batch_size, n_classes)


def train(
    model, 
    train_data, 
    val_data=None,
    batch_size=64,
    n_epochs=100,
    learning_rate=1e-3,
    verbose=False,
):
    """
    Function to train the ResNet model. 

    Parameters
    ----------
    model: ResNet
        The ResNet model to train.

    train_data: torch.utils.data.Dataset
        Training dataset, including both input time series and ground-truth class labels.

    val_data: torch.utils.data.Dataset
        Validation dataset (optional), including both input time series and 
        ground-truth class labels.

    batch_size: int
        Batch size for training.

    n_epochs: int
        Number of epochs to train the model.

    learning_rate: float
        Learning rate for the optimizer.

    verbose: bool
        If True, print out information during training.
    """
    pass


def predict(
    model, 
    test_data, 
):
    """
    Function to make predictions using the trained ResNet model.

    Parameters
    ----------
    model: ResNet
        The trained ResNet model.

    test_data: torch.utils.data.Dataset
        Test dataset, including both input time series and ground-truth class labels.
    """
    pass