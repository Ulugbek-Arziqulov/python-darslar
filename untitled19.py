# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 08:22:32 2025

@author: HI-TECH
"""

 # VAZIFA:
# 1. Foydalanuvchidan ismini so'rang (input)
# 2. Yoshini so'rang (input va int ga o'tkazing)
# 3. Sevimli rangini so'rang (input)
# 
# 4. Hammasini chiroyli formatda print qiling
#
# BONUS: Yoshidan foydalanib, 10 yildan keyin necha yosh bo'lishini hisoblang

ism=input("ismingizni kiriting: ")
yosh=int(input("yoshingizni kiriting: "))
rang=input("Sevimmi rangingizni kiriting: ")

print(f"Ismingiz: {ism.title()} \nYoshingiz: {yosh} \nSevimli rangingiz: {rang.title()}")

print(f"Siz 10 yildan kiyin {yosh+10} yoshda bo'lasiz.")
