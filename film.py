dostlar={
    "Ali":["Terminator", "Rambo", "Titanic"],
    "Vali":["Tenet", "Inaption", "Interstellar"],
    "Hasan":["Abdullajon", "Bomba", "Shaytanat"],
    "Husan":["Mahallada duv-duv gap", "John Wick"]
}
for ism,film in dostlar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in film:
        print(kino.upper())
