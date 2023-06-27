# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#         #parasyti metoda ar knyga turi > 300 psl.
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
# Knyga1 = Knyga("Haris Poteris", "Rowling", 600)
# Knyga2 = Knyga("Potvynis", "Boijring", 250)
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         #parasyti metoda kursi padidins darbuotojo atlyginima tam tikru procentu
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def visa_informacija(self):
#         print(f"informacija apie darbuotoja: ")
#         print(f"vardas: {self.vardas}")
#         print(f"pavarde: {self.pavarde}")
#         print(f"atlyginimas: {self.atlyginimas} ")
#
#
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Arvydas", "Sabonis", 1500)
#
# Darbuotojas1.padidinti_atlyginima(10)
# print(f"Naujas atlyginimas: {Darbuotojas1.vardas} {Darbuotojas1.atlyginimas} eurai ")
# Darbuotojas1.nauja_pavarde("Petraitis")
# print(Darbuotojas1.pavarde)
#
# Darbuotojas1.visa_informacija()
#
# Darbuotojas2.padidinti_atlyginima(10)
# print(f"Naujas atlyginimas: {Darbuotojas2.vardas} {Darbuotojas2.atlyginimas} eurai")


# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         #atnaujinti kaina darom akcija
#
#     def atnaujinti_kaina (self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f"{self.pavadinimas} nauja kaina: {nauja_kaina}")
#
#
#     def sandelio_likutis(self, pardavimo_kiekis):
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"Parduota {self.pavadinimas} {pardavimo_kiekis}")
#         else:
#             print(f"Nepakankamas likutis {self.pavadinimas}")
#
#     def sandelio_papildymas(self, padidintas_likutis):
#         self.kiekis += padidintas_likutis
#         print(f"Padidintas kiekis {self.pavadinimas} {padidintas_likutis}")
#
#
# Preke1 = Preke("Pienas", 5, 50)
# Preke2 = Preke("Duona", 2, 20)
# Preke1.atnaujinti_kaina(3.5)
# Preke1.sandelio_likutis(60)
# Preke1.sandelio_papildymas(10)
# print(f"{Preke1.pavadinimas} Naujas sandelio likutis: {Preke1.kiekis}")

# ---------------------------BLOGAS--------------------------------
# class Blog:
#     def __init__(self):
#         self.posts = []
#     def create_post(self, pavadinimas, aprasymas):
#         post = {
#             "pavadinimas": pavadinimas,
#             "aprasymas": aprasymas
#         }
#         self.posts.append(post)
#         print("Irasas sekmingai sukurtas")
#
#
#     def dispay_all_posts(self):
#         if not self.posts:
#             print("Irasu nerasta")
#         else:
#             print("Blog irasai")
#             for post in self.posts:
#                 print(f"Pavadinimas: {post['pavadinimas']}")
#                 print(f"Aprasymas: {post['aprasymas']}")
#                 print(f"------")
#
#     def update_post(self, pavadinimas, naujas_aprasymas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 post["aprasymas"] = naujas_aprasymas
#                 print("Postas atnaujintas")
#                 break
#         else:
#             print("Blogo postas nerastas")
#
#
#     def delete_post(self, pavadinimas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 self.posts.remove(post),
#                 print("Postas sekmingai pasalintas")
#                 break
#         else:
#             print("Postas buvo rastas")
#
#
# post1= Blog()
# post1.create_post("Kriminaliai", "Dzipas partrenke bobute")
# post1.create_post("Politika", "Sirinskiene nusiskuto usus")
# post1.create_post("Kulinarija", "Pyragas su braskem")
# post1.update_post("Kriminaliai", "Uzsidege palapine")
# post1.dispay_all_posts()
# post1.delete_post("Kriminaliai")


# ----------------------ZMOGUS--------------------
# zmogus = {
#     "vardas": "Jonas",
#     "amzius": 25,
#     "miestas": "Kaunas"
# }
# print("Mano vardas: ", zmogus['vardas'])
#
# # --------------------------pridedame nauja elementa i savo zodyna
# zmogus["lytis"] = "vyras"
# print("As esu ", zmogus["lytis"])

# ---------------------------keitime reiksme
# zmogus["amzius"] = 20
# print("Atsiprasau man yra: ", zmogus['amzius'], "metu")

# --------------------------triname
# del zmogus["miestas"]
# print(zmogus['miestas'])

#-------------------------- interuojame per visus zodyno elementus
# for key, value in zmogus.item():
#     print(key,":, value")

# ------------------------Tuple
# kordinates = (10, 50)
# print(kordinates[1])
# kosdinates1 = (54, 42, 12)
# sujungitos_kordinates = kordinates + kosdinates1
# print(sujungitos_kordinates)



