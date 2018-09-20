#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:20:30 2018

@author: emmaelisabethkiis
"""

wd = '/Users/emmaelisabethkiis/Desktop/Pyhton/Data/'

import os, io

os.chdir(wd)                        # change directory to wd
os.listdir(wd)                      # shows list of content in my wd

datapath = 'Artikler'               # path to data in my working directory

os.listdir(datapath)                # list of files in my data
filenames = os.listdir(datapath)    # create variable with list of all files


myfiles = []                        # create list without macbook's .DS_Store file
for filename in filenames:
    if filename != '.DS_Store':
        myfiles.append(filename)

len(myfiles)                        # 124 artikler i alt




