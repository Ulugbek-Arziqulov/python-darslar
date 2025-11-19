# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 09:59:46 2025

@author: HI-TECH
"""
# 1.
# VAZIFA:
# 1. range() dan foydalanib 1 dan 10 gacha raqamlarni chop eting
# 2. Har bir raqamni alohida qatorda chiqaring


for raqam in range(1,11):
    print(raqam)


# 2.# VAZIFA:
# 1. Ismlar ro'yxatini yarating (3-5 ta ism)
# 2. For loop bilan har bir ismga "Salom, [ism]!" deb murojaat qiling
# 3. Har bir salom alohida qatorda chiqsin

ismlar=['ali', 'vali', 'hasan', 'husan', 'sardor']
for ism in ismlar:
    print(f"Salom {ism.title()}")
    
# 3. # VAZIFA:
# 1. 1 dan 20 gacha raqamlarni ko'rib chiqing (for loop)
# 2. Faqat JUFT raqamlarni chop eting


for juft_raqam in range(1,21):
    if juft_raqam %2==0:
        print(juft_raqam)









































