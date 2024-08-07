
#1-topshiriq
alloma={
    'Abu Abdulloh Muhammad':{"familya":"ibn Ismoil",
        "yil":810,
        "joy":"Buxoro",
        "umr":60 },
    'Abdulla':{"familya":"Qodiriy",
        "yil":1894,
        "joy":"Toshkent",
        "umr":44 },
    'Erkin':{"familya":"Vohidov",
        "yil":1936,
        "joy":"Farg'ona",
        "umr":80 },
    'Alisher':{"familya":"Navoiy",
        "yil":1441,
        "joy":"Xirot",
        "umr":60 }
}
for ism, info in alloma.items():
    print(f"\n{ism.title()} {info['familya'].title()}, {info['yil']}-yilda {info['joy']}da tavallud topgan. {info['umr']} yil umr ko`rgan. ")





#2-topshiriq
alloma={
    'Abu Abdulloh Muhammad':{"familya":"ibn Ismoil",
        "yil":810,
        "joy":"Buxoro",
        "umr":60,
        "asarlari":["Al-jome`as-sahih","Al-adab al-mufrad","At-tarix al-kabir","At-tarix as-sag`ir"]},
    'Abdulla':{"familya":"Qodiriy",
        "yil":1894,
        "joy":"Toshkent",
        "umr":44,
        "asarlari":["O`tgan kunlar", "Mehrobdan Chayon", "Obid ketmon"]},
    'Erkin':{"familya":"Vohidov",
        "yil":1936,
        "joy":"Farg'ona",
        "umr":80,
        "asarlari":["Tong nafasi", "Qo'shiqlarim sizga", "O`zbegim", "Qiziquvchan Matmusa"] },
    'Alisher':{"familya":"Navoiy",
        "yil":1441,
        "joy":"Xirot",
        "umr":60,
        "asarlari":["Xamsa", "Lison ut-tayir", "Mahbub Al-qulub"]}
    }
for ism, info in alloma.items():
    print(f"\n{ism.title()} {info['familya'].title()}, quyidagi asarlarni yozgan: \n {info['asarlari']}")
