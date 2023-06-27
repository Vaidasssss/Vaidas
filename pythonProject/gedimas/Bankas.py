class Bankas:
    #kuriamas konstruktorius
    def __init__(self):
        #sukuriamas tuscias masyvas kuriame talpiname visas banko saskaitas
        self.saskaitos = []

        #kuriame metodo "Nauja saskaita"
    def nauja_saskaita(self, vardas, pradinis_balansas, numeris):
            #  inicijuojame saskaitos parametrus
        saskaita = {
            "vardas": vardas,
            "balansas": pradinis_balansas,
            "numeris": numeris
            }
            # pridedame saskaita
        self.saskaitos.append(saskaita)
        print("Nauja saskaita sekmaingai sukurta")

        # balanso didinimas

    def balanso_didinimas(self, saskaitos_numeris, suma):
            #iteruosime visas saskaitas ir atrasime musu saskaita kurioje norime padidinti valansa
        for saskaita in self.saskaitos:
            if saskaita["numeris"] == saskaitos_numeris:
                if saskaita["balansas"] >= suma:
                    saskaita ["balansas"] -= suma
                    print("Pinigai sekmingai isimti")
                else:
                    print("Nepakankamas saskaitos likutis")
                break
        else:
            print("Nepavyko rasti saskaitos su nurodytu numeriu!")

    def balansas(self, saskaitos_numeris):
        for saskaita in self.saskatos:
            if saskaita["numeris"] == saskaitos_numeris:
                print(f"Saskaitos Balansas: {saskaita['balansas']} €")
                break
        else:
            print("Nepavyko rasti saskaitos su nurodytu numeriu!")

# sukuriame objekta
sebBankas = Bankas()

# naudojame while cikla ir leidziame klientui pasirinkti norima operacija
while True:
    print("Pasirinkite norima veikima_> ")
    print("1. Sukurti nauja saskaita")
    print("2. Inesti lesas i saskaita")
    print("3. Isimti lesas is saskaitos")
    print("4. Patikrinti saskaitos balansa")
    print("0. Uzbaigti pasirinkimus")
    pasirinkimas = input ("Iveskite pasirinkimo numeri_> ")

    #inicijuojame veikimus
    if pasirinkimas == "1":
        vardas = input("Iveskite varda_> ")
        pradinis_balansas = float(input("Iveskite pradini balansa_> "))
        numeris = input("Iveskite saskaitos numeris_> ")
        # gauname vardas ir pradinis balansas
        sebBankas.nauja_saskaita(vardas, pradinis_balansas, numeris)
    elif pasirinkimas == "2":
        numeris = input("Iveskite saskaitos numeris_> ")
        suma = float(input("Iveskite inesama suma_> "))
        sebBankas.isemimas(numeris, suma)
    elif pasirinkimas == "3":
        numeris = input("Iveskite saskaitos numeris_> ")
        suma = float(input("Iveskite isimama suma_> "))
        sebBankas.isemimas(numeris, suma)
    elif pasirinkimas == "4":
        numeris = input("Iveskite saskaitos numeri_> ")
        sebBankas.balansas(numeris)
    elif pasirinkimas == "0":
        break
    else:
        print("Neteisingas pasirinkimas! Bandykite dar karta.")


1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.

suma += 0
    if skacius == 0
        print(suma)
    else:
        print(0)
sasrasas= [1, 2, 3, 4, 5, 6, 8, 7]
rezultatas= skacius + sasrasas
print(rezultatas)
