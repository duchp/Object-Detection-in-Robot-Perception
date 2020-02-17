# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:15:32 2019

@author: lenovo
"""

import os  
import random  

trainval_percent = 0.7  
train_percent = 0.8
minfilepath = '../VOCminImage'
totalfilepath = 'JPEGImages'
txtsavepath = 'ImageSets/Main'  
total_png = os.listdir(totalfilepath)  
min_png = os.listdir(minfilepath)  


ftest = open(txtsavepath+'/test_min.txt', 'w')  
 

for i in total_png:  
    #print(i)
    if i in min_png: 
        name = i[:-4]+'\n' 
        ftest.write(name)  
        print(name)

ftest .close()
print('Well Done')
