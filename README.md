# Object-Detection-in-Robot-Perception(Hand Gesture Recognition)
The hand gesture recognition plays an important role in the human-robot interaction (HRI) field. Most previous researches only investigate hand gesture recognition in a short distance, which is not able to be used for interaction with mobile robots like unmanned aerial vehicles in a longer distance.Therefore, we investigate the problem of long-range hand gesture recognition.

## Dataset

  Every model have 'data/' file. Let's introduce it.

  Our data type is VOC type. So we have '.xml' files for label of images and '.png' for our images. All of '.xml' files have been saved in './VOCdevkit/VOChand/Annotations/' and all of '.png' files have been saved in './VOCdevkit/VOChand/JPEGImages/'. In order to compare the influence of different distances on the model accuracy more conveniently, We save the farthest images in './VOCdevkit/VOCmaxImage/' and the nearest images in './VOCdevkit/VOCminImage/'.

  Then, We need to segment the data set to get the train set and the test set of different types of data. So run 'generate_txt.py', 'generate_max_txt.py' and 'generate_min_txt.py' to get these sets of all datasets, the farthest dataset and the nearest dataset. All files it generate will be saved in './VOCdevkit/VOChand/ImageSets/main/'.

  But in two-ssd model, we need informations of shoulder. Some of our images don't have label of shoulder but only have label of hand. So, we should run 'is_have_shoulder.py' to get a txt file which contain id of files that have shoulder's label. This file will be saved in './VOCdevkit/VOChand/ImageSets/main/'. Only the 'data/' file of two-ssd contain this part.

## ssd
A simple SSD model can be used as a base-model. We can see its results and then notice the distance play an important role of model accuracy.

* Train 

  -`train_all.py`: Training a SSD net on train set and saving its weights every 1000 epochs. Weights files all be saved in   'weights_all/'.The final weights file is named 'VOC.pth'. We upload it here and you can use it directly.

* Test and Evaluation 

  -`test.py`: Testing -eval_all.py: Evaluation of all datasets. 
  
  -`eval_max.py`: Evaluation of the farthest datasets. 
  
  -`eval_min.py`: Evaluation of the nearest datasets.

* Visualization 

  -`paint.py`:Plot the prediction box of ssd model and true box on the image.

## ssd-cbam
'Convolutional Block Attention Module (CBAM),a simple yet effective attention module for feed-forward convolutional neural networks.' Because CBAM takes the attention of space and channel into consideration, so it is added to the structure of SSD.The specific structure is shown in the figure below:
 ![image](https://github.com/duchp/Object-Detection-in-Robot-Perception/blob/master/ssd-cbam/ssd-cbam.JPG)

* Train 
  
  -`train_all.py`: Training a SSD net on train set and saving its weights every 1000 epochs. Weights files all be saved in 'weights_all/'.The final weights file is named 'VOC.pth'. We upload it here and you can use it directly.

* Test and Evaluation 
  
  -`test.py`: Testing 
  
  -`eval_all.py`: Evaluation of all datasets. 
  
  -`eval_max.py`: Evaluation of the farthest datasets. 
  
  -`eval_min.py`: Evaluation of the nearest datasets.

* Visualization 
  
  -`paint.py`:Plot the prediction box of ssd model and true box on the image.

## two-simple_ssd  
We proposed a cascaded SSD structure for the long-range hand gesture recognition. This model employed two SSDs for object detection. One is for the head-shoulder region detection and the other is for the hand gesture bounding box proposal and classification.

* Train  

  -`train_shoulder.py`: Training a SSD net on train set and saving its weights every 1000 epochs. Weights files all be saved in 'weights_shoulder/'   
  
  -`train_generate_shoulder_box.py`: Testing all train datasets by SSD net that be trained by `train_shoulder.py`. All predict results of shoulder label have been saved in 'shoulder_csv'. This `.csv` file will be used in `train_hand.py` , `test_trainset.py` and `eval_train_hand.py` for image crop.
  
  -`train_hand.py`:Using 'shoulder_csv/train_shoulder.csv' to cut image. Training these images after cutting by another SSD net and saving its weights every 1000 epochs. Weights files all be saved in 'weights_hand/'. 

* Test  
  
  -`test_generate_shoulder_box.py`: Testing all test datasets by SSD net that be trained by `train_shoulder.py`. All predict results of shoulder label have been saved in 'shoulder_csv'. This `.csv` file will be used in `test_testset.py` and `eval_test_hand.py` for image crop.
  
  -`test_max_generate_shoulder_box.py`: Testing test datasets in 'VOCmaxImage' by SSD net that be trained by train_shoulder.py. All predict results of shoulder label have been saved in 'shoulder_csv'. This .csv file will be used in eval_test_hand_max.py for image crop.
  
  -`test_min_generate_shoulder_box.py`: Testing test datasets in 'VOCminImage' by SSD net that be trained by train_shoulder.py. All predict results of shoulder label have been saved in 'shoulder_csv'. This .csv file will be used in eval_test_hand_min.py for image crop.
  
  -`test_trainset.py`:Using 'shoulder_csv/train_shoulder.csv' and weights file from `train_hand.py` to test train set. Result is saved in 'test/trainset'.
  
  -`test_testset.py`:Using 'shoulder_csv/test_shoulder.csv' and weights file from `train_hand.py` to test test set. Result is saved in 'test/testset'.  
  
* Evaluation   
  
  -`eval_test_hand.py`:Evaluating the performance of SSD net that be trained by `train_hand.py` on test set.  
  
  -`eval_test_hand_max.py`:Evaluating the performance of SSD net that be trained by train_hand.py on test set in 'VOCmaxImage'.
  
  -`eval_test_hand_min.py`:Evaluating the performance of SSD net that be trained by train_hand.py on test set in 'VOCminImage'.
  
* Visualization 
  
  -`paint.py`:Plot the prediction box of two-ssd model and true box on the image.
