country={
    "AQSH":"Washington D.C shahri",
    "ITALIYA":"Rim shahri",
    "Malayziya":"kuala-Lumpur",
    "O'zbekiston":"Toshkent",
    "Qirg'iziston":"Bishkek",
    "Qozogiston":"Nursulton",
    "Rossiya":"Moskva shahri",
    "Singapur":"Singapur",
    "Tojikiston":"Dushanbe"
}
davlat=input("Qaysi davlatning poytaxtini bilishni istaysiz?: ")
if davlat in country:
    print(f"{davlat}ning poytaxti {country[davlat]}")
else:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
