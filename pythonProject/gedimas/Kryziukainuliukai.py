# TicTacToe
# class TicTacToe:
#     def __init__(self):
#         self.board = [" "for _ in range(9)]
#         self.current_player = "X"
#
#     def print_boar(self):
#         print("----------")
#         for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
#             print("|", end="")
#             for cell in row:
#                 print(f"{cell} |", end="")
#             print("\n----------")
#
#     def make_move(self, position):
#         if self.board[position] == " ":
#             self.board[position] = self.current_player
#             self.current_player = "O" if self.current_player == "X" else "X"
#         else:
#             print("Invalid move. Try again")
#
#     def check_winner(self):
#         winning_combinations = [
#              [0, 1, 2], [3, 4, 5], [6, 7, 8],
#              [0, 3, 6], [1, 4, 7], [2, 5, 8],
#              [0, 4, 8], [2, 4, 6]
#              ]
#         for combo in winning_combinations:
#              a, b, c = combo
#              if self.board[a] == self.board[b] == self.board[c] != " ":
#                  return self.board[a]
#         if " " not in self.board:
#             return "Tie"
#         return None
#
#     def play_game(self):
#         print("Wellcome")
#         self.print_boar()
#
#
#         while True:
#             position= int(input("player" + self.current_player + "make your move(0-8):  "))
#             self.make_move(position)
#             self.print_boar()
#             winner = self.check_winner()
#             if winner:
#                 if winner == "Tie":
#                     print("It's a TIE")
#                 else:
#                     print("Pleayer " + winner + " WINNS")
#                 break
#
#
# game = TicTacToe()
# game.play_game()
#
# def sudeti(a, b):
#     return a + b
#
# def atimti(a, b):
#     return a - b
#
# def dauginti(a, b):
#     return a * b
#
# def dalinti(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("Dalyba iš nulio negalima!")
#
# print("Skaiciuotuvas")
# print("--------------")
#
# while True:
#     print("Pasirinkite veiksmą:")
#     print("1. Sudėti")
#     print("2. Atimti")
#     print("3. Dauginti")
#     print("4. Dalinti")
#     print("5. Baigti")
#
#     veiksmas = input("Įveskite veiksmo numerį: ")
#
#     if veiksmas == "5":
#         print("Programa baigta.")
#         break
#
#     skaicius1 = float(input("Įveskite pirmą skaičių: "))
#     skaicius2 = float(input("Įveskite antrą skaičių: "))
#
#     if veiksmas == "1":
#         rezultatas = sudeti(skaicius1, skaicius2)
#         print("Rezultatas:", rezultatas)
#     elif veiksmas == "2":
#         rezultatas = atimti(skaicius1, skaicius2)
#         print("Rezultatas:", rezultatas)
#     elif veiksmas == "3":
#         rezultatas = dauginti(skaicius1, skaicius2)
#         print("Rezultatas:", rezultatas)
#     elif veiksmas == "4":
#         rezultatas = dalinti(skaicius1, skaicius2)
#         if rezultatas is not None:
#             print("Rezultatas:", rezultatas)
#     else:
#         print("Neteisingas veiksmo numeris. Bandykite dar kartą.")