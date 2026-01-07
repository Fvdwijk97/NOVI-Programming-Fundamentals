# ==========================================
# OPDRACHT - NAMEN
# Maak een functie die een lijst met namen kan ontvangen. De functie zorgt vervolgens dat de namen uit de lijst met een
# hoofdletter beginnen. De items moeten gescheiden worden door een komma, en de laatste twee door 'en'.
# Voorbeeld input: ["mark", "elwyn", "nova", "frans"]
# Voorbeeld output: "Mark, Elwyn, Nova en Frans"
# ==========================================

def names(lijst_namen):
    print('"', end='')
    for name in lijst_namen:
        if name != lijst_namen[-1]:
            print(f"{name.capitalize()}", end=', ')
        else:
            print(f"en {name.capitalize()}", end='"')

namen = ["felicia", "mayank", "patricia", "rudy", "nirmala", "archana", "sumeet"]

names(namen)