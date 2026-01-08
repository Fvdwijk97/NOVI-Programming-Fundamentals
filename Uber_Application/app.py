import utils as u
from user_data import user

# Lijst ubers/prijzen en functionaliteiten
uber_options = [("1", {"Uber Black": 2.00}), ("2", {"Uber Van": 3.50}), ("3", {"Uber X": 1.50})]
keuze_menu = ["Naam wijzigen", "Voorkeur aanpassen", "Rit boeken", "Rit geschiedenis inzien", "Applicatie sluiten"]

# Start applicatie
print("Welkom bij de Uber App!\n")
user["Naam"] = input("Voer uw naam in: ").capitalize()
u.scheiding()

# Keuzemenu ubers/bijbehorende prijzen, en gebruikerskeuze opslaan in 'chosen_uber'
u.uber_menu(uber_options)
chosen_uber = u.uber_kiezen(uber_options)

# Gebruiker kan kiezen of ze gekozen uber willen opslaan als 'default'. Met input validatie
u.voorkeur_opslaan(chosen_uber)

# Gebruiker voert aantal km's in en totale prijs wordt berekend obv gekozen uber en afstand
distance = u.get_distance()
total_cost = u.calc_total_cost(uber_options, chosen_uber, distance)

# Geboekte rit incl prijs bevestigen aan gebruiker en opgeslagen in geschiedenis
print("\n", 20 * "-", end="\n\n")
print("RIT BEVESTIGD")
print(f"U heeft gekozen voor {chosen_uber}. De kosten voor uw rit van {distance} km zijn {total_cost:.2f} euro.")

user["Geschiedenis"].append({"Uber": chosen_uber, "Afstand": distance, "Prijs": total_cost})

# Gebruiker komt in keuzemenu met verschillende functionaliteiten app en maakt een keuze. Met input validatie
while True:
    u.scheiding()
    print("KEUZE MENU")
    for i, keuze in enumerate(keuze_menu, 1):
        print(f"{i}. {keuze}")
    chosen_action = input("\nVoer het nummer van uw keuze in: ")

    if chosen_action == "1":
        u.scheiding()
        print("NAAM WIJZIGEN")
        user["Naam"] = input("Voer uw naam in: ").capitalize()
        print("\nUw naam is opgeslagen!")

    elif chosen_action == "2":
        u.scheiding()
        print("UBER VOORKEUR WIJZIGEN\n")
        print(f"Uw huidige voorkeur: {user["Voorkeur"]}\n")
        u.uber_menu(uber_options)
        user["Voorkeur"] = u.uber_kiezen(uber_options)

    elif chosen_action == "3":
        u.scheiding()
        print("RIT BOEKEN")
        if user["Voorkeur"]:
            while True:
                print(f"Uw voorkeur is: {user["Voorkeur"]}. Wilt u verder gaan (1) of wilt u een andere dienst kiezen (2)?\n")
                voorkeur_gebruiken = input("Voer het nummer van uw keuze in: ")
                print()
                if voorkeur_gebruiken == "1":
                    chosen_uber = user["Voorkeur"]
                    break
                elif voorkeur_gebruiken == "2":
                    u.uber_menu(uber_options)
                    chosen_uber = u.uber_kiezen(uber_options)
                    u.voorkeur_opslaan(chosen_uber)
                    break
                else:
                    print("\nU heeft geen geldige keuze gemaakt. Probeer het nog eens.\n")
        else:
            u.uber_menu(uber_options)
            chosen_uber = u.uber_kiezen(uber_options)
            u.voorkeur_opslaan(chosen_uber)
        distance = u.get_distance()
        total_cost = u.calc_total_cost(uber_options, chosen_uber, distance)
        u.scheiding()
        u.rit_bevestiging(chosen_uber, distance, total_cost)
        user["Geschiedenis"].append({"Uber": chosen_uber, "Afstand": distance, "Prijs": total_cost})

    elif chosen_action == "4":
        u.scheiding()
        print("RIT GESCHIEDENIS")
        for i, rit in enumerate(user["Geschiedenis"], 1):
            print(f"Rit {i}: {rit["Uber"]}, {rit["Afstand"]}km, {rit["Prijs"]:.2f} euro.")

    elif chosen_action == "5":
        u.scheiding()
        print(f"Tot ziens {user["Naam"]}!")
        break

    else:
        print("U heeft geen geldige keuze gemaakt. Probeer het nog eens.")
