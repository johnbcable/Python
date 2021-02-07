#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:42:46 2021

@author: a03pl
"""

x = int(input('Enter an integer (x): '))
y = int(input('Enter an integer (y): '))
z = int(input('Enter an integer (z): '))
if x<y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:          
    print('z is least')
print('Done with conditional3')
    