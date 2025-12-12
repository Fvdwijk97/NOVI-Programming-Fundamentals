# ==========================================
# Schrijf een programma dat een gebruiker om een wachtwoord vraagt. De gebruiker heeft maximaal 3 pogingen om het juiste wachtwoord in te voeren. Als het juiste wachtwoord is ingevoerd, print je een succesbericht en beëindig je de loop. Als de gebruiker 3 pogingen fout invoert, geef je een bericht dat de toegang is geweigerd.
#
# Stappenplan:
#
# 1. Stel een vast wachtwoord in (bijvoorbeeld: "python123"), door daar een variabele voor te maken.
# 2. Vraag de gebruiker om het wachtwoord in te voeren.
# 3. Gebruik een while-loop om de gebruiker maximaal 3 kansen te geven om het juiste wachtwoord in te voeren.
# 4. Als de gebruiker het juiste wachtwoord invoert, beëindig dan de loop met een succesbericht.
# 5. Als de gebruiker na 3 pogingen nog steeds het verkeerde wachtwoord invoert, geef een foutmelding.
# ==========================================

wachtwoord = "python123"
pogingen = 3

while True:
    input_ww = input("Voer uw wachtwoord in: ")
    if input_ww == wachtwoord:
        print("U wordt nu ingelogd.")
        break
    elif input_ww != wachtwoord:
        pogingen -= 1
        print(f"U heeft het verkeerde wachtwoord ingevoerd. U heeft nog {pogingen} pogingen.")
        print()
        if pogingen < 1:
            print("De toegang is geblokkeerd.")
            break