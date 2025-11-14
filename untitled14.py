# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:29:01 2025

@author: HI-TECH
"""

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar1=list(filter(lambda meva:(meva.startswith('o') and meva.endswith('a')), mevalar))
print(mevalar1)