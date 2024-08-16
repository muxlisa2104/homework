# 1-masala
# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting
# (ism, foydalanuvchi ismi, email, va hokazo)


class User :
    def __init__(self, name, username, email):
        self.name = name
        self.uname = username
        self.mail = email
    def describe(self):
        return  (f" Ismi: {self.name}; "
                 f"Foydalanuvchi nomi: {self.uname}; ")
    def get_mail(self):
        return f"Elektron pochtasi: {self.mail}"
user1 = User("Muxlisa", "muxlisa2104", "mavlonova252022@gmail.com")
print(user1.describe(), user1.get_mail())

#2-masala
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin
# (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).



class Foydalanuvchi:
    def __init__(self, username, ism, familiya, email):
        self.uname = username
        self.ism = ism
        self.familiya = familiya
        self.mail = email
    def get_uname(self):
        """Foydalanuvchining foydalanuvchi nomini qaytaradi"""
        return f"Foydalanuvchi nomi: {self.uname} "
    def get_fullname(self):
        """Foydalanuvchining ism-familiyasini qaytaradi"""
        return f"Ismi: {self.ism} {self.familiya} "
    def get_mail(self):
        """Foydalanuvchinining elektron pochta manzilini qaytaradi"""
        return  f" Pochtasi: {self.mail}"
foydalanuvchi=Foydalanuvchi("muxlisa2104", "Muxlisa", "Mavlanova", "mavlonova252022@gmail.com")
print(foydalanuvchi.get_uname(), foydalanuvchi.get_fullname(), foydalanuvchi.get_mail())