'''
 Author: Mason Edgar
 Supervisor: John Sochacki 
 Graphical User Interface (GUI) for the Wifi Programmable Frequency Synthesizer
 
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit
import resource_rc 


filename = ''
flag = 0

class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 236)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog{\n""background-color: rgb(255, 255, 255);\n""}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        self.BrowseButton = QtWidgets.QPushButton(Dialog)
        self.BrowseButton.setObjectName("BrowseButton")
        self.gridLayout.addWidget(self.BrowseButton, 4, 1, 1, 1)
        self.OKbuttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.OKbuttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.OKbuttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OKbuttonBox.setObjectName("OKbuttonBox")
        self.gridLayout.addWidget(self.OKbuttonBox, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        #################### BUTTON ACTION #########################################################
        self.BrowseButton.clicked.connect(self.BrowseFunction) 
        QLineEdit.setPlaceholderText(self.lineEdit, "Search for the file using the 'Browse' button")
        QLineEdit.setReadOnly (self.lineEdit, True)
        ############################################################################################
        self.retranslateUi(Dialog)
        self.OKbuttonBox.accepted.connect(Dialog.accept)
        self.OKbuttonBox.accepted.connect(self.OKbuttonAccepted)
        self.OKbuttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wifi Module"))
        self.BrowseButton.setText(_translate("Dialog", "Browse"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/img/0ed03b37.png\"/></p><p><span style=\" font-weight:600;\">Wifi Programmable Frequency Synthesizer Module</span></p></body></html>"))
               
    def BrowseFunction(self):
        self.buffer, _ = QFileDialog.getOpenFileName(None,"Open File","","Text Files (*.txt);;All Files (*)", None)
        QLineEdit.setText(self.lineEdit, self.buffer)
        
    def OKbuttonAccepted(self):
        global filename
        global flag
        flag = 1
        filename = self.buffer
        
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.aboutToQuit.connect(app.deleteLater)
    

   
while(flag == 0):
    QtCore.QCoreApplication.processEvents() 
    
    
txt = open(filename,"r")

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
    
    
    
    
    
    
    
    