# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:15:12 2025

@author: HI-TECH
"""

savat=[]
while True:
    mahsulot=input('Mahsulot nomini yozing: ')
    savat.append(mahsulot)
    javob=input("Yangi maxsulot qo'shasizmi? ha/yo'q: ")
    if javob =='ha':
        continue
    else:
        break

print('Sizning buyurtmangiz: ')
for mahsulotlar in savat:
    print(mahsulotlar.title())