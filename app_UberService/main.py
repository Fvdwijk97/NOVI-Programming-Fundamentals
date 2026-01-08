import utils as u
from user_data import user

# Lijst ubers/prijzen en functionaliteiten
uber_options = [("1", {"Uber Black": 2.00}), ("2", {"Uber Van": 3.50}), ("3", {"Uber X": 1.50})]
main_menu = ["Naam wijzigen", "Voorkeur aanpassen", "Rit boeken", "Rit geschiedenis inzien", "Applicatie sluiten"]

# Start applicatie
print("Welkom bij de Uber App!\n")
user["Naam"] = input("Voer uw naam in: ").capitalize()
u.separator()

# Keuzemenu ubers/bijbehorende prijzen, en gebruikerskeuze opslaan in 'chosen_uber'
u.generate_uber_menu(uber_options)
chosen_uber = u.parse_uber_choice(uber_options)

# Gebruiker kan kiezen of ze gekozen uber willen opslaan als 'default'. Met input validatie
u.safe_preference(chosen_uber)

# Gebruiker voert aantal km's in en totale prijs wordt berekend obv gekozen uber en afstand
distance = u.get_distance()
total_cost = u.calc_total_cost(uber_options, chosen_uber, distance)

# Geboekte rit incl prijs bevestigen aan gebruiker en opgeslagen in geschiedenis
u.separator()
u.confirm_ride(chosen_uber,distance,total_cost)

user["Geschiedenis"].append({"Uber": chosen_uber, "Afstand": distance, "Prijs": total_cost})

# Gebruiker komt in keuzemenu met verschillende functionaliteiten app en maakt een keuze. Met input validatie
while True:
    u.separator()
    print("KEUZE MENU")
    for num, keuze in enumerate(main_menu, 1):
        print(f"{num}. {keuze}")
    chosen_action = input("\nVoer het nummer van uw keuze in: ")

    if chosen_action == "1":
        u.separator()
        print("NAAM WIJZIGEN")
        user["Naam"] = input("Voer uw naam in: ").capitalize()
        print("\nUw naam is opgeslagen!")

    elif chosen_action == "2":
        u.separator()
        print("UBER VOORKEUR WIJZIGEN\n")
        print(f"Uw huidige voorkeur: {user["Voorkeur"]}\n")
        u.generate_uber_menu(uber_options)
        user["Voorkeur"] = u.parse_uber_choice(uber_options)

    elif chosen_action == "3":
        u.separator()
        print("RIT BOEKEN")
        if user["Voorkeur"]:
            while True:
                print(f"Uw voorkeur is: {user["Voorkeur"]}. Wilt u verder gaan (1) of wilt u een andere dienst kiezen (2)?\n")
                use_preference = input("Voer het nummer van uw keuze in: ")
                print()
                if use_preference == "1":
                    chosen_uber = user["Voorkeur"]
                    break
                elif use_preference == "2":
                    u.generate_uber_menu(uber_options)
                    chosen_uber = u.parse_uber_choice(uber_options)
                    u.safe_preference(chosen_uber)
                    break
                else:
                    print("\nU heeft geen geldige keuze gemaakt. Probeer het nog eens.\n")
        else:
            u.generate_uber_menu(uber_options)
            chosen_uber = u.parse_uber_choice(uber_options)
            u.safe_preference(chosen_uber)
        distance = u.get_distance()
        total_cost = u.calc_total_cost(uber_options, chosen_uber, distance)
        u.separator()
        u.confirm_ride(chosen_uber, distance, total_cost)
        user["Geschiedenis"].append({"Uber": chosen_uber, "Afstand": distance, "Prijs": total_cost})

    elif chosen_action == "4":
        u.separator()
        print("RIT GESCHIEDENIS")
        for num, rit in enumerate(user["Geschiedenis"], 1):
            print(f"Rit {num}: {rit["Uber"]}, {rit["Afstand"]}km, {rit["Prijs"]:.2f} euro.")

    elif chosen_action == "5":
        u.separator()
        print(f"Tot ziens {user["Naam"]}!")
        break

    else:
        print("U heeft geen geldige keuze gemaakt. Probeer het nog eens.")
