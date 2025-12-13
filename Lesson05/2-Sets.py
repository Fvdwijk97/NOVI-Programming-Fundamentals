# OPGAVEN EDHUB
# ==========================================
# Opgave 1:
# Gegeven zijn de sets kleuren1 en kleuren2.
# Bepaal zelf het verschil van kleuren1 en kleuren2 met behulp van de methode difference().
# De volgorde van de verzamelingen is van belang voor het verschil.
# ==========================================

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}

kleuren3 = kleuren1.difference(kleuren2)
print(kleuren3)

#of

kleuren4 = kleuren1 - kleuren2
print(kleuren4)

# ==========================================
# Opgave 2:
# Bepaal zelf het symmetrisch verschil van kleuren1 en een lijst met alle kleuren die in kleuren2 voorkomen met behulp
# van de methode symmetric_difference().
# ==========================================

kleuren2_list = list(kleuren2)
kleuren5 = kleuren1.symmetric_difference(kleuren2_list)

print(kleuren5)

# ==========================================
# OPGAVEN GITHUB
# ==========================================
# Voorbeeld Opdracht:
# Gegeven is een set met de getallen 1, 2 en 3.
# Voeg het getal 1 toe aan de set en daarna het getal 4.
#
# Print de set 'getallen'.
# Het getal 1 stond al in de set, dus wordt niet nogmaals toegevoegd. Het getal 4 wordt wel toegevoegd.
# ==========================================

getallen = {1, 2, 3}

getallen.add(1)
getallen.add(4)

print('getallen: ', getallen)  # Het resultaat is: {1, 2, 3, 4}

# ==========================================
# Opgave 1:
# Gegeven is de verzameling {3, 44, 17, 23, 58, 9, 36}
# Voer de volgende opdrachten uit:
# - Voeg de value 27 aan de verzameling toe.
# - Verwijder de value 23 uit de verzameling.
# - Druk alle values in de verzameling tussen 20 en 50 af. Gebruik hiervoor een for loop.
#
# Verwachte uitkomst: 36, 27, 44
# ==========================================

verzameling = {3, 44, 17, 23, 58, 9, 36}

verzameling.add(27)
verzameling.remove(23)

verzameling2 = {number for number in verzameling if number > 20 and number < 50}
print(verzameling2)

# Óf:

verzameling3 = set()

for number in verzameling:
    if number > 20 and number < 50:
        verzameling3.add(number)

print(verzameling3)

# ==========================================
# Opgave 2:
# Gegeven zijn de verzamelingen {red, blue, green} en {yellow, blue, green}
# Zoek uit met behulp van wiskundige verzamelingsoperatoren of methodes:
# a Welke kleur zit wel in verzameling_kleuren_1 maar niet in verzameling_kleuren_2?
# b Welke kleuren zitten niet in beide sets? ('red' en 'yellow')
#
# Print de resultaten.
# ==========================================

verzameling_kleuren_1 = {'red', 'blue', 'green'}
verzameling_kleuren_2 = {'yellow', 'blue', 'green'}

a = verzameling_kleuren_1.difference(verzameling_kleuren_2) # Óf:
a2 = verzameling_kleuren_1 - verzameling_kleuren_2 # Óf:
verzameling_kleuren_1 -= verzameling_kleuren_2

print(a)
print(a2)
print(verzameling_kleuren_1)

b = verzameling_kleuren_1.symmetric_difference(verzameling_kleuren_2) # Óf:
b2 = verzameling_kleuren_1 ^ verzameling_kleuren_2 # Óf:
verzameling_kleuren_1 ^= verzameling_kleuren_2

print(b)
print(b2)
print(verzameling_kleuren_1)

# ==========================================
# Opgave 3:
# Gegeven zijn de verzamelingen {11, 22, 33} en {5, 11, 16, 22}
# Gebruik wiskundige verzamelingsoperatoren om de volgende verzamelingen te printen:
# c    {33}
# d    {5, 16}
# e    {5, 11, 16, 22, 33}
# f    {11, 22}
#
# (LET OP: De volgorde van de values in de verzamelingen is niet belangrijk, die kan namelijk veranderen omdat een set unordered is.)
# ==========================================

verzameling1 = {11, 22, 33}
verzameling2 = {5, 11, 16, 22}

c = verzameling1 - verzameling2
d = verzameling2 - verzameling1
e = verzameling1 | verzameling2
f = verzameling1 & verzameling2

print(c)
print(d)
print(e)
print(f)