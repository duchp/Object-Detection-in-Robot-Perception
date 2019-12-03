# Object-Detection-in-Robot-Perception(Hand Gesture Recognition)
## two-simple_ssd  
The hand gesture recognition plays an important role in the human-robot interaction (HRI) field. Most previous researches only investigate hand gesture recognition in a short distance, which is not able to be used for interaction with mobile robots like unmanned aerial vehicles in a longer distance. Therefore, we investigate the problem of long-range hand gesture recognition. We proposed a cascaded SSD structure for the long-range hand gesture recognition. Our model employed two SSDs for object detection. One is for the head-shoulder region detection and the other is for the hand gesture bounding box proposal and classification.

* Dataset  
Our data type is VOC type. So we have `.xml` files for label of images and `.png` for our images. All of .xml files have been saved in 'data/VOCdevkit/VOChand/Annotations/' and all of .png files have been saved in 'data/VOCdevkit/VOChand/JPEGImages/'. But some of our images don't have label of shoulder but only have label of hand. So, we should run `is_have_shoulder.py` to get a txt file whitch contain id of files that have shoulder's label. This file will be saved in  'data/VOCdevkit/VOChand/ImageSets/main/'.  

  Then, We need to segment the data set to get the train set and the test set. So run `generate_txt.py` to get these sets. All files it generate will be saved in 'data/VOCdevkit/VOChand/ImageSets/main/'.  

* Train  
-`train_shoulder.py`: Training a SSD net on train set and saving its weights every 1000 epochs. Weights files all be saved in 'weights_shoulder/'   
  
  -`train_generate_shoulder_box.py`: Testing all train datasets by SSD net that be trained by `train_shoulder.py`. All predict results of shoulder label have been saved in 'shoulder_csv'. This `.csv` file will be used in `train_hand.py` , `test_trainset.py` and `eval_train_hand.py` for image crop.
  
  -`train_hand.py`:Using 'shoulder_csv/train_shoulder.csv' to cut image. Training these images after cutting by another SSD net and saving its weights every 1000 epochs. Weights files all be saved in 'weights_hand/'. 

* Test  
-`test_generate_shoulder_box.py`: Testing all test datasets by SSD net that be trained by `train_shoulder.py`. All predict results of shoulder label have been saved in 'shoulder_csv'. This `.csv` file will be used in `test_testset.py` and `eval_test_hand.py` for image crop.
  
  -`test_trainset.py`:Using 'shoulder_csv/train_shoulder.csv' and weights file from `train_hand.py` to test train set. Result is saved in 'test/trainset'.
  
  -`test_testset.py`:Using 'shoulder_csv/test_shoulder.csv' and weights file from `train_hand.py` to test test set. Result is saved in 'test/testset'.  
  
* Evaluation  
-`eval_train_hand.py`:Evaluating the performance of SSD net that be trained by `train_hand.py` on train set.  

  -`eval_train_shoulder.py`:Evaluating the performance of SSD net that be trained by `train_shoulder.py` on train set.  
 
  -`eval_test_hand.py`:Evaluating the performance of SSD net that be trained by `train_hand.py` on test set.  

  -`eval_test_shoulder.py`:Evaluating the performance of SSD net that be trained by `train_shoulder.py` on test set.

