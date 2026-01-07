from user_data import user

def scheiding():
    print("\n", 20 * "-", end="\n\n")

def uber_menu(lijst):
    print("Kies het type Uber:")
    for num, option in lijst:
        for uber, price in option.items():
            print(f"{num}. {uber} - {price:.2f} euro per km")
    print()

def uber_kiezen(lijst):
    while True:
        get_user_choice = input("Voer het nummer van uw keuze in: ")
        if get_user_choice != "1" and get_user_choice != "2" and get_user_choice != "3":
            print("U heeft geen geldige keuze gemaakt. Probeer het nog eens.")
            scheiding()
        else:
            break
    for num, option in lijst:
        for uber in option.keys():
            if get_user_choice == num:
                chosen_uber = uber
    return chosen_uber

def voorkeur_opslaan(chosen_uber):
    while True:
        voorkeur_opslaan = input("Wilt u de gekozen uber opslaan als voorkeur voor volgende ritten? ja/nee: ")
        print()
        if voorkeur_opslaan.lower() == "ja":
            user["Voorkeur"] = chosen_uber
            break
        elif voorkeur_opslaan.lower() == "nee":
            break
        else:
            print("U heeft geen geldige keuze gemaakt. Voer in 'ja' of 'nee'.")

def get_distance():
    distance = int(input("Voer het aantal kilometers van uw rit in: "))
    return distance

def rit_bevestiging(chosen_uber, distance, total_cost):
    print("RIT BEVESTIGD")
    print(f"U heeft gekozen voor {chosen_uber}. De kosten voor uw rit van {distance} km zijn {total_cost:.2f} euro.")

def calc_total_cost(price_list, users_choice, distance_km):
    for option in price_list:
        for key, value in option[1].items():
            if users_choice == key:
                price_per_km = value
    total_cost = distance_km * price_per_km
    return total_cost

