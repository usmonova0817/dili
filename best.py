# name = "dunyo,baxora, dilnoza Muborak"
# print(name)
#
# name = "Abror"
# print("salom" + ' ' +  name + ' ' + "bugun darsga borasanmi?")
# name = "Diyor"
# print(name + ' '+ "choyhonaga boramizmi")
#
# sonlar = 2,-4, 0, 34.5,
# print(sonlar)
#
# a = 12
# b = 45
# c = a + b
# print(c)
#
#
# a = int(input("a sonini kiriting"))
# b = int(input(" b sonini kiriting"))
# c = a + b
# print(c)

# name = ['Dunyp', 'Shaydo','Laylo']
# print(name)
#
# print("salom", name[1])
#
# sonlar = [45, 67.8, -34  ]
# print(sonlar)
# a = sonlar[0] + sonlar[2]
# print(a)
#
# t_shaxs = ['Alisher Navoiy','Buxoriy']
# z_shaxs = ['Ilon Maek','Bell Gets']
#
#
# mamlakatlar = ['AQSH', 'Ukrayina','London',]
# print(mamlakatlar)
#
# bozorlik = ['olma', 'nok', 'olcha', 'urik', 'anjir']
# print(sorted(bozorlik))
# print(bozorlik)
# print(len(bozorlik))
#
# gullar = ['atirgul', 'chinnigul','lola', 'rayhon',]
# gullar.sort(reverse=True)
# print(gullar)
# ismlar = ['Nora', 'dilnoza', 'gulnoza', 'Aziza', 'lola', 'madina']
# print(sorted(ismlar))
# print(ismlar)
#
#
# raqamlar =  list(range(0, 26))
# print(raqamlar)
# print(raqamlar[18] - raqamlar[4])
#
# juft_sonlar = list(range(120, 1200,2))
# toq_sonlar = list(range(121, 1200, 2))
# print(juft_sonlar)
# print(toq_sonlar)
# print(juft_sonlar[6] - toq_sonlar[2])
# print(len(juft_sonlar))
# print(len(toq_sonlar))
#
#
#
# nomerlar = list(range(0, 30))
# my_nomer = nomerlar[0:20]
# print(my_nomer)
#
#
# toamlar = ['dulma', 'qazi', 'tandir', 'kabob', 'shashlik', 'osh']
# toamlar.append("shurva  osh tort choy")
# print(toamlar)
#
# toamlar = ['dulma', 'qazi', 'tandir', 'kabob', 'shashlik', 'osh']
# toamlar2 = toamlar
# toamlar2.append("yahna")
# toamlar2.append("limon")
# print(toamlar)
# print(toamlar2)



# uyga vazifa 3 topshiriq

# toq_sonlar = list(range(11, 100, 2))
# print(toq_sonlar)
# raqamlar = list(range(11, 100,2))
# for raqam in raqamlar:
#     print(f"{raqam}ning kubi {raqam**3}ga teng")
#
#
#
# #4-topshiriq
#
# kinolar = []
# print(" 5 ta yoqtirgan kinogizni nomini yozing")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-dagi kino nomini kiriting"))
# print(kinolar)
#
# #5 topshiriq
# ismlar = []
# print("bugun nechta odam bilan uchrashdingiz")
# for n in range(3):
#     ismlar.append(input(f"{n+1}-uchrashgan odamingiz ismini yozing:"))
#
# print(ismlar)





#1-topshiriq

# a = float(input("istalgan son kiriting:"))
#
# if a <=0:
#     print(f"{a} manfiy son")
# else:
#     print(f" {a} musbat son")

#3-topshiriq


# a =  float(input("birinchi soni kiriting:"))
# b = float(input("ikkinchi soni kiriting:"))
# if a==b:
#     print(f"sonlar bir-biriga teng;{a}={b}")
# else:
#     print(f" sonlar bir-biriga teng emas")



#2-topshiriq

# a = float(input("istalgan son kiriting"))
# if a >=0:
#     print(f"{a}ning kvadrat ildizi {a**0.5}ga teng")
# else:
#     print(f'{a} manfiy son kiritingiz')


#1topshiriq

# b = float(input("istalgan son kiriting"))
# if b >= 0:
#     print(f"siz kiritgan {b} son musbat")
# else:
#     print(f"siz kiritgan {b} manfiy ")
#
# #2 topshiriq
#
# a = float(input("stalgan son kiriting"))
# if a >= 0:
#     print(f"siz kiritgan son musbat va {a}ning kvadrat ildizi {a**0.5} ga teng")
# else:
#     print(f"siz kiritgan {a} son manfiy musbat son kiriting")

# # 3 topshiriq
# a = float(input(" Birinchi soni kiriting "))
# b = float(input("ikkinchi soni kiriting "))
# if a==b:
#     print(f"siz kiritgan sonlar bir biriga teng {a} = {b}")
# else:
#     print(f"siz kiritgan sonlar bir biriga teng emas ")

#4topshiriq
# yosh = int(input("yoshingiz nechida "))
# if 4>= yosh >= 60:
#     price = 0
# elif yosh <= 18:
#     price = 10000
# elif yosh >= 18:
#     price = 20000
# print(f"sizning yoshingiz {yosh}da, sizga  kirish {price} sum")

# #5 topshiriq
# a = float(input("Birinchi sonni kiriting"))
# b = float(input("Ikkinchi sonni kiriting"))
# if a == b:
#     print("kiritgan sonlaringiz teng ")
# else:
#     print("siz kiritgan sonlar teng emas")


maxsulotlar = ['olma' 'nok' 'urik' 'olcha' 'non' 'uzum' 'gilos' 'yog' 'hurmo' 'dulana']
savat = [ ]
for n in range(5):
    savat.append(input(f"savatga {n+1} maxsulot kiriting"))
for maxsulot in savat:
    if  maxsulot in maxsulotlar:
        print(f"dukonda {maxsulot} bor")
else:
    print(f"dukonda {maxsulot} yuq")


































































































































































































