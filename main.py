from Xana import Xana
import numpy as np
import DataManipulation as _data
from timeit import default_timer
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import pickle
import h5py
import concurrent.futures


def main():
    data = _data.DataManipulation()
    t1 = default_timer()
    dataArr = data.GetData('fw_3_SiO2_PPG_A_00006_data_000001.h5')
    t2 = default_timer()
    print("It took to extract data: ", t2 - t1)
    t1 = default_timer()
    data.SparseToCOO(dataArr)
    t2 = default_timer()
    print("It took to convert data: ", t2-t1)
    
    v = [ dataArr[0:1000,:,:], dataArr[1001:2000,:,:],dataArr[2001:3000,:,:],dataArr[3001:4000,:,:],dataArr[4001:4999,:,:]]
    t1 = default_timer()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(data.SparseToCOO, v)
    t2 = default_timer()
    print("It took to convert data (using threading): ", t2-t1)

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
