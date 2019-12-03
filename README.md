# Object-Detection-in-Robot-Perception(Hand Gesture Recognition)
## two-simple_ssd  
The hand gesture recognition plays an important role in the human-robot interaction (HRI) field. Most previous researches only investigate hand gesture recognition in a short distance, which is not able to be used for interaction with mobile robots like unmanned aerial vehicles in a longer distance. Therefore, we investigate the problem of long-range hand gesture recognition. We proposed a cascaded SSD structure for the long-range hand gesture recognition. Our model employed two SSDs for object detection. One is for the head-shoulder region detection and the other is for the hand gesture bounding box proposal and classification.

* Dataset  
Our data type is VOC type. So we have `.xml` files for label of images and `.png` for our images. All of .xml files have been saved in 'data/VOCdevkit/VOChand/Annotations' and all of .png files have been saved in 'data/VOCdevkit/VOChand/JPEGImages'. But some of our images don't have label of shoulder but only have label of hand. So, we should run `is_have_shoulder.py` to get a txt file whitch contain id of files that have shoulder's label. This file will be saved in  'data/VOCdevkit/VOChand/ImageSets/main'.  

  Then, We need to segment the data set to get the training set and the verification set. So run `generate_txt.py` to get these sets. All files it generate will be saved in 'data/VOCdevkit/VOChand/ImageSets/main'.
* Train
* Evaluation
* Test
