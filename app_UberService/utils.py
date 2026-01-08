from user_data import user

def separator():
    """Zorgt voor goede opmaak en scheiding functionaliteiten tijdens gebruik app"""
    print("\n", 20 * "-", end="\n\n")

def generate_uber_menu(lijst):
    """Genereert het keuzemenu voor type ubers met bijbehorende prijzen
    :param: lijst van tuples. Eerste waarde is nummering, tweede waarde is dict {Uber : prijs}.
    """
    print("Kies het type Uber:")
    for num, option in lijst:
        for uber, price in option.items():
            print(f"{num}. {uber} - {price:.2f} euro per km")
    print()

def parse_uber_choice(lijst):
    """Vraagt gebruiker een uber te kiezen obv keuzemenu. Haalt obv ingevoerd nummer het bijbehorende
    type uber op en slaat deze op in 'chosen_uber'. Incl input validatie.
    :param: lijst van tuples. Eerste waarde is nummering, tweede waarde is dict {Uber : prijs}."""
    while True:
        get_user_choice = input("Voer het nummer van uw keuze in: ")
        if get_user_choice != "1" and get_user_choice != "2" and get_user_choice != "3":
            print("U heeft geen geldige keuze gemaakt. Probeer het nog eens.")
            separator()
        else:
            break
    for num, option in lijst:
        for uber in option.keys():
            if get_user_choice == num:
                chosen_uber = uber
    return chosen_uber

def safe_preference(chosen_uber):
    """Geeft gebruiker mogelijkheid gekozen uber op te slaan als voorkeur, of dit over te slaan.
    Incl input validatie.
    :param: str met gebruikers keuze voor uber."""
    while True:
        user_preference = input("Wilt u de gekozen uber opslaan als voorkeur voor volgende ritten? ja/nee: ")
        print()
        if user_preference.lower() == "ja":
            user["Voorkeur"] = chosen_uber
            break
        elif user_preference.lower() == "nee":
            break
        else:
            print("U heeft geen geldige keuze gemaakt. Voer in 'ja' of 'nee'.")

def get_distance():
    """Vraagt gebruiker het aantal km's."""
    distance = int(input("Voer het aantal kilometers van uw rit in: "))
    return distance

def calc_total_cost(price_list, users_choice, distance_km):
    """Berekent de totale prijs obv gekozen dienst en afstand in km"""
    for option in price_list:
        for key, value in option[1].items():
            if users_choice == key:
                price_per_km = value
    total_cost = distance_km * price_per_km
    return total_cost

def confirm_ride(chosen_uber, distance, total_cost):
    """Opmaak voor output gekozen rit incl gekozen uber, aantal km's en totale prijs.
    :chosen_uber: str met gebruikers keuze voor uber
    :distance: int met afstand in km, ingevoerd door gebruiker
    :total_cost: totale prijs obv gekozen dienst en afstand"""
    print("RIT BEVESTIGD")
    print(f"U heeft gekozen voor {chosen_uber}. De kosten voor uw rit van {distance} km zijn {total_cost:.2f} euro.")
