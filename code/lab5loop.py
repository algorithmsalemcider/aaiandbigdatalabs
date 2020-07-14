# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:57:48 2020

@author: Jooda
"""


counter = 0 


myword = raw_input (' enter a word: ' )
print 'you entered: ' + myword 
L = len( myword )
print ' your word is" ' + str(L) + ' letters long.' 
for i in range (0 , L ): 
    print ' the ' + str(i) + 'the letter is ' +myword[i]
