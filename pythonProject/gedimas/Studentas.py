class Studentas:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_age(self):
        return age

class StudentManagmentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Naujas studentas pridetas ")

    def remove_student(self):
        for student in self.studenets:
            if student.get.student_id() == student_id:
                self.students.remove(student)
                print("Studentas pašalintas")
        print("Studentas su šiuo ID nerastas")

    def get_student_info(self, student_id):
        for student in self.student_id:
            if student.get_student_id == student_id:
                print("Studento ID: ", get_student_id)
                print("Studento vardas: ", get_name)
                print("Studento amžius: ", get_age)

        print("Studentas nurodytu ID nerastas ")

    def show_all_students(self):
        if len(self.students) == 0:
            print("Nėra studentų nuomenų ")
            return
        for student in self.students:
            print("Studento ID: ", student.get_student_id)
            print("Studento vardas: ", student.get_name)
            print("Studento amžius: ", student.get_age)
            print("-----------")

    def run(self):
        while True:
            print("\nKomandos:")
            print("1 - Pridėti naują studentą")
            print("2 - Pašalinti studentą")
            print("3 - Gauti informaciją apie studentą pagal ID")
            print("4 - Rodyti visus studentus")
            print("5 - Baigti programą")

            command = input("Iveskite komandos numerį: ")

            if command == "1":
                student_id = input("Įveskite studento ID: ")
                name = input("Įveskite studento varda: ")
                age = int(input("Įveskite studento amžių: "))
                student = Studentas(student_id, name, age)
                self.add_student(student)

            elif command == "2":
                student_id = input("Iveskite studento ID, kurį norite pašalinti ")
                self.remove_student(student_id)

            elif command == "3":
                student_id = input("Įveskite studento ID, apie kurį norite gauti informaciją ")
                self.get_student_info(student_id)

            elif command == "4":
                self.show_all_students()

            elif command == "5":
                print("Programa baikta ")
                break

            else:
                print("Komanda negalima. Bandykite dar kartą")


sistema = StudentManagmentSystem()
sistema.run()













