#from Xana import Xana
import DataManipulation as _data
from timeit import default_timer
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import pickle

import concurrent.futures
from PyQt5 import QtWidgets
import mainwindow as _main_win
import sys

file_name = 'm029_eggwhite_70C_bd_00001-Low-Int/e4m/m029_eggwhite_70C_bd_00001_data_000001.h5'
d = []

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = _main_win.MainWindow()
    mw.show()
    sys.exit(app.exec_())
   # with h5py.File(file_name, "r") as f:
       # data = f.get('entry/data/data')
        #data_array = []
        #for i in data.iter_chunks():
            #data_array.append(data[i])
        
        #d = data_array
        #data = f.get('entry/data/data').id.get_num_chunks()
        #print(data)
        #data_array = np.array(data)
  #
  
  
    #data = _data.DataManipulation()
    #t1 = default_timer()
    #dataArr = data.GetData(file_name)
    #print(dataArr.shape)
    #plt.imshow(dataArr[1,:,:])
    #plt.show()
    #t2 = default_timer()
    #print("It took to extract data: ", t2 - t1)
    #t1 = default_timer()
    #data.SparseToCOO(dataArr)
    #t2 = default_timer()
    #print("It took to convert data: ", t2-t1)
    
    #v = [ dataArr[0:1000,:,:], dataArr[1001:2000,:,:],dataArr[2001:3000,:,:],dataArr[3001:4000,:,:],dataArr[4001:4999,:,:]]
    #t1 = default_timer()
    #with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        #executor.map(data.SparseToCOO, v)
    #t2 = default_timer()
    #print("It took to convert data (using threading): ", t2-t1)

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
