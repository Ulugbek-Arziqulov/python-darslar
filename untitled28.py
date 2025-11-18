# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 12:06:54 2025

@author: HI-TECH
"""

# Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
while True:
    
    import re
    tel_raqam=input("Telefon raqam kiriting:")

    andoza=r"^\+998\d{9}$"

    if re.match(andoza,tel_raqam): 
        print("Raqam to'g'ri")
        break
    else:
        print("Raqam noto'g'ri")

