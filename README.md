# YOLO-v5 wrapper
Wrap YOLO-V5 as a package for easier use in ROS2.

## Installation
`pip3 install -e .`

## Download pre-trained models
+ All available models are pre-defined in model_ids.yaml.
+ Installation for user-only will generate script in ~/.local, add the path into ~/.bashrc so that download script can be used.
+ Usage: `yolov5_download [predefined model's name]`, it will download .yaml and .pt file to data/ and models/ respectively.

## Difference from original version
+ Wrap it as a package for installation.
+ Add download.py for easier to download pre-trained models.
+ Add *detect_once.py* for real-time detection task, such as integration with `ROS`.