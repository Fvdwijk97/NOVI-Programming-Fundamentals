# ==========================================
# Gegeven zijn 3 lijsten met letters, nummers en symbolen.
# Schrijf een applicatie die de gebruiker vraagt hoeveel letters, nummers en symbolen het ww moet bevatten.
# De applicatie moet obv input van de gebruiker een willekeurig wachtwoord genereren.
#
# 1. Genereer een wachtwoord in een vooraf bepaalde volgorde: letters, nummers, symbolen.
# 2. Genereer een wachtwoord in een willekeurige volgorde, dus letters, nummers en symbolen door elkaar.
# ==========================================


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']

import random

aantal_letters = int(input("Hoeveel letters wil je in je ww?: "))
aantal_nummers = int(input("Hoeveel nummers wil je in je ww?: "))
aantal_symbolen= int(input("Hoeveel symbolen wil je in je ww?: "))
print()

ww = "" # opdr 1
ww_mixing = [] # Opdr 2
ww_shuffled = "" # Opdr 2

for aantal in range(aantal_letters):
    letter = random.choice(letters)
    ww += letter
    ww_mixing.append(letter)

for aantal in range(aantal_nummers):
    nummer = random.choice(numbers)
    ww += nummer
    ww_mixing.append(nummer)

for aantal in range(aantal_symbolen):
    symbool = random.choice(symbols)
    ww += symbool
    ww_mixing.append(symbool)

# Opdr 2
random.shuffle(ww_mixing)

for x in ww_mixing:
    ww_shuffled += x

# Output
print(f"Wachtwoord 'simpele' generator is: {ww}")
print(f"Wachtwoord 'moeilijke'generator is: {ww_shuffled}")