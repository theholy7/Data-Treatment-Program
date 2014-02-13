#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Data Treatment Program for INESC-MN

author: José Antunes 
last edited: 1st Jan 2013
"""

import sys
from PySide.QtGui import *
from PySide.QtCore import *

class AppMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Basic Data File Generator')

        self.initUI()

        self.resize(800, 640)
        self.geometry = self.frameGeometry()

        self.centerpoint = QDesktopWidget().availableGeometry().center()
            
        self.geometry.moveCenter(self.centerpoint)
        self.move(self.geometry.topLeft())

        self.show()

    def initUI(self):
        self.centralWidget = CentralWidget()
        self.createmenu()
        self.setCentralWidget(self.centralWidget)

    def createmenu(self):
        self.menubar = QMenuBar()
        self.menubar.addMenu("&File")
        
class CentralWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayouts()

    def setLayouts(self):
        self.outerVBox = QVBoxLayout() #Include in widget

        self.topGroupBox = QGroupBox("File Management") #GroupBox with name
        self.middleGroupBox = QGroupBox("Action Buttons")
        self.bottomGroupBox = QGroupBox("Report Preview")

        self.topHBox = QHBoxLayout() #Include in outerVBox
        self.middleHBox = QHBoxLayout() #Include in outerVBox
        self.bottomHBox = QHBoxLayout() #Include in outerVBox

        self.topGroupBox.setLayout(self.topHBox) #Groupbox with Hbox layout
        self.middleGroupBox.setLayout(self.middleHBox) #Groupbox with Hbox layout
        self.bottomGroupBox.setLayout(self.bottomHBox) #Groupbox with Hbox layout

        self.outerVBox.addWidget(self.topGroupBox) #Add group boxes to a Vbox layout in central widget
        self.outerVBox.addWidget(self.middleGroupBox)
        self.outerVBox.addWidget(self.bottomGroupBox)

        self.setLayout(self.outerVBox)

def main():
    
    app = QApplication(sys.argv)
    appmainwin = AppMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()