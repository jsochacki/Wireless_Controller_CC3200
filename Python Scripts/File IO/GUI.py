# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 194)
        self.OKbuttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.OKbuttonBox.setGeometry(QtCore.QRect(40, 160, 341, 32))
        self.OKbuttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.OKbuttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OKbuttonBox.setObjectName("OKbuttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.BrowseButton = QtWidgets.QPushButton(Dialog)
        self.BrowseButton.setGeometry(QtCore.QRect(290, 80, 93, 28))
        self.BrowseButton.setObjectName("BrowseButton")
        #################### BUTTON ACTION #########################
        self.BrowseButton.clicked.connect(self.BrowseFunction) 
        self.filename = ''
        ############################################################
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.OKbuttonBox.accepted.connect(Dialog.accept)
        self.OKbuttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wifi Module"))
        self.BrowseButton.setText(_translate("Dialog", "Browse"))
        self.label.setText(_translate("Dialog", "Wifi Programmable Frequency Synthesizer Module"))
               
        
    def BrowseFunction(self):
        self.filename, _ = QFileDialog.getOpenFileName(None,"Open File","","Text Files (*.txt);;All Files (*)", None)
        

    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
 
    
    
    print("\n")
    txt = open(self.filename,"r")
    values = txt.readlines()

    new_values = [None] * 13      
    numbers = [None] * 13
    
    for i in range(len(values)):
        
        for index, char in enumerate(values[i]):
    
            if i < 12:
                if char == '0' and index > 2:
                    
                    new_values[i] = values[i][index:-1]
                
                    break
            else: 
                if char == '0' and index > 2:
                
                    new_values[i] = values[i][index:]
                
                    break
            
    for i in range(len(new_values)):
        
        numbers[i] = int(new_values[i], 16)
        
        
    for i in range(len(numbers)):
        print(hex(numbers[i]))