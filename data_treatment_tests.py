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
        self.statusbar = self.statusBar().showMessage('Ready')

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
        self.menubar = QMenuBar(self)
        self.filemenu = self.menubar.addMenu("&File")
        self.settingsmenu = self.menubar.addMenu("&Settings")

        self.viewstatusbar = QAction("&Status Bar",self.settingsmenu)
        self.viewstatusbar.setCheckable(True)
        self.viewstatusbar.setChecked(True)
        self.viewstatusbar.setStatusTip("Displays Status Bar")
        self.viewstatusbar.toggled.connect(self.ViewStatusBar)

        self.settingsmenu.addAction(self.viewstatusbar)

    def ViewStatusBar(self):
        if self.viewstatusbar.isChecked() == True:
            self.statusbar = self.statusBar().showMessage("Status Bar is visible", 5000)
        else:
            self.setStatusBar(self.statusbar)


        
class CentralWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayouts()

    def setLayouts(self):
        self.outerVBox = QVBoxLayout() #Include in widget
        self.setLayout(self.outerVBox)

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

        #Create all buttons
        self.addButton = QPushButton("Add Files")
        self.addButton.clicked.connect(self.get_selected_paths)

        self.validateButton = QPushButton("Validate Files")
        self.previewButton = QPushButton("Preview Report")
        self.generateButton = QPushButton("Generate Report")

        #Add buttons to GUI
        self.middleHBox.addWidget(self.addButton)
        self.middleHBox.addWidget(self.validateButton)
        self.middleHBox.addWidget(self.previewButton)
        self.middleHBox.addWidget(self.generateButton)
        #self.middleHBox.addStretch()

        #Create File System and Tree
        self.model = QFileSystemModel()

        self.root_index = self.model.setRootPath(QDir.currentPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.root_index)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.setSelectionBehavior(QAbstractItemView.SelectRows)

        #List view to keep added items tha shall be used 
        self.list = QListView()

        #Table view to create a preview of the file that will be written
        self.table = QTableView()

        #Add tree and list to GUI
        self.topHBox.addWidget(self.tree)
        self.topHBox.addWidget(self.list)

        #Add table to GUI
        self.bottomHBox.addWidget(self.table)

    
    def get_selected_paths(self):
        #Get selected indexes (name, size, type, date modified)
        indexes = self.tree.selectedIndexes()
        #Create lists to store paths and names of files
        file_paths = []
        file_name = []

        #For each index, select name (which is column zero)
        for index in indexes:
            if index.column() == 0:
                #Store path of file and name
                file_paths.append(self.model.filePath(index))
                file_name.append(self.model.fileName(index))

        print file_name
        print "\n"
        print file_paths

def main():
    
    app = QApplication(sys.argv)
    appmainwin = AppMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()