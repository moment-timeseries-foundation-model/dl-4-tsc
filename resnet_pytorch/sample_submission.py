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
        Constructor to initialize the ResNet model.

        Parameters
        ---------- 
        output_directory: str
            Directory to save the model and load an existing model from.

        input_shape: tuple
            Shape of the input time series (n_channels, n_time_steps). 

        n_classes: int
            Number of classes for the classification tasks. 

        n_feature_maps: int
            Number of feature maps in the convolutional layers.

        verbose: bool
            If True, print details. 

        random_seed: int
            Random seed for reproducibility. 
        """
        pass

    def forward(self, x):
        """
        Defines the forward pass of the model.

        Parameters
        ----------
        x: torch.Tensor
            Input tensor of shape (batch_size, n_channels, n_time_steps). 
        
        Returns
        -------
        y: torch.Tensor
            Output tensor of shape (batch_size, n_classes). 
        """
        y = None
        return y


def train(
    model, 
    train_data, 
    val_data,
    batch_size,
    n_epochs,
    learning_rate,
    verbose,
):
    """
    This function defines the training loop for the ResNet model.

    Parameters
    ----------
    model: ResNet
        The ResNet model to train. 

    train_data: torch.utils.data.Dataset
        Training dataset; each sample is a tuple (input time series, ground-truth class label).

    val_data: torch.utils.data.Dataset
        Validation dataset (optional), in the same format as the training dataset. 

    batch_size: int
        Batch size for training.

    n_epochs: int
        Number of epochs to train the model. 

    learning_rate: float
        Learning rate for the optimizer.

    verbose: bool
        If True, print training and evaluation details.
        
    Returns
    -------
    model: ResNet
        The trained ResNet model.
    """
    model = None
    return model


def predict(
    model, 
    test_data, 
):
    """
    This function generates predictions on a given test dataset using a ResNet model.

    Parameters
    ----------
    model: ResNet
        The ResNet model used for making predictions. 

    test_data: torch.utils.data.Dataset
        Test dataset; each sample is a tuple (input time series, ground-truth class label).

    Returns
    -------
    y_true: numpy.ndarray
        Ground-truth labels for the test dataset, with shape (n_samples,).

    y_pred: numpy.ndarray
        Predicted scores for each class, with shape (n_samples, n_classes).
    """
    y_true, y_pred = None, None
    return y_true, y_pred