# ==========================================
# Les 1 - Opdracht
# Schrijf een verhaal van 20 - 50 woorden, waarin je minimaal 5 variabelen zet die
# de gebruiker zelf moet invullen.
# Vraag de gebruiker om input voor die variabelen.
# ==========================================

naam = input("Hoe heet je?: ")
naam_vriend = input("Hoe heet je vriend(in)?: ")
activiteit = input("Wat heb je altijd al eens willen doen?: ")
restaurant = input("Waar wil je uiteten?: ")
gerecht = input("Wat wil je eten?: ")
drinken = input("Wat wil je drinken?: ")
toetje = input("Toetje?: ")

print(f"{naam} verveelt zich en besluit iets leuks met {naam_vriend} te doen.\n"
      f"{naam_vriend} vertelt dat altijd al eens zou willen {activiteit}.\n"
      f"Ze besluiten het uit te proberen en na afloop gaan ze uiteten bij {restaurant}.\n"
      f"Ze bestellen allebei {gerecht}, {drinken} en {toetje}.")

