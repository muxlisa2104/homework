davlatlar={
    "O'zbekiston":{"poytaxt":"Toshkent",
                   "hududi":448978,
                   "aholisi":33000000,
                   "pul birligi":"so'm"},
    "Rossiya":{"poytaxt":"Moskva",
                    "hududi":17098246,
                    "aholisi": 144000000,
                    "pul birligi": "rubl"},
    "AQSh":{"poytaxt":"Vashington",
                    "hududi":9631418,
                    "aholisi": 327000000,
                    "pul birligi": "dollar"},
    "Malayziya":{"poytaxt":"Kuala-lumpur",
                    "hududi":329750,
                    "aholisi": 25000000,
                    "pul birligi": "rinngit"}
    }
for davlat,malumot in davlatlar.items():
    print(f"\n{davlat.title()}ning poytaxti\t{malumot['poytaxt'].title()},")
for a,b in malumot.items():
    print(f"{a}:{b}")
