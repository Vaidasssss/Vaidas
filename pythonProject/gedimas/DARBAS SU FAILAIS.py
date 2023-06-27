#DARBAS SU FAILAIS NAUDOJANT OPEN FUNKCIJA;
#FAILO ATTIDARYMAS
# r - read skaito faila
# w - write bando nurasyti tam tikras reiksmes
# a - append egzistuojanti faila peraso
# encoding="utf8" supranta lietuvi6kas raides
# file = open("tekstas.txt", "a", encoding="utf8")
# content = file.write("Tekstas naujame faile, kuremia išbandome open funkcija")
# print(content)


#uzdaro faila
# file = open("tekstas.txt", "a", encoding="utf8")
# file.write("Tekstas naujame faile, kuriame išbandome open funkcija")
# file.close()

#\n perkelia i nauja eilute
# whith automatiskai uzdaro nereikia close
# with open("tekstas1.txt", "w", encoding="utf8") as file:
#     file.write("Tekstas antrajame faile\n")
#     file.write("Antra eilute\n")
#     file.write("Trecia eilute\n")


#Faifo apieskas ir suradimas
# filename = input("Iveskite savo failo pavadinimas->")
#
# try:
#     with open(filename, "r", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileExistsError:
#     print("File not found!")
# except:
#     print("Somthing went wrong")



# filename = input("Iveskite nauja pavadinima->")
#
# try:
#     with open(filename, "w", encoding="utf8") as file:
#         file.write("Obuolys\n")
#         file.write("Bananas\n")
#         file.write("Slyva\n")
#         print("Duomenys sekmingai irasyti")
#
# except:
#     print("Kazkas negerai")

