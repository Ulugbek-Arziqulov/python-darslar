# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:23:30 2025

@author: HI-TECH
"""

 # qoldiqsiz_bolish(13)

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
def oraliq(min,max,qadam={}):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq(0,21,3))
print(oraliq(0,15,5))