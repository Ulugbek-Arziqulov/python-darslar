# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 15:33:57 2025

@author: HI-TECH
"""

import random
son=random.randint(1,50)
print(son)

urinish=0
print("="*40)
print("Topish o'yini - 1 dan 50 gacha")
print("="*40)

while True:
    taxmin=int(input("taxminiy son kiriting: "))
    urinish=urinish+1
    
    if taxmin < son:
        print("Kattaroq son kiriting!")
    elif taxmin > son:
        print("Kichikroq son kiriting!")
    else:
        print("="*40)
        print(f" To'g'ri! Son {son} edi!")
        print(f"Siz {urinish} marta urinib topdingiz!")
        print("="*40)
        break
    
    
    