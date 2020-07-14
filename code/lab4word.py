# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:54:12 2020

@author: Jooda
"""

myword = raw_input ('enter a word: ')
print ('you entered:' + myword)


i = myword.find ('A')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print 'This word Contains an a' 
else:
    print 'This word doesnt contain an a'    
    
i = myword.find ('I')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print "this word contains an I"
else :
    print 'This word doesnt contain an I'       
    
i = myword.find ('E')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print "this word contains an E"
else:
    print 'This word doesnt contain an E'   
    
    
i = myword.find ('U')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print "this word contains an U"
else:
    print 'This word doesnt contain an U'   

i = myword.find ('O')
print ('i=' + str(i))
if i == 0 or i == 1 or i==2 or i==3 or i==4 or i== 5 or i==6: 
    print "this word contains an o"
else:
    print 'This word doesnt contain an o'   




