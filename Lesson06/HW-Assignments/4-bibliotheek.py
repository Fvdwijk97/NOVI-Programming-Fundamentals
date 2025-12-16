# ==========================================
#Je gaat een bibliotheekprogramma maken. Boeken bevatten volgende info: Naam, Auteur, Genre, Publicatiejaar.
#
# Het programma moet de volgende functionaliteiten hebben:
# - De gebruiker moet boeken kunnen toevoegen aan de bibliotheek.
# - De gebruiker moet een lijst van alle boeken in de bibliotheek kunnen opvragen.
# - De gebruiker moet een lijst van alle boeken in een bepaald genre kunnen opvragen.
# - De gebruiker moet het programma kunnen stoppen.
# ==========================================

# BIBLIOTHEEK
bibliotheek = {
    "The Silent Patient": {
        "auteur": "Alex Michaelides",
        "genre": "Thriller",
        "publicatiejaar": 2019
    },
    "Where the Crawdads Sing": {
        "auteur": "Delia Owens",
        "genre": "Fictie",
        "publicatiejaar": 2018
    },
    "The Night Circus": {
        "auteur": "Erin Morgenstern",
        "genre": "Fantasy",
        "publicatiejaar": 2011
    },
    "Educated": {
        "auteur": "Tara Westover",
        "genre": "Memoir",
        "publicatiejaar": 2018
    },
    "Circe": {
        "auteur": "Madeline Miller",
        "genre": "Fantasy",
        "publicatiejaar": 2018
    }
}

# ==========================================
# FUNCTIONS
# ==========================================

def doorgaan_of_stoppen():
    """Bepaald of gebruiker (nog) een actie wil uitvoeren of wilt stoppen"""
    doorgaan_of_stoppen = input("\nWilt u terug naar het keuze menu (ja/nee)?: ")
    if doorgaan_of_stoppen.lower() == "ja":
        return True
    elif doorgaan_of_stoppen.lower() == "nee":
        return print("\nU verlaat de bibliotheek, tot ziens!")

def keuze_menu1():
    """Bepaald of gebruiker wil toevoegen, inzien of stoppen"""
    kiezen = True
    while True:
        gekozen_optie = input("\na. Ik wil een boek toevoegen\n"
                        "b. Ik wil een lijst met boeken inzien\n"
                        "c. Ik wil het programma verlaten\n"
                        "Kies één van bovenstaande acties: ")
        if (len(gekozen_optie.lower()) > 2 and gekozen_optie in "a. ik wil een boek toevoegen") or gekozen_optie.lower() == "a":
            kiezen = False
            return "a"
        elif (len(gekozen_optie.lower()) > 2 and gekozen_optie in "b. ik wil een lijst met boeken inzien") or gekozen_optie.lower() == "b":
            kiezen = False
            return "b"
        elif (len(gekozen_optie.lower()) > 2 and gekozen_optie in "c. ik wil het programma verlaten") or gekozen_optie.lower() == "c":
            kiezen = False
            return "c"
        else:
            print("U heeft géén geldige keuze gemaakt, probeer het nog eens.")
            kiezen = True

def keuze_menu2():
    """Bepaald wat voor lijst boeken de gebruiker wil inzien"""
    kiezen = True
    while kiezen == True:
        gekozen_optie = input("\nWat wilt u inzien?\n"
              "a. Alle boeken\n"
              "b. Zoeken op genre\n"
              "Uw keuze: ")
        if (len(gekozen_optie.lower()) > 2 and gekozen_optie.lower() in "a. alle boeken") or gekozen_optie.lower() == "a":
            kiezen = False
            return "a"
        elif (len(gekozen_optie.lower()) > 2 and gekozen_optie.lower() in "b. zoeken op genre") or gekozen_optie.lower() == "b":
            kiezen = False
            return "b"
        else:
            print("U heeft géén geldige keuze gemaakt, probeer het nog eens.")
            kiezen = True

# ==========================================
# PROGRAMMA
# ==========================================

print("Welkom bij de bibliotheek!")

doorgaan = True  #Zorgt dat programma door gaat, totdat gebruiker aangeeft klaar te zijn
while doorgaan == True:
    gebruikers_keuze = keuze_menu1()  #Gebruiker moet aangeven welke actie uitgevoerd moet worden

# Gebruiker wilt boek toevoegen, True-flag zodat gebruiker kan blijven toevoegen totdat hij/zij klaar is
    if gebruikers_keuze == "a":
        toevoegen = True
        while toevoegen == True:
            gebruiker_voegt_toe = (input("\nVul titel, auteur, genre, publicatiedatum in (gescheiden door komma's): "))
            gebruiker_voegt_toe = [antw.strip("") for antw in gebruiker_voegt_toe.split(",")]
            bibliotheek[gebruiker_voegt_toe[0]] = {"auteur": gebruiker_voegt_toe[1],
                                                   "genre": gebruiker_voegt_toe[2],
                                                   "publicatiejaar": gebruiker_voegt_toe[3]}
            voltooid = input("Wilt u nog een boek toevoegen? (ja/nee): ")
            if voltooid.lower() == "ja":
                toevoegen = True
            else:
                toevoegen = False
        doorgaan = doorgaan_of_stoppen() # Als klaar met toevoegen: terug naar hoofdmenu of programma verlaten

# Gebruiker wilt boeken inzien, kan kiezen tussen alle boeken of alleen binnen genre
    elif gebruikers_keuze == "b":
        gebruiker_wil_inzien = keuze_menu2()

        if gebruiker_wil_inzien == "a":  # Gebruiker wilt alle boeken inzien
            print(f"\n{50 * "*"}")
            print("Alle boeken in onze bibliotheek:")
            print(50 * "*")
            for boek, info in bibliotheek.items():
                print(f"\n{boek}")
                for key, value in info.items():
                    print(f"{key}: {value}")

        elif gebruiker_wil_inzien == "b": # Gebruiker wilt alle boeken binnen bepaald genre inzien
            genre_opzoeken = input("\nWelk genre wilt u inkijken?: ")
            genre_lijst = {}
            print(f"\n{50 * "*"}")
            print(f"Alle boeken met het genre '{genre_opzoeken.capitalize()}':")
            print(50 * "*")
            for boek, info in bibliotheek.items():
                if genre_opzoeken.capitalize() in info["genre"]:
                    genre_lijst[boek] = info
            for boek, info in genre_lijst.items():
                print()
                print(boek)
                for key, value in info.items():
                    print(f"{key}: {value}")

        doorgaan = doorgaan_of_stoppen() # Optie om terug te gaan naar hoofdmenu of programma verlaten

# Gebruiker wilt programma verlaten
    elif gebruikers_keuze == "c":
        print("\nU verlaat de bibliotheek, tot ziens!")
        doorgaan = False





