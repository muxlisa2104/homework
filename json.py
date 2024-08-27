import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)

with open('data.json','w') as data:
    json.dump(data_json, data)

talaba_json = {
    "ism":"Hasan",
    "familiya":"Husanov",
    "tyil":2000
    }
ismi = talaba_json['ism']
fam = talaba_json ['familiya']
print(f"F.I.O.: {ismi} {fam}")
