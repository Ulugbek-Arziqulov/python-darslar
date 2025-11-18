# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:10:01 2025

@author: HI-TECH
"""

# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
"""Hayitgacha bo'lgan kunni taxminiy xisoblaymiz!"""

import datetime as dt
bugun=dt.datetime.now()
ramazon=dt.datetime(2026,4,1)
qurbon=dt.datetime(2026,6,10)
ramazon=ramazon-bugun
qurbon=qurbon-bugun
print(f"Ramazon hayitigacha {ramazon} kun bor!")
print(f"Qurbon hayitigacha {qurbon} kun bor!")





