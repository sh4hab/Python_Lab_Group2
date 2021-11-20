# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 00:04:32 2021

@author: MohammadAmin
"""

#x= open('python_lab.txt','x')
x= open('python_lab.txt','w')
x.write('masz')
x.close()#necessary

f=open('python_lab.txt','r')
print(f.read())
f.close()#necessary

with open('python_lab.txt','a') as file:#noneed to close
        file.write('\n97101789')
with open('python_lab.txt') as file:
     a=file.read()
     file.seek(0)
     b=file.readlines()
     print('output of readline: '+str(b)) # saving each line into a list
     print('whole text:\n'+a)