# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:38:59 2020

@author: Jooda
"""

import random 
i = random.randint( 0, 100)
print 'i=' + str( i )





if (i % 2 == 0 ):
    print ' i is even'

elif ( i > 0 ):
    print ' i is odd'

else: 
    print ' i is 0'