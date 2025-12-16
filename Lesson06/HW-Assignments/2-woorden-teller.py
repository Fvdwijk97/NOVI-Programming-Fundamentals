# ==========================================
# Programmeer een applicatie die telt hoeveel woorden er in een zin staan.
# Bonus: maak het mogelijk om een zin in te geven en het aantal woorden te tellen.
# ==========================================

zin = input("Schrijf een zin: ")
gesplitste_zin = [word for word in zin.split(" ")]

print(f"Het aantal woorden in de zin: {len(gesplitste_zin)} woorden")
