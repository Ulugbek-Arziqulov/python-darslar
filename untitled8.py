# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:22:58 2025

@author: HI-TECH
"""


# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz 
# # bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def qoldiqsiz_bolish (son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n}ga qoldiqsiz bo'linadi!")
        