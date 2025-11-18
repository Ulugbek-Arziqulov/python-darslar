# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 12:24:30 2025

@author: HI-TECH
"""

# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:
import re

def extract_urls(text):
    pattern = r"(?:https?://|www\.)[^\s<>\"']+"
    urls=re.findall(pattern, text)
   
    urls = [u.rstrip(".,;:!?)]\"'") for u in urls]
    return urls

matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

natija=extract_urls(matn)
print(natija)