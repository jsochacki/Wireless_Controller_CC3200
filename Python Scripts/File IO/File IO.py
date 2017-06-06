# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:12:02 2017

@author: medgar
"""



filename = input("Please enter the filename plus extension:\n")

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

