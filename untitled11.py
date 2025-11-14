# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:25:31 2025

@author: HI-TECH
"""

                        
def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

print(kattasi(10,20,-5))
