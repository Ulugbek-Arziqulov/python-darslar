# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:25:07 2025

@author: HI-TECH
"""

def foydalanuvchi_malumot(ism, familiya, tyil, tjoy, email='', tel=None):
    """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili
         va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya"""
    foydalanuvchi={'ism':ism,
                   'familiya':familiya,
                   'tyil':tyil,
                   'yoshi':2025-tyil,
                   'tjoy':tjoy,
                   'email':email,
                   'tel':tel}
    return foydalanuvchi
print("Foydalanuvchi haqida ma'lumot kiriting!")
while True:
    foydalanuvchilar=[]
    ism=input('Ismi:')
    familiya=input('Familiyasi:')
    tyil=int(input('Tug\'ilgan yili:'))
    tjoy=input('Tug\'ilgan joyi:')
    email=input("Email:")
    tel=input('Telefon raqami:')
    foydalanuvchilar.append(foydalanuvchi_malumot(ism, familiya, tyil, tjoy, email, tel))
    javob=input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break
print("foydalanuvchilar:")
for foydalanuvchi in foydalanuvchilar:
    print(f"{foydalanuvchi['ism'].title()}, {foydalanuvchi['familiya'].title()},"
          f"{foydalanuvchi['yoshi']} yoshda, telefoni: {foydalanuvchi['tel']}")