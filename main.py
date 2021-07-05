from Xana import Xana
import numpy as np
import DataManipulation as _data
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import pickle
import h5py
import concurrent.futures


def main():
    data = _data.DataManipulation()
    data.SparseToCOO(data.GetData('fw_3_SiO2_PPG_A_00006_data_000001.h5'))
    
    print(data.data_list)
    
    # v = [ data[0:1000,:,:], data[1001:2000,:,:],data[2001:3000,:,:],data[3001:4000,:,:],data[4001:4999,:,:]]
    # with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    # executor.map(SparseToCOO, v)

    # a_group_key = list(f.keys())[0]

    # Get the data
    # data = list(f[a_group_key])
    # print(data)


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

if __name__ == '__main__':
    main()
