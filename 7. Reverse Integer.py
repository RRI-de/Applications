# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:36:25 2020

@author: rebec

Given a 32-bit signed integer, reverse digits of an integer
"""
import pandas as pd

a = -48

if a < 0:
    b = str(a * -1)
else:
    b = str(a)  

z = []

y = ''

for i in enumerate(b):
    z.append(i)
print(z)

z.reverse()
length = len(z)
for i in range(length):
    y = y +(z[i][1])
if a < 0:
    print(int(y) * -1)
else:
     print(int(y))
     
     
# Alternative Lösung 

c = b[::-1]

int(c)



