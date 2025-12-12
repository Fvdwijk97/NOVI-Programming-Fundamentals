# ==========================================
# Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent,
# en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.
# Het programma gebruikt een while-loop om de berekening stap voor stap uit te voeren,
# telkens de grootste munt eraf halend totdat het bedrag nul is.
#
# Stappenplan:
#
# 1. Vraag de gebruiker om een bedrag in centen in te voeren (bijvoorbeeld 87).
#       (Bonus: check of de gebruiker niet meer dan 100 invoert)
# 2. Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken.
#    De loop stopt wanneer het bedrag nul is.
# 3. Maak in de while-loop, voor elke munt waarde een (nested) if-statement, waarin je het volgende doet:
#       - Bereken hoevaak die muntwaarde in het bedrag past.
#       - Trek zo vaak de muntwaarde van het bedrag af,
#         zodat de volgende iteratie van de while-loop het aangepast bedrag gebruikt
#       - Print hoeveel munten van deze waarde de gebruiker terug moet krijgen.
#
# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.
# ==========================================

vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

vijftig_munt = 0
twintig_munt = 0
tien_munt = 0
vijf_munt = 0
een_munt = 0

bedrag = int(input("Voer een bedrag in centen in van maximaal 100: "))

while True:
    if bedrag > vijftig_cent:
        vijftig_munt += (bedrag // vijftig_cent)
        bedrag = (bedrag % vijftig_cent)
    elif bedrag > twintig_cent:
        twintig_munt += (bedrag // twintig_cent)
        bedrag = (bedrag % twintig_cent)
    elif bedrag > tien_cent:
        tien_munt += (bedrag // tien_cent)
        bedrag = (bedrag % tien_cent)
    elif bedrag > vijf_cent:
        vijf_munt += (bedrag // vijf_cent)
        bedrag = (bedrag % vijf_cent)
    elif bedrag > een_cent:
        een_munt += (bedrag // een_cent)
        bedrag = (bedrag % een_cent)
    elif bedrag == 0:
        print(f"wisselgeld in munten:\n"
              f"50: {vijftig_munt}x \n"
              f"20: {twintig_munt}x \n"
              f"10: {tien_munt}x \n"
              f"5: {vijf_munt}x \n"
              f"1: {een_munt}x")
        break
