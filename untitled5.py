# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:19:10 2025

@author: HI-TECH
"""

def kvadrat_kub (son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi."""
    print(f"{son} ning kvadrati {son**2} ga \n {son} ning kubi {son**3} ga teng!")
kvadrat_kub(5)


def juft_toq (son):
    """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya."""   
    if son%2:
        print(f"{son} toq son!")
    else:
        print(f"{son} juft son!")