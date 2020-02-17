import os
import cv2
from data import *
import pandas as pd

imgpath = VOC_ROOT+'VOChand/JPEGImages/'
path = 'test/test.txt'
f = open(path, 'r') 
for lines in f:
    r = lines.strip('\n').split()
    if r[0] == 'hand_type_9_5895':
        img = cv2.imread(imgpath + r[0] + '.png')
        print(img.shape)
        print(int(float(r[1])))
        cv2.rectangle(img,(int(float(r[1])),int(float(r[2]))),(int(float(r[3])),int(float(r[4]))),(255, 0, 0),2)
        cv2.rectangle(img,(int(float(r[7])),int(float(r[8]))),(int(float(r[9])),int(float(r[10]))),(0, 255, 0),2)
        cv2.imwrite('try_cbam.png', img)
#i = 12
#img = cv2.imread(imgpath+f['img_id'][i]+'.png')
#print(img.shape)
#cv2.rectangle(img,(f['cood_xmin'][i],f['cood_ymin'][i]),(f['cood_xmax'][i],f['cood_ymax'][i]),(255, 0, 0),2)
#cv2.imwrite('try.png', img)