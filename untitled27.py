# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:23:48 2025

@author: HI-TECH
"""

# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
import datetime as dt

def yosh_hisobla(y, o, k):
    bugun=dt.date.today()
    tugilgan=dt.date(y, o, k)
    
    yil=bugun.year-tugilgan.year
    oy=bugun.month-tugilgan.month
    kun=bugun.day-tugilgan.day
    if kun <0:
        oy-=1
        oldingi_oy=bugun.month-1 if bugun.month > 1 else 12
        oldingi_yil=bugun.year if bugun.month > 1 else bugun.year - 1 
        kun+=(dt.date(oldingi_yil,oldingi_oy +1, 1)- dt.date(oldingi_yil, oldingi_oy, 1)).days
        
    if oy < 0:
        yil -= 1
        oy += 12
    
    return yil, oy, kun
y, o, k =yosh_hisobla(1994,5,24)
print(f"Tug'ilganingizdan beri {y} yil {o} oy {k} kun bo'ldi")
    



