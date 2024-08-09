#1-topshiriq
def toliq_ism_yasa():
    ism=input("Ismingizni kiriting: ")
    familiya=input("Familiyangizni kiriting ")
    tugilgan_yil=int(input("Tug'ilgan yilingizni kiriting: "))
    joriy_yil=2024
    yosh = joriy_yil - tugilgan_yil
    print(f"Siz {ism.title()} {familiya.title()} {yosh} yoshdasiz")
toliq_ism_yasa()


#2-topshiriq
def kv_kub():
    son=float(input("Istagan soningizni kiriting: "))
    kvadrat=son**2
    kub=son**3
    print(f"{son} ning kvadrati {kvadrat}")
    print(f"{son} ning kubi {kub}")
kv_kub()


#3-topshiriq
def juft_toq():
    son=int(input("Son kiriting: "))
    if son //2==0:
        print("Juft son")
    else:
        print("Toq son")
juft_toq()

#4-topshiriq
def katta_son():
    son1=int(input("1-sonni kiriting: "))
    son2=int(input("2-sonni kiriting: "))
    if son1 > son2:
        print("Katta son=", son1)
    elif son1 < son2:
        print("Katta son=", son2)
    else:
        print("Sonlar teng")
katta_son()


#5-topshiriq
def kv(x,y=2):
    x=float(input("Istagan soningizni kiriting: "))
    kv=x**y
    print(f"{x} ning kvadrati {kv}")
kv()
#6-topshiriq

def qoldiq():
    son = int(input("Son kiriting: "))
    for i in range(2, 10):
        if son % i == 0:
            print(f"{son} = {i} ga qoldiqsiz bo'linadi.")
        else:
            print(f"{son} = {i} ga qoldiq bilan bo'linadi.")

qoldiq()
