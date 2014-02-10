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


class Example(QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        centralWidget = QWidget()

        outerVBox = QVBoxLayout() #Include in widget

        topGroupBox = QGroupBox("File Management") #GroupBox with name
        middleGroupBox = QGroupBox("Action Buttons")
        bottomGroupBox = QGroupBox("Report Preview")

        topHBox = QHBoxLayout() #Include in outerVBox
        middleHBox = QHBoxLayout() #Include in outerVBox
        bottomHBox = QHBoxLayout() #Include in outerVBox

        topGroupBox.setLayout(topHBox) #Groupbox with Hbox layout
        middleGroupBox.setLayout(middleHBox) #Groupbox with Hbox layout
        bottomGroupBox.setLayout(bottomHBox) #Groupbox with Hbox layout

        outerVBox.addWidget(topGroupBox) #Add group boxes to a Vbox layout in central widget
        outerVBox.addWidget(middleGroupBox)
        outerVBox.addWidget(bottomGroupBox)

        #Create all buttons
        addButton = QPushButton("Add Files")
        validateButton = QPushButton("Validate Files")
        previewButton = QPushButton("Preview Report")
        generateButton = QPushButton("Generate Report")


        #Following the reddit help I created a File System Model and a TreeView Widget
        self.model = QFileSystemModel()
        self.root_index = self.model.setRootPath(QDir.currentPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.root_index)

        #List view to keep added items tha shall be used 
        self.list = QListView()

        #Table view to create a preview of the file that will be written
        self.table = QTableView()

        #Add tree and list to GUI
        topHBox.addWidget(self.tree)
        topHBox.addWidget(self.list)

        #Add table to GUI
        bottomHBox.addWidget(self.table)

        #Add buttons to GUI
        middleHBox.addWidget(addButton)
        middleHBox.addWidget(validateButton)
        middleHBox.addWidget(previewButton)
        middleHBox.addWidget(generateButton)
        
        #Set OuterVbox which contains everything as central widget for GUI main window
        centralWidget.setLayout(outerVBox)

        #add central widget to main window
        self.setCentralWidget(centralWidget)


        #Simple status bar
        self.statusBar().showMessage('Ready')
        
        #Add menus 
        self.appMenus() #Calls AppMenus function

        #Add function to retrieve file paths to "Add" Button
        addButton.clicked.connect(self.get_selected_paths)
        
        #Position and Geometry functions for app window
        self.resize(600, 480)
        self.center()        
        self.setWindowTitle('Basic Data File Generator')    
        self.show()
    
    def center(self):
        
        qr=self.frameGeometry()
        cp= QDesktopWidget().availableGeometry().center()
        
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def appMenus(self):
        
        exitAction = QAction('&Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        showMenu = menubar.addMenu('&Show')

        settingsMenu = menubar.addMenu('&Settings')

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_selected_paths(self):

        indexes = self.tree.selectedIndexes()
        print indexes
        print "\n"
        file_paths = [self.model.filePath(index) for index in indexes]
        file_name = [self.model.fileName(index) for index in indexes]
        print file_name, file_paths


def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
