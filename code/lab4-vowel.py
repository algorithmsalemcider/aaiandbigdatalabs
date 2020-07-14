# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:16:24 2020

@author: Jooda
"""


myword = raw_input ('enter a word: ')
print ('you entered:' + myword)


i = myword.find ('A')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print 'This word Contains a vowel' 

    
i = myword.find ('I')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print 'This word Contains a vowel' 

    
i = myword.find ('E')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print 'This word Contains a vowel' 

    
    
i = myword.find ('U')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print 'This word Contains a vowel' 
 

i = myword.find ('O')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print 'This word Contains a vowel' 
 
else: 
    print 'This word doesnt contain a vowel'
