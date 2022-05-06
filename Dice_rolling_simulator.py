# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:54:19 2021

@author: kmate
"""

import random

def throw_dice():
    
    value = random.randint(1, 36)
    
    if value <= 6:
        print("""
               _________
              |         |
              |         |
              |    O    |
              |         |
              |_________|
              """)
    elif value > 6 and value <= 12:
        print("""
               _________
              |         |
              |         |
              |  O   O  |
              |         |
              |_________|
              """)
    elif value > 12 and value <= 18:
        print("""
               _________
              |         |
              |  O      |
              |    O    |
              |      O  |
              |_________|
              """)
              
    elif value > 18 and value <= 24:
        print("""
               _________
              |         |
              |  O   O  |
              |         |
              |  O   O  |
              |_________|
              """)
    
    elif value > 24 and value <= 30:
        print("""
               _________
              |         |
              |  O   O  |
              |    O    |
              |  O   O  |
              |_________|
              """)
    elif value > 30 and value <= 36:
        print("""
               _________
              |         |
              | O  O  O |
              |         |
              | O  O  O |
              |_________|
              """)
              
              
# %%
throw_dice()