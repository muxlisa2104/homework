class Talaba:
    """Talaba klassi"""
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.fanlar = []

    def fanga_yozil(self, fan):
        if fan not in self.fanlar:
            self.fanlar.append(fan)
        else:
            print("Siz bu fanga allaqachon yozilgansiz! ")

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        return  f"Ism:{self.ism}; Yosh:{self.yosh}; Fanlar: {[fan.fan_nomi for fan in self.fanlar]}"


class Fan:
    """Fan klassi"""
    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi

class Professor(Talaba):
    def __init__(self, ism, yosh, lavozim):
        super().__init__(ism, yosh)
        self.lavozim = lavozim

    def get_info1(self):
        return f"Professor: {self.ism}, Yosh: {self.yosh}, Lavozim: {self.lavozim}, Fanlar: {[fan.fan_nomi for fan in self.fanlar]}"

class Foydalanuvchi:
    def __init__(self, username, email):
        self.username = username
        self.mail = email

    def get_info2(self):
        return f"Foydalanuvchi: {self.username} Pochtasi: {self.mail}"



class Sotuvchi(Foydalanuvchi):
    def __init__(self, username, email, sotuvlar_soni):
        super().__init__(username, email)
        self.sotuv_soni = sotuvlar_soni

    def get_info3(self):
        return f"Sotuvchi: {self.username} Pochtasi: {self.mail} Sotuvlar soni: {self.sotuv_soni}"



class Mijoz(Foydalanuvchi):
    def __init__(self, username, email, buyurtmalar_soni):
        super().__init__(username, email)
        self.buyurtmalar_soni = buyurtmalar_soni

    def get_info4(self):
        return f"Mijoz: {self.username}, Email: {self.mail}, Buyurtmalar: {self.buyurtmalar_soni}"


class Admin(Foydalanuvchi):
        def __init__(self, username, email, admin_id):
            super().__init__(username, email)
            self.admin_id = admin_id

        def ban_user(self):
            print("Foydalanuvchi bloklandi")


        def get_info5(self):
            return f"Admin: {self.username} Pochtasi: {self.mail} Admin ID: {self.admin_id}"


        def ban_user(self):
            print("Foydalanuvchi bloklandi")


# Fan obyektlarini yaratish
math = Fan("Matematika")
phy = Fan("Fizika")

# Talaba obyektini yaratish
student = Talaba("Aziz", 18)
student.fanga_yozil(math)
student.fanga_yozil(phy)
print(student.get_info())

# Professor obyektini yaratish
professor = Professor("Javohir", 25, "Matematika professori")
professor.fanga_yozil(math)
print(professor.get_info1())

# Sotuvchi va Mijoz obyektlarini yaratish
sotuvchi = Sotuvchi("Guli", "gul@gmail.com", 120)
mijoz = Mijoz("Aziza", "aziza@gmail.com", 5)
print(sotuvchi.get_info3())
print(mijoz.get_info4())

# Admin obyektini yaratish va test qilish
admin = Admin("Muxlisa", "mavlonova252022@gmail.com", "00112233")
admin.ban_user()
print(admin.get_info5())
