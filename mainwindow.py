#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:32:53 2023

@author: tosson
"""

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QSpinBox, QLabel, QPushButton, QErrorMessage, QMessageBox

from PyQt5 import uic

from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt
import numpy as np

import data as _data


if int(QtCore.qVersion()[0]) > 4:
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
    


class Canvas(FigureCanvas):
    ax = any
    fig = any
    def __init__(self, parent):
        w = int(parent.frameGeometry().width()/80)
        h = int(parent.frameGeometry().height()/80)
        self.fig, self.ax = plt.subplots(figsize= (w,h))
        super().__init__(self.fig)
        self.setParent(parent)

    
    
class MainWindow(QtWidgets.QMainWindow):
    data_object = _data.Data()

    def __init__(self):
        super().__init__()
        #load ui
        uic.loadUi("mainwindow.ui", self)
        
        #========== UI components intialization ========================
        self.openFileBtn.clicked.connect(self.upload_file)
        self.openFileBtn.setIcon(QtGui.QIcon('resources/icons/load.png'))
        self.openFileBtn.setIconSize(QtCore.QSize(50,50))
        self.loginBtn.setIcon(QtGui.QIcon('resources/icons/connect.png'))
        self.loginBtn.setIconSize(QtCore.QSize(50,50))

        #================ Ploting widget intialization ===================        
        self.chart_2d  = Canvas(self.mainPlotWidget)
        #toolbar_2d = NavigationToolbar(self.chart_2d, self.toolBarWidget)
        #layout = QtWidgets.QVBoxLayout()
        #layout.addWidget(toolbar_2d)
        self.chart_2d.ax.axis(False)


    def upload_file(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Open Data File')
        dialog.setNameFilter('Data files (*.h5)')
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.file_full_path = str(dialog.selectedFiles()[0])
        choice = QMessageBox.question(None, "Information","Load file: "+ self.file_full_path, QMessageBox.Ok, QMessageBox.Cancel)
        print(choice)
        if not choice  == 1024:
            return
        #self.fileNameText.setText(self.file_full_path)
        self.data_object.file_name = self.file_full_path
        self.data_object.load_data_from_file()
        self.chart_2d.ax.clear()
        self.chart_2d.ax.imshow(self.data_object.integrated_img, interpolation='none')
        self.chart_2d.ax.axis(False)
        self.chart_2d.fig.canvas.draw()
        plt.imshow(self.data_object.integrated_img)
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        