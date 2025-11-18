# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 20:16:41 2025

@author: HI-TECH
"""

# VAZIFA:
# Oddiy login tizimi:
# 
# 1. Foydalanuvchi nomini so'rang
# 2. AGAR username "admin" bo'lsa:
#    - Parolni so'rang
#    - Agar parol "1234" bo'lsa → "Kirish muvaffaqiyatli!"
#    - Aks holda → "Parol xato!"
# 3. AKS HOLDA (username admin emas):
#    - "Foydalanuvchi topilmadi!"

# Bu NESTED IF (ichma-ich if)

login=input("Login: ")
if login=="admin":
    parol=(input("Parol: "))
    
    if parol=="1234":
        print("Kirish muvaffaqiyatli!")
    else:
        print("Kirish xato.")
    
else:
    print("Login adminniki emas!")
    print("Foydalanuvchi topilmadi.")


















