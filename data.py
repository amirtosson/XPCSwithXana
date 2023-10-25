#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:42:53 2023

@author: tosson
"""
import hdf5plugin
import h5py
import numpy as np
from timeit import default_timer


class Data():
    raw_data = []
    file_name = ""
    integrated_img = []
    
    def load_data_from_file(self):
        f =  h5py.File(self.file_name, "r")
        t1 = default_timer()
        self.raw_data = f.get('entry/data/data')[:,:,:]
        t2 = default_timer()
        self.integrated_img = np.sum(self.raw_data, axis = 0)