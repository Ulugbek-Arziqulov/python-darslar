# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:28:32 2025

@author: HI-TECH
"""


# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def son (*sonlar):
    kopaytma=1
    for son in sonlar :
        kopaytma*=son
    return kopaytma
    
print(son(2,5,10,50))
