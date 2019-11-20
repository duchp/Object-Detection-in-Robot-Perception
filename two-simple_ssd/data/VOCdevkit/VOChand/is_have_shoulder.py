# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:15:32 2019

@author: lenovo
"""

import os  
import random
try:
    import xml.etree.cElementTree as ET 
except ImportError:
    import xml.etree.ElementTree as ET  

xmlfilepath = 'Annotations/'
txtsavepath = 'ImageSets/Main'  
total_xml = os.listdir(xmlfilepath)  

num = len(total_xml)  
list = range(num) 

ftest = open(txtsavepath+'/have_shoulder.txt', 'w')  
 
for i in list:  
    tree = ET.parse(xmlfilepath+total_xml[i])
    target = tree.getroot()
    tt = total_xml[i][:-4]+'\n' 
    for obj in target.iter('object'):
        name = obj.find('name').text.lower().strip()\
        
        if name == 'head_shoulder':
            print(target.find('filename').text)
            ftest.write(tt) 
            


ftest .close()
print('Well Done')
