# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:19:06 2020

@author: trhislop
"""

# this script will rename multiple files in a folder
# replace obvious filepath, =dst "name", and "file type" 
import os
os.chdir(r'C:\Users\TRHislop\Desktop\Essential\Loop_Signature\Data_Files\June_2020_PVR')
i=1
for file in os.listdir() :
    src=file
    dst="June"+str(i)+".pvr"
    os.rename(src,dst)
    i+=1