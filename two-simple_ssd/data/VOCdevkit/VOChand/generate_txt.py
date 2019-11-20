# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:15:32 2019

@author: lenovo
"""

import os  
import random  

trainval_percent = 0.7  
train_percent = 0.8
txtsavepath = 'ImageSets/Main'  
total_xml = open('ImageSets/Main/have_shoulder.txt').readlines()

num = len(total_xml)  
list = range(num)  
tv = int(num*trainval_percent)  
tr = int(tv*train_percent)  
trainval = random.sample(list,tv)  
train = random.sample(trainval,tr)  

ftrainval = open(txtsavepath+'/trainval.txt', 'w')  
ftest = open(txtsavepath+'/test.txt', 'w')  
ftrain = open(txtsavepath+'/train.txt', 'w')  
fval = open(txtsavepath+'/val.txt', 'w')  

for i in list:  
    
    name = total_xml[i]
    #print(name)
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  

ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
print('Well Done')
