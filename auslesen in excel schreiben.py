# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:03:31 2020

@author: rebec
"""

import pandas as pd
import numpy as np
import os


pfad = 'C:\\Users\\rebec\\Desktop\\Test'
x = os.listdir(pfad)

excel = pd.DataFrame()
excel = pd.read_excel('C:\\Users\\rebec\\Desktop\\Test\\Quelle.xlsx', usecols="C:D", header=4)

for i in x:
    excel = excel.append(pd.read_excel('C:\\Users\\rebec\\Desktop\\Test\\Quelle.xlsx', usecols="C:D", header=4))
    

excel.to_excel('C:\\Users\\rebec\\Desktop\\Test\\Ziel.xlsx', index=False)


