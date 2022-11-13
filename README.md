# WiderFaceDetection_Experiment
Integration Result of MMDetection_pkl and YOLOV5_txt on WIDERFACE Datasets

## Dataset Preparation

### Data DownLoad
Data DownLoad from [WIDERFACE Dataset](http://shuoyang1213.me/WIDERFACE/index.html)

Unzip the downloaded file and place it in the corresponding folder.

Empty file `Datasets` is in `Datasets.zip`, it is crucial, unzip it then do the following.

1. WIDER Face Training Images    ->   `./Datasets/WIDER_train/`
2. WIDER Face Validation Images  ->   `./Datasets/WIDER_val/`
3. Face annotations              ->   `./Datasets/wider_face_split/`


### DataFormat Transform
Thanks to [Data Transformation Guide from CSDN](https://blog.csdn.net/mary_0830/article/details/116589279)

Run the following program step by step:

1. `face2voc.py`: Convert the original format to VOC format.
2. `voc2coco`: Convert VOC format to COCO format.     # Used in [MMDetection](https://github.com/open-mmlab/mmdetection) tools
3. 'yolo_extract.py`: Extract filenames.
4. `xml2yolo.py`: Convert COCO format to YOLO format. # Used in [YOLOV5](https://github.com/ultralytics/yolov5) tools
