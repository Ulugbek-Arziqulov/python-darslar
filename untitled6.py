# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:20:15 2025

@author: HI-TECH
"""

# juft_toq(3)
def solishtir(a,b):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya."""
    if a<b:
        print(f"Raqamlarni solishtirganimizda {a} dan {b} raqami katta ekanligi aniqlandi!")
    elif a>b:
        print(f"Raqamlarni solishtirganimizda {b} dan {a} raqami katta ekanligi aniqlandi!")
    else:
        print("Raqamlar teng!")
solishtir(10,20)