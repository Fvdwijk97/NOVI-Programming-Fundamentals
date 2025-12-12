# ==========================================
# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.
# ==========================================

prijs_pizza_S = 15
prijs_pizza_M = 20
prijs_pizza_L = 25

bestelling = input("Kies de maat van uw pizza (S, M of L): ")
extra_pepperoni = input("Wilt u extra pepperoni?: ")
extra_kaas = input("Wilt u extra extra kaas?: ")

if bestelling == "S".upper():
    prijs = prijs_pizza_S
    if extra_pepperoni == "ja".lower():
        prijs += 2
elif bestelling == "M".upper():
    prijs = prijs_pizza_M
    if extra_pepperoni == "ja".lower():
        prijs += 3
elif bestelling == "L".upper():
    prijs = prijs_pizza_L
    if extra_pepperoni == "ja".lower():
        prijs += 3

if extra_kaas == "ja".lower():
    prijs += 1

print(f"Dat wordt dan ${prijs}, alstublieft")

