#1-topshiriq
savol="Yaxshi ko'rgan kitobingizni kiriting: "
savol+="(dasturni to'xtatish uchun 'stop' deb yozing): "
while True:
    qiymat=input(savol)
    if qiymat == 'stop':
        break

  
#3-topshiriq
mahsulotlar=[]
print("Buyurtma qabul qiluvchi ro'yxat tuzamiz: ")
n=1
while True:
    savol=f"{n}-mahsulot nomini kiriting: "
    mahsulot=input(savol)
    mahsulotlar.append(mahsulot)
    javob=input("Yana mahsulot qo'shasizmi? (Yes/No) ")
    if javob=="Yes":
        n+=1
        continue
    else:
        break
print(mahsulotlar)



#4-topshiriq
ebozor={}
while True:
    mahsulot=input("Mahsulot nomini kiriting: ")
    narx=input(f"{mahsulot.title()}ning narxini kiriting: ")
    ebozor[mahsulot]=float(narx)
    javob=input("Yana mahsulot kiritasizmi? (ha/yoq) ")
    if javob=="yoq":
        break
for mahsulot, narx in ebozor.items():
    print(f"{mahsulot.title()} {narx} so'm")
