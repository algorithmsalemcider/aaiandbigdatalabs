# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:58:45 2020

@author: Jooda
"""

numberx = raw_input('please enter a number:')
print ('You entered ' + numberx)
numbery = raw_input('please enter a another number:')
print ('You entered ' + numbery)
print ('The mathematical operators applied to ' + numberx + ' and ' + numbery + 'are')
x = int (numberx)
y= int (numbery)
print ('Is the first number less than the second?')
print (x < y)
print ('Is the first number more than the second?')
print (x > y)
print ('Is the first number equal to the second?')
print (x == y)
print ('Is the first number less than and equal to the second?')
print (x <= y)
print ('Is the first number greater than and equal to the second?')
print (x >= y)