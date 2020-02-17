# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:15:32 2019

@author: lenovo
"""

import os  
import random  

trainval_percent = 0.7  
xmlfilepath = 'Annotations/'
txtsavepath = 'ImageSets/Main'  
total_xml = os.listdir(xmlfilepath)  

num = len(total_xml)  
list = range(num)  
tv = int(num*trainval_percent)  
random.seed(0)
trainval = random.sample(list,tv)  


ftrainval = open(txtsavepath+'/trainval.txt', 'w')  
ftest = open(txtsavepath+'/test.txt', 'w')  


for i in list:  
    name = total_xml[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
    else:  
        ftest.write(name)  

ftrainval.close()  
ftest .close()
print('Well Done')
