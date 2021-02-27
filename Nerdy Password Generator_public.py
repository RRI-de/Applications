# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:57:53 2021

@author: rebecca_ri Nerdy Password Generator

- A password needs to be of minimum 10 character's length

- A password needs upper and lower case letters, numbers and special characters

- The password must not consist of easily guessed words like username, birth date etc.

- Simple words should not be included (sun, today, tomorrow, etc.)
"""

# %% Library import

import pandas as pd
import random

# %% Data import
# Data Source: kaggle.com
hp = pd.read_csv('C:\....csv', engine='python', sep=';', header=0)  # Harry Potter
hdr = pd.read_csv('C:\....csv', engine='python', sep=',', header=0)  # Lord of the Rings
sw = pd.read_csv('C:\\....csv', engine='python', sep=',', header=0)  # Star Wars

# %% Creation of selection list
selection_list = []
selection_list.append(hp['Name'])
selection_list.append(hdr['name'])
selection_list.append(sw['name'])

# %% Generator
# Remove spaces between first and last name
mod_sel_list = []
for group in selection_list:
    for row in group:
        if " " in row:
            row = row.replace(" ", "_")
            mod_sel_list.append(row)
# Remove names < 10 characters
for i in mod_sel_list:
    if len(i) < 10:
        mod_sel_list.remove(i)
# Create random number < 100
number_add_on = random.randint(0,100)
# Create list for special characters according to ASCII code
special_add_on = []
for i in range(32, 48, 1):
    special_add_on.append(chr(i))
# Combine results to password
password = mod_sel_list[random.randint(0,529)] + str(number_add_on) + special_add_on[(random.randint(0,15))]
# Print password
print('Your password has been genereated. Please use ' + password + ' for the next 180 days.')


