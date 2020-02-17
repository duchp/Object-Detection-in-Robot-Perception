import os
import cv2
from data import *
import pandas as pd

imgpath = VOC_ROOT+'VOChand/JPEGImages/'
path = 'test/testset/test_min.txt'
f = open(path, 'r') 
f_shoulder = pd.read_csv('shoulder_csv/test_shoulder_min.csv')
for i in range(len(f_shoulder['img_id'])):
    if f_shoulder['img_id'][i] == 'hand_type_9_5895':
        id_shoulder = i
        break
for lines in f:
    r = lines.strip('\n').split()
    if r[0] == 'hand_type_9_5895':
        img = cv2.imread(imgpath + r[0] + '.png')
        print(img.shape)
        cv2.rectangle(img,(int(float(r[1])) + f_shoulder['cood_xmin'][id_shoulder],int(float(r[2])) + f_shoulder['cood_ymin'][id_shoulder]),(int(float(r[3])) + f_shoulder['cood_xmin'][id_shoulder],int(float(r[4])) + f_shoulder['cood_ymin'][id_shoulder]),(255, 0, 0),2)
        cv2.rectangle(img,(int(float(r[7])) + f_shoulder['cood_xmin'][id_shoulder],int(float(r[8])) + f_shoulder['cood_ymin'][id_shoulder]),(int(float(r[9])) + f_shoulder['cood_xmin'][id_shoulder],int(float(r[10])) + f_shoulder['cood_ymin'][id_shoulder]),(0, 255, 0),2)
        cv2.imwrite('try_twossd.png', img)
