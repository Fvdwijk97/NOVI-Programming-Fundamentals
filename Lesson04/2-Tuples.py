# ==========================================
# Opgave 1:
# Loop door de tuple en print elk element afzonderlijk
# ==========================================

steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")

for stad in steden:
    print(stad)

# ==========================================
# Opgave 2:
# Combineer de twee tuples tot één nieuwe tuple
# ==========================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)

# ==========================================
# Opgave 3:
# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)
# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element
# ==========================================

tuple4 = (5, "hallo", 6.0, True, False, "nee", 10, "haha", True)

print(tuple4[0])
print(tuple4[2:6])
print(tuple4[-1])

# ==========================================
# Opgave 4:
# Maak een tuple met een naam en een leeftijd
# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)
# Print de uitgepakte variabelen
# ==========================================

tuple5 = ("Felicia", 28)
naam = tuple5[0]
leeftijd = tuple5[1]

print(f"Naam: {naam}")
print(f"Leeftijd: {leeftijd}")

# ==========================================
# Opgave 5:
# ==========================================

variabele1 = ('rood',)
variabele2 = ('geel')

print(type(variabele1))
print(type(variabele2))

# ==========================================
# Opgave 6:
# Declareer twee tuples met de namen ‘tuple_een’ en ‘tuple_twee’.
# tuple_een krijgt de waarden 1, 2 en 3. tuple_twee krijgt de waarden 4, 5 en 6.
# Zorg dat je een tuple krijgt met de waarden 1, 2, 3, 4, 5 en 6. Onthoud dat tuples onveranderlijk zijn.
# ==========================================

tuple_een = (1, 2, 3)
tuple_twee = (4, 5, 6)
combined_tuple = tuple_een + tuple_twee
print(f"combined tuple: {combined_tuple}.")

# ==========================================
# Opgave 7:
# maak een tuple aan met de waarden 'b', 'c', 'a'
# print de waarden van de tuple in de alfabetische volgorde (a, b, c)
# Tip: maak gebruik van de indexen van de tuple
#
# Verwachte uitkomst:  a b c
# ==========================================

tuple1 = ('b', 'c','a')
tuple2 = (tuple1[2], tuple1[0], tuple1[1])

print(tuple2)

# ==========================================
# Opgave 8:
# Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 1 tot en met 5 waarin elk element bestaat uit een tuple die het getal en het bijbehorende kwadraat bevat.
# Gebruik een list comprehension.
#
# Verwachte uitkomst: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# ==========================================

getal_kwadraat_paar = []

for getal in range(5):
    tuple4 = (getal + 1), ((getal + 1) ** 2)
    getal_kwadraat_paar.append(tuple4)

print(getal_kwadraat_paar)

# =========================================
# Opgave 9:
# Maak een tuple genaamd tuple_count met de waarden 1, 2, 3, 4, 5
# Draai de volgorde van de getallen om. Zorg dat je een nieuwe tuple krijgt met de waarden 5, 4, 3, 2, 1
# Tip: Maak gebruik van de reversed() functie
#
# Verwachte uitkomst: (5, 4, 3, 2, 1)
# ==========================================

tuple_count = (1, 2, 3, 4, 5)
tuple_reverse = tuple(reversed(tuple_count))

print(tuple_reverse)