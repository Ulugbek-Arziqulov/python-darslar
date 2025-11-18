# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 20:45:44 2025

@author: HI-TECH
"""

# VAZIFA:
# Harorat bo'yicha kiyim maslahatini bering:
#
# - 30 va yuqori → "Juda issiq! Yengil kiyim kiying"
# - 20-29 → "Iliq havo, qulay kiyining"
# - 10-19 → "Sovuqroq, kurtka kerak bo'lishi mumkin"
# - 0-9 → "Sovuq! Iliq kiyining"
# - 0 dan past → "Juda sovuq! Qalın kiyim kiying"
#
# BONUS: 
# - Yomg'ir yog'ayotganini ham so'rang (ha/yo'q)
# - Agar yomg'ir bo'lsa → "Soyabon olib keting!" qo'shing

print("Harorat bo'yicha maslahatlar..")
harorat=float(input("Havo haroratini kiriting: "))
   
if harorat>=30:
    print("Juda issiq yengil kiyim kiyib oling.")
    
elif harorat>=20:
    print("Iliq havo, qulay kiyining.")
    
elif harorat>=10:
    print("Sovuqroq, kurtka kerak bo'lishi mumkin.")
    
else:
    print("Juda sovuq! Iliq kiyining.")
    
yomgir=input("Yomg'ir yog'yabdimi? ha/yo'q: ")
if yomgir=="ha":
    print("Soyabon olib keting!")

















