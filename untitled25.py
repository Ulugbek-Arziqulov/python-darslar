# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:36:51 2025

@author: HI-TECH
"""

# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
from datetime import datetime, timedelta

sana=datetime.now()

for i in range(10):
    print(f"{i+1}-sana: {sana.strftime('%d. %m. %Y')}")
    sana=sana + timedelta(weeks=2)
    

