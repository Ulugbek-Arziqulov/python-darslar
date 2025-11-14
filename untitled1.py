# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:15:16 2025

@author: HI-TECH
"""

print("Mahsulotlar va narxlari ro'yxatini yaratamiz!")
e_bozor={}
while True:
    element=input("Sotib olmoqchi bo'lgan mahsulotlaringizni yozing: ")
    narx=int(input(f"{element.title()}ning narxini kiriting: "))
    e_bozor[element] = narx
    javob = input("Yana mahsulot olmoqchisiz?(ha/yo'q')")
    if javob!= 'ha':
        break
print("\n Sotib olgan mahsulotlaringiz ro'yxati: ")
for bozor, narx in e_bozor.items():
    print(f"{bozor.title()} - {narx}so'm")
umumiy = sum(e_bozor.values())
print(f"\nJami: {umumiy} so'm")