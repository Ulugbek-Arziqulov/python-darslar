# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 19:52:52 2025

@author: HI-TECH
"""

# VAZIFA:
# Kinoga kirish qoidalari:
# - Yosh 13 dan katta BO'LISHI kerak
# - VA (and) puli 50000 dan ko'p BO'LISHI kerak
# 
# 1. Yosh va pulni so'rang
# 2. Agar IKKALA shart ham to'g'ri bo'lsa → "Xush kelibsiz!"
# 3. Aks holda → "Kirishga ruxsat yo'q"

# LOGICAL OPERATORS:
# and - ikkala shart ham to'g'ri bo'lishi kerak
# or  - kamida bittasi to'g'ri bo'lsa kifoya


print("Kinoga kirish qoidalari!")
yosh=int(input("Yoshingizni kiriting: "))
pul=float(input("Pulingizni kiriting: ")) 
if yosh>=13 and pul>=50000:
    print("Xush kelibsiz!")
    
else:
    print("Kirishga ruxsat yo'q!")
    if yosh < 13:
        print("Sabab: Yoshingiz yetarli emas")
    if pul < 50000:
        print("Sabab: Pulingiz yetarli emas")







