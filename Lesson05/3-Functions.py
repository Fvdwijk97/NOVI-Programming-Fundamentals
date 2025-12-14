# OPGAVEN EDHUB
# ==========================================
# Opgave 1:
# Doe een functieaanroep van bereken_inhoud_cilinder() waarbij alleen de waarde van de hoogte als argument wordt
# meegegeven en voor de straal de defaultwaarde wordt gebruikt.
# ==========================================

PI = 3.14

def bereken_inhoud_cilinder(straal=1, hoogte=2):
    """"Inhoud van een cilinder berekenen"""
    inhoud = PI * hoogte * straal
    return(inhoud)

print(bereken_inhoud_cilinder(hoogte = 3))

# ==========================================
# OPGAVEN GITHUB
# ==========================================
# Voorbeeld Opdracht
# Schrijf een functie die de tekst “Hello, World!” print. Roep vervolgens de functie aan.
# ==========================================

def print_hello_world():
    print('Hello, World!')

print_hello_world()  # Uitkomst: Hello, World!

# ==========================================
# Opdracht 1:
# Print de tafel van 5 met behulp van een for-loop en een functie (genaamd 'print_tafel_regel').
# De factor en for-loop zijn al gegeven. Schrijf de functie om de regel van de tafel te printen.
#
# Verwachte uitkomst:
# 1  x  5  =  5
# 2  x  5  =  10
# 3  x  5  =  15 enz.
# ==========================================

def print_tafel_regel(getal):
    """Tafel van een getal afdrukken en berekenen"""
    for num in range(1, 11):
        print(num * getal)

factor = 5
print_tafel_regel(factor)

# ==========================================
# Opdracht 2:
# Maak een dobbelsteen met de volgende deelopdrachten.
#
# Opdracht 2a:
# Maak met behulp van de bibliotheek (library) 'random' een functie die een willekeurig getal tussen 1 en 6 genereert.
# Zorg dat de functie twee argumenten ontvangt, namelijk 'min' en 'max'. Voor het minimum (1) en maximum (6).
# Voer de functie 10 keer uit (met een for-loop). Als het willekeurige getal is gegenereert print je het getal.
#
# Opdracht 2b;
# Maak een variabele aan 'aantal_keer_zes' en zet deze op 0. Schrijf een functie die aan het eind print hoe vaak er een 6 is gegooid.
# De variabele 'aantal_keer_zes' moet in de print statement worden gebruikt.
#
# Verwachte uitkomst (voorbeeld):
# 3 7 2 6 1 4 5 6 2 1
# Er is 2 keer een 6 gegooid
# ==========================================

import random

def number_generator(min, max):
    """Generating random numbers"""
    random_num = random.randrange(min, max)
    return(random_num)

aantal_keer_zes = 0

for x in range(1, 11):
    number = number_generator(1, 7)
    print(number)
    if number == 6:
        aantal_keer_zes =+ 1

print(f"Er is {aantal_keer_zes} keer een 6 gegooid.")

# ==========================================
# Opdracht 3:
# Omrekenen van Fahrenheit naar Celsius. Gegeven zijn temperaturen van drie steden in Fahrenheit.
#
# Schrijf een functie die de temperatuur in Fahrenheit ontvangt als argument en deze omrekent naar Celsius.
# De formule voor de conversie is als volgt: celsius = (fahrenheit - 32) * 5/9
# Schrijf ook een functie die de temperatuur afrond in hele getallen.
# print de temperatuur in Celsius afgerond op hele getallen.
#
# Verwachte uitkomst:
# 18
# 24
# 40
# ==========================================

def fahr_to_celcius(fahr):
    """Graden omrekenen van Fahrenheit naar Celsius"""
    celsius = round((fahr - 32) * (5 / 9))
    return(celsius)

temp_in_fahr_stockholm = 65
temp_in_fahr_sydney = 75
temp_in_fahr_cairo = 104

print(f"De temperatuur in Stockholm: {fahr_to_celcius(temp_in_fahr_stockholm)}C")
print(f"De temperatuur in Sydney: {fahr_to_celcius(temp_in_fahr_sydney)}C")
print(f"De temperatuur in Caïro: {fahr_to_celcius(temp_in_fahr_cairo)}C")