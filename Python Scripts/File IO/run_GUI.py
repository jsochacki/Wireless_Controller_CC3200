import sys
<<<<<<< HEAD
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit
import resource_rc
 
from GUI import Ui_Dialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    
    
    

print("\n\n\nHELLO WORLD")








file = Ui_Dialog.filename

print(file)



txt = open(file,"r")

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
=======
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Wifi Module'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
 
        self.show()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Wifi Module", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
 
    
 
   
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
>>>>>>> master
