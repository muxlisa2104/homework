 lugat={"for":"uchun",
        "if":"agar",
        "integer":"butun sonlar",
        "string":"matn",
        "float":"haqiqiy sonlar tipi"}
 for i in sorted(lugat.keys()):
     print(i)
 print()
 for i2 in sorted(lugat.values()):
     print(i2)
 sorted = dict(sorted(lugat.items()))
 for kalit,qiymat in sorted.items():
     print(f"{kalit}: {qiymat}")




 country={
     "AQSH":"Washington D.C",
     "Malayziya":"Bishkek",
     "Italiya":"Rim",
     "O'zbekiston":"Toshkent",
     "Qirg'iziston":"Dushanbe"
 }

 davlat=input("Qaysi davlatning poytaxtini bilishni istaysiz?")
 if davlat in country:
     print(f"{davlat} ning poytaxti {country[davlat]}")
 else:
     print("Kechirasiz bu davlat haqida bizda malumot yoq")



 lugat={
     "for":"uchun",
     "if":"agar",
     "integer":"son",
     "string":"matn",
     "float":"onlik son",
     "input":"kiritish",
     "boolean":"mantiqiy qiymat",
     "dot":"nuqta",
     "key":"kalit",
     "value":"qiymat"
    }
s=[]
q=[]
for i, k in lugat.items():
     s.append(i)
     q.append(k)
print(*sorted(s))
print(*sorted(q))
