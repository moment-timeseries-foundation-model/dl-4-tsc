# ResNet Implementation in TensorFlow

This branch prepares a ResNet implementation in TensorFlow from the original `dl-4-tsc` implementation, used as input and sample submission files for the `resnet-tensorflow-to-pytorch` challenge in TimeSeries Gym.

## Modifications made to the `dl-4-tsc` repo:

1. A folder named `resnet_tensorflow/` is created  
2. `classifiers/resnet.py` and `utils/utils.py` are copied to `resnet_tensorflow/`
3. A folder named `resnet_pytorch/` is created, and a new file named `sample_solution.py` is added under this folder.  

### Changes to `resnet_tensorflow/resnet.py`:
- Removed `.replace()` in `self.output_directory` in `__init__()`
- Added `n_feature_maps`, `batch_size`, and `nb_epochs` as input parameters
- Used `y_val` to compute `y_true` in `fit()`
- Removed unused variables: `x_train`, `y_train`, and `y_test` from `predict()`

### Changes to `resnet_tensorflow/utils.py`:
- Retained only `calculate_metrics`, `save_test_duration`, and `save_logs`
- Removed losses plotting from `save_logs`

### Changes to `resnet_pytorch/sample_solution.py`:
- Provided a skeleton implementation of ResNet in PyTorch, including the required class and functions with accompanying documentation.