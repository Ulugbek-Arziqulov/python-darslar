# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:26:32 2025

@author: HI-TECH
"""

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta
#  harfga o'zgatiruvchi funksiya yozing.

def katta_harf(matnlar):
    matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar [i] = matnlar [i].title()
    return matnlar 

ismlar=['ali', 'vali','hasan']
yangi_ismlar=katta_harf(ismlar)
katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
