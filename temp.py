# AMALIYOT        

# # Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# #  Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy 
# #  ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familiya,**talabalar):
    talabalar[ism]=ism
    talabalar[familiya]=familiya
    return talabalar

talaba1=talaba_info("odina", 'olimova', tyil=1990, tjoy='samarqand',)
talaba2=talaba_info("salim", 'olimov', tyil=1992, tjoy='samarqand',)
print(talaba1)

