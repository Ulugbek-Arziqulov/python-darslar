# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:37:57 2025

@author: HI-TECH
"""

#1. VAZIFA:
# 1. son degan o'zgaruvchiga 1 qo'ying
# 2. While loop bilan son 10 ga yetguncha sanang
# 3. Har bir raqamni print qiling
# 4. Har safar son ga 1 qo'shing

son=1
while son<=9:
    print(son)
    son=son+1    


# 2. # VAZIFA:
    
# 1. to'g'ri_parol = "python" deb o'rnating
# 2. While True: bilan cheksiz loop yarating
# 3. Foydalanuvchidan parol so'rang
# 4. Agar to'g'ri bo'lsa → "To'g'ri!" va break
# 5. Aks holda → "Xato, qayta urinib ko'ring"

parol="python"
while True:
        foydalanuvchi=input("Parol kiriting: ")
        if foydalanuvchi==parol:
            print("To'gri!")
            break
        else:
            print("Xato, qayta o'rinib ko'ring!")





























