import random
import time
sudetai = ["Rugilė", "Egidijus", "Deividas", "Tomas", "Miglė", "SauliusS", "SauliusA", "Aušrinė", "Jūratė",
           "Vaidas", "Modestas"]
random_student = random.choice(sudetai)
time.sleep(3)
print("Atsitiktinai pasirinktas studentas: ", random_student)