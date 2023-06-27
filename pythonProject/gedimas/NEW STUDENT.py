class Studentas:
    def __init__(self, studento_id, vardas, amzius):
        self.studento_id = studento_id # Inicializuojamas studento ID atributas
        self.vardas = vardas # Inicializuojamas vardo atributas
        self.amzius = amzius # Inicializuojamas amžiaus atributas

    def get_studento_id(self):
        return self.studento_id # Grąžinamas studento ID

    def get_vardas(self):
        return self.vardas # Grąžinamas vardas

    def get_amzius(self):
        return self.amzius # Grąžinamas amžius

class SarasoValdymas:
    def __init__(self):
        self.studentai=[] # Inicializuojamas tuščias studentų sąrašas

    def prideti_studenta(self, studentas):
        self.studentai.append(studentas) # Pridedamas studentas prie sąrašo
        print("Studentas pridetas") # Spausdinamas pranešimas apie pridėjimą

    def istrinti_studenta(self, studento_id):
        for studentas in self.studentai:
            if studentas.get_studento_id() == studento_id: # Tikrinama, ar studento ID sutampa
                self.studentai.remove(studentas)  # Pašalinamas studentas iš sąrašo
                print("Studentas pasalinta ") # Spausdinamas pranešimas apie pašalinimą
        print("Studentas su norodytu ID pasalintas ") # Spausdinamas pranešimas, jei nerasta studento su nurodytu ID

    def get_studento_info(self, studento_id):
        for studentas in self.studentai:
            if studentas.get_studento_id() == studento_id: # Tikrinama, ar studento ID sutampa
                print("Studento ID ", studentas.get_studento_id()) # Spausdinamas studento ID
                print("Vardas ", studentas.get_vardas()) # Spausdinamas studento vardas
                print("Amzius ", studentas.get_amzius()) # Spausdinamas studento amžius
        print("Studentas su norodytu ID nerastas") # Spausdinamas pranešimas, jei nerasta studento su nurodytu ID


    def parodyti_visus_studentus(self):
        if not self.studentai:
           print("Studetnu sarase nerasta ") # Spausdinamas pranešimas, jei sąrašas tuščias
        for studentas in self.studentai:
            print("Studento ID ", studentas.get_studento_id()) # Spausdinamas studento ID
            print("Vardas ", studentas.get_vardas()) # Spausdinamas studento vardas
            print("Amzius ", studentas.get_amzius()) # Spausdinamas studento amžius

    def paleisti(self):
        while True:
            print()
            print("1 - Pridėti naują studentą")
            print("2 - Pašalinti studentą")
            print("3 - Gauti informaciją apie studentą pagal ID")
            print("4 - Rodyti visus studentus")
            print("5 - Baigti programą")
            print()

            komanda = input("Iveskite komanda: ")

            if komanda == "1":
                studento_id = input("Iveskite studento ID ")
                vardas = input("Iveskite varda ")
                amzius = input("Iveskite amziu ")
                studentas = Studentas(studento_id, vardas, amzius) # Sukuriamas Studentas objektas
                self.prideti_studenta(studentas)

            elif komanda == "2":
                studento_id = input("Iveskite studento ID kuri norite pasalinti ")
                self.istrinti_studenta(studento_id) # Pašalinamas studentas pagal nurodytą ID

            elif komanda == "3":
                studento_id = input("Iveskite studento ID, apie kuri norite gauti informacija ")
                self.get_studento_info(studento_id) # Gaunama informacija apie studentą pagal nurodytą ID

            elif komanda == "4":
                self.parodyti_visus_studentus() # Rodomi visi studentai sąraše

            elif komanda == "5":
                print("Programa baigta ") # Spausdinamas pranešimas apie programos pabaigą
                break

            else:
                print("Komanda neteisinga, bandykite dar karta") # Spausdinamas pranešimas apie netinkamą komandą


sistema = SarasoValdymas()
sistema.paleisti()

