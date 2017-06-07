import sys
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