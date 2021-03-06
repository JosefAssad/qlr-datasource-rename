#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
import re

#Angiv rodfolderen for qlr-filerne
ROOTDIR = '/Volumes/DISK_IMG/qlr_dims'

#Angiv den nye host
NEWHOST = 'anders'

#Looper over filer i mapper/undermapper
for subdir, dirs, files in os.walk(ROOTDIR):
    for f in files:
        filepath = os.path.join(subdir, f)
        #For hver fil skrives "Editing: filename"
        print('Editing: ' + filepath)
        tree = ET.parse(filepath)
        root = tree.getroot()
        for ds in root.findall('maplayers/maplayer/datasource'):
            ds.text = re.sub(r'host=[^\s]*', 'host=%s' % NEWHOST, ds.text)
        tree.write(filepath)
