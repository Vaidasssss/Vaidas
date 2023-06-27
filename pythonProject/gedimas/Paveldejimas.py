
# metodo perrasymas
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal make a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def make_sound(self):
#         print("The dog barks")
#
#
# dog = Dog("Bob", 5)
# dog.make_sound()
# print(dog.name, dog.age)


# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start_engine(self):
#         print("Engine started")
#
#     def stop_engine(self):
#         print("Engine stoped!")
#
# class Car(Vehicle):
#
#     def dirve(self):
#         print("Car is driving")
#
# car = Car("Toyota")
# car.start_engine()
# car.dirve()
# car.stop_engine()

#  class Zmogus:                              #sukuriame tevine klase
#     def __init__(self, name, age):          #isvardiname savybes
#         self.name = name                    #aprasome savybes
#         self.age = age
#
#     def display_info(self):                 #METODAS rodyti informacija apie zmogu
#         print(f"Vardas {self.name}")
#         print(f"Metai {self.age}")
#
# class Darbuotojas(Zmogus):                  #Sukuriame vaikine klase
#     def __init__(self, name, age, salary):  #Isvardiname kokias savybes tures darbuotojas
#         super().__init__(name, age)         #nurodome, kurias savybes tures darbuotojas
#         self.salary = salary                #aprasome papildoma darbuotojo savybe
#
#     def display_info(self):
#         super().display_info()              #panaudosiu tevines klases metoda. print vardas, amzius
#         print(f"Atlyginimas {self.salary}")
#
# zomogus = Zmogus("Antanukas", 12)           #panaudosius tevines klases metoda. print vardas, amzius
# darbuotojas = Darbuotojas("Jonukas", 13, 200)
#
# zomogus.display_info()
# print()
# darbuotojas.display_info()



# sukurti pirkiniu prepselio funkcionaluma. turim prodykta ir pirkiniu krepseli----------------------------------------

# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#     def display_info(self):
#         print(f"Pavadinimas {self.title}")
#         print(f"Kaina {self.price} $")
#
# class DiscountedProduct(Product):
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage
#
#     def calculate_discount_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discounted_price = self.price - discount_amount
#         return discounted_price
#
#
#     def display_info(self):
#         super().display_info()
#         print(f"Nuolaida {self.discount_percentage} %")
#         print(f"Galutine kaina {self.calculate_discount_price()} $")
#
# class ShoppingCart(Product):
#     def __init__(self):
#         super().__init__(title=None, price=None)
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         print(f"Produktas {product.title} idetas")
#
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print(f"Produktas {product.title} pasalintas")
#         else:
#             print(f"Produktas {product.title} nerastas")
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products:
#             total_price += product.price
#         return total_price
#
#
#
# prod = Product("Pienas", 2.99)
# prod1 = DiscountedProduct("Obuolys", 2.99, 15)
# prod2 = Product("Sviestas", 4.99)
#
# shopingcart = ShoppingCart()
# shopingcart.add_product(prod)
# shopingcart.add_product(prod1)
# shopingcart.add_product(prod2)
# print()
# for product in shopingcart.products:
#     product.display_info()
#     print()
#
# total_price = shopingcart.calculate_total_price()
# print(f"Bendra kaina {total_price} $")
# print()
#
# shopingcart.remove_product(prod)
#
# total_price = shopingcart.calculate_total_price()
# print(f"Nauja bendra kaina {total_price} $")
# print()


# SET----------------GET-------------------------------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def get_name (self):
#         return self.name
#
#     def set_name (self, name):
#         self.name = name
#
#     def get_age (self):
#         return self.age
#
#     def set_age (self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             print("Amžius negi būti neigemas")
#
# person = Person("Jonas", 15)
#
# print("Persona ", person.get_name())
# print("Amzius ", person.get_age())
#
# person.set_name("Petras")
# person.set_age(20)
#
# print("New Persona ", person.get_name())
# print("New Amzius ", person.get_age())
#
#
# person.set_name("Vaidas")
# person.set_age(30)
#
# print("Neww name ", person.get_name())
# print("Neww age ", person.get_age())

