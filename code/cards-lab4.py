# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:11:43 2020

@author: Jooda
"""

import random 
i = random.randint( 0, 51)
n = random.randint (9, 12)
print 'i=' + str( i )
if ( i <= 12 ):
   
    if (n%13) == 0:
        print ' 2 of diamond'
    if (n%13) == 1:
        print ' 3 of diamond'
    if (n%13) == 2:
        print ' 4 of diamond'
    if (n%13) == 3:
        print ' 5 of diamond'
    if (n%13) == 4:
        print ' 6 of diamond'
    if (n%13) == 5:
        print ' 7 of diamond'
    if (n%13) == 6:
        print ' 8 of diamond'
    if (n%13) == 9 :
        print 'Jack of diamond'
    if (n%13) == 10 :
        print 'Queen of diamond '
    if (n%13) == 11 :
        print 'King of diamond'
    if (n%13) == 12 :
        print 'Ace of diamond'
    
        
elif (i <= 25):
    
     if (n%13) == 0:
        print ' 2 of club'
     if (n%13) == 1:
        print ' 3 of club'
     if (n%13) == 2:
        print ' 4 of club'
     if (n%13) == 3:
        print ' 5 of club'
     if (n%13) == 4:
        print ' 6 of club'
     if (n%13) == 5:
        print ' 7 of club'
     if (n%13) == 6:
        print ' 8 of club'
     if (n%13) == 9 :
        print 'Jack of club'
     if (n%13) == 10 :
        print 'Queen of club'
     if (n%13) == 11 :
        print 'King of club'
     if (n%13) == 12 :
        print 'Ace of club'
 
   
   
elif (i <= 38): 
  
    if (n%13) == 0:
        print ' 2 of hearts'
    if (n%13) == 1:
        print ' 3 of hearts'
    if (n%13) == 2:
        print ' 4 of hearts'
    if (n%13) == 3:
        print ' 5 of hearts'
    if (n%13) == 4:
        print ' 6 of hearts'
    if (n%13) == 5:
        print ' 7 of hearts'
    if (n%13) == 6:
        print ' 8 of hearts'
    if (n%13) == 9 :
        print 'Jack of hearts'
    if (n%13) == 10 :
        print 'Queen of hearts'
    if (n%13) == 11 :
        print 'King of hearts'
    if (n%13) == 12 :
        print 'Ace of hearts'
     
else: 
   
     if (n%13) == 0:
        print ' 2 of Spades'
     if (n%13) == 1:
        print ' 3 of Spades'
     if (n%13) == 2:
        print ' 4 of Spades'
     if (n%13) == 3:
        print ' 5 of Spades'
     if (n%13) == 4:
        print ' 6 of Spades'
     if (n%13) == 5:
        print ' 7 of Spades'
     if (n%13) == 6:
        print ' 8 of Spades'
     if (n%13) == 9 :
        print 'Jack of Spades'
     if (n%13) == 10 :
        print 'Queen of Spades'
     if (n%13) == 11 :
        print 'King of Spades'
     if (n%13) == 12 :
       print 'Ace of Spades'
    