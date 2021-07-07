"""
@author:    Amir Tosson
@license:   GNU General Public License v3 or higher
@copyright: Universität Siegen, Deutschland
@email:     tosson@physik.uni-siegen.de
"""

"""
summary:    this model contains the functions required 
            for XPCS data manipulation  
name:       DataManipulation
date:       04-07-2021
"""

import numpy as np
import h5py

class DataManipulation():

    data_list = []

    def __init__(self):
        super().__init__

    def GetData(self, filename):
        with h5py.File(filename, "r") as f:
            data = f.get('entry/data/data')
            data_array = np.array(data)
        return data_array

    def SparseToCOO(self, arr):
        for i in range(arr.shape[0]):
            arr1 = arr[i, :, :]
            a = np.transpose(np.nonzero(arr1))
            b = np.transpose(arr1[[a[:, 0]], [a[:, 1]]])
            a = np.append(a, b, axis=1)
            self.data_list.append(a)