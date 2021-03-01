# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:06:41 2021

@author: rebec
"""
import numpy as np

def code_guess():
## code_input
   
    code_complexity = list(range(0,3)) 
    numbers = []
    for n in code_complexity:
        x = np.random.randint(1,21)
        if x in numbers:
            x = np.random.randint(1,21)
            numbers.append(x)
        else:
            numbers.append(x)
   
    print(numbers)

    user_input = []
    guess = [False, False, False]
    
    while guess != [True, True, True]:
        for m in code_complexity:
            if guess[m] != True:
                user_inputs = int(input(f'Please enter number {m+1}:'))
                user_input.append(user_inputs)
             
## code_check
    
        for i in user_input:
            if i in numbers:
                print(f'Number {i} is correct!')
                guess[numbers.index(i)] = True
            else:
                print(f'Number {i} is incorrect, please try again!')
        

code_guess()
    
    
            
    


