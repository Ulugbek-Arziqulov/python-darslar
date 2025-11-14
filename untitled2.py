# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:16:35 2025

@author: HI-TECH
"""

mahsulotlar = ['suv','anjir','uzum','non']
e_bozor = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while mahsulotlar:
    buyurtma = mahsulotlar.pop()
    if buyurtma in e_bozor.keys():
        narh = e_bozor[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")