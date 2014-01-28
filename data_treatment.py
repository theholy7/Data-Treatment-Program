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

        topGroupBox.setLayout(topHBox)
        middleGroupBox.setLayout(middleHBox)
        bottomGroupBox.setLayout(bottomHBox)

        outerVBox.addWidget(topGroupBox)
        outerVBox.addWidget(middleGroupBox)
        outerVBox.addWidget(bottomGroupBox)

        #topHBox.addStretch()
        middleHBox.addStretch(0)
        bottomHBox.addStretch(1)

        addButton = QPushButton("Add Files")
        addButton.clicked.connect(self.get_selected_paths)
        validateButton = QPushButton("Validate Files")
        previewButton = QPushButton("Preview Report")
        generateButton = QPushButton("Generate Report")

        model = QFileSystemModel()
        root_index = model.setRootPath(QDir.currentPath())

        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(root_index)

        self.listWidget = QListWidget(self)

        topHBox.addWidget(self.tree)
        topHBox.addWidget(self.listWidget)

        middleHBox.addWidget(addButton)
        middleHBox.addWidget(validateButton)
        middleHBox.addWidget(previewButton)
        middleHBox.addWidget(generateButton)
        

        centralWidget.setLayout(outerVBox)

        self.setCentralWidget(centralWidget)

        self.statusBar().showMessage('Ready')
        
        self.appMenus() #Calls AppMenus function
        
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
        file_paths = [self.model.filePath(index) for index in indexes]
        print file_paths


def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
