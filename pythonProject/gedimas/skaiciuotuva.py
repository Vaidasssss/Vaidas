class Calculator:
    def __init__(self):
        self.result = 0

    def sudetis(self, skaicius1, skaicius2):
        self.result = skaicius1 + skaicius2

    def atimtis(self, skaicius1, skaicius2):
        self.result = skaicius1 - skaicius2

    def daugyba(self, skaicius1, skaicius2):
        self.result = skaicius1 * skaicius2

    def dalyba(self, skaicius1, skaicius2):
        self.result = skaicius1 / skaicius2

    def gauti_rezultata(self):
        return self.result

skaiciuoklis = Calculator()

while True:
    print("Pasirinkite norimą veiksmą:")
    print("1. Sudėtis")
    print("2. Atimtis")
    print("3. Dalyba")
    print("4. Daugyba")
    print("5. Baigti programa")

    pasirinkimas = input("Įveskite pasirinkimo numerį: ")

    if pasirinkimas == "1":
        skaicius1 = int(input("Įveskite pirmą skaičių: "))
        skaicius2 = int(input("Įveskite antrą skaičių: "))
        skaiciuoklis.sudetis(skaicius1, skaicius2)
        print("Rezultatas:", skaiciuoklis.gauti_rezultata())

    elif pasirinkimas == "2":
        skaicius1 = int(input("Įveskite pirmą skaičių: "))
        skaicius2 = int(input("Įveskite antrą skaičių: "))
        skaiciuoklis.atimtis(skaicius1, skaicius2)
        print("Rezultatas:", skaiciuoklis.gauti_rezultata())

    elif pasirinkimas == "3":
        skaicius1 = int(input("Įveskite pirmą skaičių: "))
        skaicius2 = int(input("Įveskite antrą skaičių: "))
        skaiciuoklis.dalyba(skaicius1, skaicius2)
        print("Rezultatas:", skaiciuoklis.gauti_rezultata())

    elif pasirinkimas == "4":
        skaicius1 = int(input("Įveskite pirmą skaičių: "))
        skaicius2 = int(input("Įveskite antrą skaičių: "))
        skaiciuoklis.daugyba(skaicius1, skaicius2)
        print("Rezultatas:", skaiciuoklis.gauti_rezultata())

    elif pasirinkimas == "5":
        break

    else:
        print("Neteisingas pasirinkimas")

    print()

