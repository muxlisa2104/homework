# Avvalgi darslarimizda yaratgan Shaxs va
# Talaba klasslariga yopiq xususiyatlar qo'shing va
# ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
#
# Yuqoridagi klasslarga talabalar_soni va
# odamlar_soni degan klassga oid xususiyatlar qo'shing.
#
# Klassga oid xususiyatlar bilan ishlash uchun maxsus
# @classmethod lar yozing


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __num_shaxs = 0

    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        Shaxs.__num_shaxs += 1

    @classmethod
    def get__num_shaxs(cls):
        return cls.__num_shaxs


    def get_age(self, joriy_yil):
        return joriy_yil - self.tyil


    def get_info(self):
        """Shaxs haqida ma'lumot"""
        return f"Ism:{self.ism} {self.familiya} {self.tyil}-yilda tug'ilgan."


class Talaba(Shaxs):
    """Talaba nomli voris klass"""
    def __init__(self, ism, familiya, tyil):
        super().__init__(ism, familiya, tyil)


odam = Shaxs("Muslima", "Mavlanova", 2017)
odam = Shaxs("Muxlisa", "Mavlanova", 2008)
odam = Shaxs("Alfiya", "Boboxonova",2008)
talaba = Talaba("Quvonchbek", "Mavlanov", 2004)
print(f"{odam.get_info()}. {odam.get_age(2024)} yoshda.")
print(f"{talaba.get_info()}. {talaba.get_age(2024)} yoshda")
print(f"Shaxs soni: {Shaxs.get__num_shaxs()}")
