boodschappenlijst = []

artikel = input("Wat heb je nodig?: ")
hoeveelheid = input("Hoeveel?: ")

while True:
    toevoegen = (hoeveelheid + 'x '), artikel
    toevoegen_joined = "".join(toevoegen)
    boodschappenlijst.append(toevoegen_joined)
    verder_gaan = input("Wil je verder gaan?: ").lower()
    if verder_gaan == "ja":
        artikel = input("Wat heb je nodig?: ")
        hoeveelheid = input("Hoeveel?: ")
    elif verder_gaan == "nee":
        print(f"Jouw boodschappenlijstje: \n{'\n'.join(boodschappenlijst)}")
        break
    else:
        print("je hebt geen geldige keuze gemaakt.")