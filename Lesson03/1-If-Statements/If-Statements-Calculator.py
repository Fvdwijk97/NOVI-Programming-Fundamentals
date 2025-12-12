# ==========================================
# Opgave 1 - Calculator:
# Schrijf een simpele rekenmachine. De gebruiker moet twee getallen en een operatie invoeren.
# Het programma moet de berekening uitvoeren en het resultaat printen.

# Het programma moet de volgende operaties ondersteunen: +, -, *, /
# Als de gebruiker een ongeldige operatie invoert, moet het programma "Invalid operation" printen.
# ==========================================

optellen = "+"
aftrekken = "-"
delen = "/"
keer = "*"

while True:
    getal1 = float(input("voer het eerste getal in: "))
    getal2 = float(input("voer het tweede getal in: "))
    operatie = input("voer een operatie in (+, -, / óf *): ")

    if operatie != optellen and operatie != aftrekken and operatie != delen and operatie != keer:
        print("invalid operation")
    elif operatie == optellen:
        print(f"The result is: {getal1 + getal2}")
    elif operatie == aftrekken:
        print(f"The result is: {getal1 - getal2}")
    elif operatie == delen:
        print(f"The result is: {getal1 / getal2}")
    elif operatie == keer:
        print(f"The result is: {getal1 * getal2}")
    print(50 * "-")

