
#Komentuoja vieną eilutę
"""
Komentuoja daug eilučių
"""
# vardas = "Vaidas"
# amzius = 24
# print (vardas)
# print(amzius)
# print(type(vardas))
# # kaip pasitikrinti kintajomo reikšmę
# print (type(amzius))
# # kaip pasitikrinti kintajomo reikšmę

# arVartotojasAktyvus = False
# print(type(arVartotojasAktyvus))

# produktoKaina = 3.99
# print(type(produktoKaina))
# Float- per kablei

# miestas= ["Vilnius", "Kaunas", "Klaipeda"]
# print(miestas[0])------------------grazina reiksmes, skai2iuojama nuo 0, šiuo atveju gražina Vilnių
# list- sarasas

# print(miestas[-1])
# miestas[1]= "Šiauliai"
# print(miestas) -----------jeigu reikia pakeisti vieną iš reikšmių, čia keičiame Kauna į Šiaulius

# miestas.append("Kėdainiai")
# print(miestas)---------prideda papildomą reikšmę, čia pridėjome Kėdainiai

# miestas.insert(1,"Anyščiai")
# print(miestas)------------nurodomas vieta kur įdedamas miestas

# miestas.pop()
# print(miestas)---------ištrina paskutinį kintamajį

# del miestas[2]
# print(miestas)-----------ištrina nurodytrą kintamajį


# print("As gyvenu " + miestas [0])--------sujunge savo tekstą su kintamaisiais

# print("Mano vardas " + vardas + "As gyvenu " + "Mano azius " + str(amzius))
# str- pakeičia skaičių (integer) reikšmes į raidines (varchar)

# ctrl+S---išsaugo

# Surašomos reikšmės kurioms atittikus spausdina nurodytas reikšmes
# if amzius > 18:
#     print("Pilnametis")
# elif amzius>= 24:
#     print("Daugiau nei 18")
# else:
#     print("Nepilnametis")

# print(len(miestas))--------parašo kiek elementų yra

# skaiciuSarasa = [1,2,3,5,666,8]
# if len(skaiciuSarasa) >0:
# print("pilnas")
# else:
# print("tuscias")


# zodis= "Kaunas"
# if zodis in miestas:
#     print("Zodis " + zodis + "egzizstuoja")
# else:
#     print("Zodis nerastas")

# skaicius = int(input("Iveskite skaiciu: "))
#
# if skaicius > 0:
#     print("Skeicius neigemas")
# elif skaicius <0:
#     print("Skai2ius neigemas")
# else:
#     print("Skaiucs yra nulis")

"""
PRISKIRIMO
= Priskirimas
+= Pirededa ir priskiria
-= Atima ir priskiria
*=
/=
%=



MATEMATINIAI OPERATORIAI
+
-
*
/
%
** kėlimas laipsniu
// sveikoji dalyba

PALYGINIMO OPERATORIAI
== lygu
!= nelygu
>
<
>=
<=


LOGINIAI OPERATORIAI
AND
or 
not

NARYSTES OPERATORIAI

in
not in

TAPATUMO OPERATORIAI

is
is not

"""


# 2. Patikrinkite, ar skaičius yra lyginis;
# skaiciai= 10
# if skaiciai %2== 0:
#     print("Lygus")
# else:
#     print("Nelyginis")

# 3. Patikrinkite, ar sąraše yra bent du skaičiai
# sarasa= [1]
# if len(sarasa)>=2:
#     print("yra")
# else:
#     print("Nera")


# for i in range(1, 11): --------reikšmes gražina stulpeliu
#     print(i)

# vardai = ["Jonas", "Saulius", "Lina", "Marius", "Rugile"]
# #    key       reiksme
# for vardas in vardai:
#     print(vardas)

# skaiciai = [10, 20, 30, 40, 50, 23]
# atrinkti = []
#
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaiciai)
# print("Atrinkti skaiciai: ", atrinkti)

# skaiciai = [10, 20, 30, 40, 50, 23, 10, 45, 2, 44, 11, 21] ------------panaikina pasikartojancias reiksmes
# unikalios_reiksmes = []
# for skaicius in skaiciai:
#     if skaicius not in unikalios_reiksmes:
#         unikalios_reiksmes.append(skaicius)
# print("Unikalios reiksmes: ", unikalios_reiksmes)


