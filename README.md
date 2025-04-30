# ResNet Implementation in TensorFlow

This branch prepares a ResNet implementation in TensorFlow from the original `dl-4-tsc` implementation, used as input for the `resnet-tensorflow-to-pytorch` challenge in TimeSeries Gym.

## Modifications made to the `dl-4-tsc` repo:

1. A folder named `resnet_tensorflow/` is created  
2. `classifiers/resnet.py` and `utils/utils.py` are copied to `resnet_tensorflow/`

### Changes to `resnet_tensorflow/resnet.py`:
- Removed `.replace()` in `self.output_directory` in `__init__()`
- Added `n_feature_maps`, `batch_size`, and `nb_epochs` as input parameters
- Used `y_val` to compute `y_true` in `fit()`
- Removed unused variables: `x_train`, `y_train`, and `y_test` from `predict()`

### Changes to `resnet_tensorflow/utils.py`:
- Retained only `calculate_metrics`, `save_test_duration`, and `save_logs`
- Removed losses plotting from `save_logs`

The modified files under `resnet_tensorflow/` serve as the input for the `resnet-tensorflow-to-pytorch` challenge in TimeSeries Gym.