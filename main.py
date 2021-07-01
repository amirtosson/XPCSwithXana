from Xana import Xana
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import pickle
import h5py

#f = h5py.File('./data/fw_3_SiO2_PPG_A_00006_data_000001.h5', 'r')
#print(f.attrs.get('entry'))

with h5py.File('./data/fw_3_SiO2_PPG_A_00006_data_000001.h5', "r") as f:
    # List all groups
    itemsS = list(f.items())
    print("Items: %s" % itemsS)
    print("Keys: %s" % f.keys())
    data = f.get('entry')
    dataarr = np.array(data.get('data/data'))

    print('s ', dataarr.shape)
    #a_group_key = list(f.keys())[0]

    # Get the data
    #data = list(f[a_group_key])
    #print(data)
"""
ana = Xana(fmtstr='p10_eiger_h5', detector='eiger500k', setupfile='./setupfiles/setup_SiO2_test.pkl')

ana.connect('data')
ana.meta

I, V = ana.get_series(0, method='average', first=10, last=1000)
print(ana.meta)
plt.subplots()
plt.imshow(I*ana.setup.mask, norm=LogNorm())
plt.show()
"""