# def nordo funkcija, priskiriama kokie veiksmai turi buti atliekami
# def suma(a, b):
#     return a + b
#
# rezultatas = suma(2, 5)
#
# print("suma: ", rezultatas)

# def pasisveikinimas(vardas="Anonimas"):
#     print("Labas, ", vardas)
# pasisveikinimas("Vaidas")


# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
#
# rezultatas = sujungti_sarasus([1, 2, 3], [4, 5, 6])
# print("Sujungtas sarasas: " , rezultatas)

# 1.Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina, ar skaičius yra lyginis. Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False.


# def ar_lyginis (skaicius):
#
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print(ar_lyginis(9))
# arašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;
#
# def didziausias_skaicius (sarasas):
#     didziausias= sarasas [0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# skaiciusarasas= [1, 2 ,7, 80, 50, 54, 6, 10]
# rezultatas= didziausias_skaicius(skaiciusarasas)
# print(rezultatas)

# Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą, kuriame yra tik unikalios reikšmės iš pradinio sąrašo.
# def unikalios_reiksmes(sarasas):
#     tuscias_listas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_listas:
#             tuscias_listas.append(reiksme)
#     return tuscias_listas
# naujas_sarasas = [1, 2, 5, 52, 56, 58, 56, 56, 58, 52, 1, 1]
# print(unikalios_reiksmes(naujas_sarasas))


# 2.Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių.
# def didziausias_skaicius(skaiciu_sarasas):
#     didziausias= skaiciu_sarasas [0]
#     for skaicius in skaiciu_sarasas:
#         if skaicius > didziausias:
#             didziausias=skaicius
#     return didziausias
# sarasas = [1, 5, 9, 6, 50, 59, 99]
# rezultatas= didziausias_skaicius(sarasas)
# print(rezultatas)



# 1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.
# def suma_be_lyginiu(sarasas):
#     suma = 0
#     for skaicius in sarasas:
#         if skaicius % 2 != 0:
#             suma += skaicius
#     return suma
# skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rezultatas = suma_be_lyginiu(skaiciai)
# print(rezultatas)


# 3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.

# def ar_pirminis(skaicius):
#     if skaicius < 2:
#         return False  # Skaičius mažesnis nei 2 negali būti pirminis
#     for i in range(2, int(skaicius ** 0.5) + 1):
#         if skaicius % i == 0:
#             return False  # Skaičius dalijasi be liekanos, todėl nėra pirminis
#     return True
# skaicius = 5
# rezultatas = ar_pirminis(skaicius)
# print("17= ", + rezultatas)  # Rezultatas: True
#
# skaicius = 15
# rezultatas = ar_pirminis(skaicius)
# print("15= ", + rezultatas)  # Rezultatas: False

# Atras būdas, reikia pataisyti
# def pirminis(skaicius):
#     if skaicius < 2:
#         return False
#     for daliklis in range(2, skaicius):
#         if skaicius % daliklis == 0:
#         return False
#     return True
# skaicius = 3
# if pirminis(skaicius):
#     print(f"skaicius {skaicius} yra pirminis skaicius")
# else:
#     print(f"skaicius {skaicius} yra ne pirminis skaicius") #f radė leidžia vidurį teksto įdėti funkciją {} skaliaustuose dedame savo funkciją




#---------------------- WHILE---------------
# skaicius = 1
# while skaicius <=5:
#     print(skaicius)
#     skaicius += 1

# skaicius = int(input("iveskite_skaiciu: "))
# while skaicius >= 0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1


# 1. Užduotis: Parašykite programą, kuri paprašytų vartotojo įvesti savo vardą ir pasisveiktų jį, atspausdinant žinutę "Labas, [vardas]!".
# vardas= input("Įveskite savo vardą: ")
# print("Labas: ", vardas, "f")

# 2.  Užduotis: Parašykite programą, kuri paprašytų vartotojo įvesti skaičių ir atspausdintų jo kvadratą.
# skaicius= int(input("Iveskite skaicius: "))
# suma= skaicius ** 2
# print("Skaicius kvadratu ", suma)

# 4. Užduotis: Parašykite programą, kuri suskaičiuotų ir atspausdintų skaičių nuo 1 iki 10 sumą.

# suma = 0
# for skaicius in range(1, 66):
#     suma += skaicius
# print(suma)


