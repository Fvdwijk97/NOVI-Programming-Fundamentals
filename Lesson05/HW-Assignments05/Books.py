# Boeken geleend door Groep 1
groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code", "Twilight",
          "De Vijfde Golf", "Harry Potter", "De Hobbit"]

# Boeken geleend door Groep 2
groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games", "Gone Girl",
          "Twilight", "De Hobbit"]

# 1 - Maak 2 sets van de boeken die door Groep 1 en Groep 2 zijn geleend:
set_groep1 = set(groep1)
set_groep2 = set(groep2)

print(f"Boeken die door groep 1 geleend zijn: {set_groep1}")
print(f"Boeken die  door groep 2 geleend zijn: {set_groep2}")
print()

# 2 - Gemeenschappelijke boeken
gemeenschappelijke_boeken = set_groep1.intersection((set_groep2))
print(f"Boeken die door beide groepen zijn geleend: {gemeenschappelijke_boeken}")
print()

# 3 - Boeken geleend door slechts één groep:
uniek_groep1 = set_groep1.difference(groep2)
uniek_groep2 = set_groep2.difference(groep1)

print(f"Boeken die alléén door groep 1 geleend zijn: {uniek_groep1}")
print(f"Boeken die alléén door groep 2 geleend zijn: {uniek_groep2}")
print()

# 4 - Aantal geleende keren per boek per groep:

dicts = [(groep1, {}), (groep2, {})]
for groep, dict in dicts:
    for boek in groep:
        if boek not in dict:
            dict[boek] =  1
        else:
            dict[boek] += 1

print(f"Groep 1 aantal keer geleende boeken: {dicts[0][1]}")
print(f"Groep 1 aantal keer geleende boeken: {dicts[1][1]}")

# 5 Welk boek is het meeste geleend in groep 1 en groep 2:

count1 = ("", 0)
count2 = ("", 0)

for book, count in dicts[0][1].items():
    if count1[1] < count:
        count1 = (book, count)

for book, count in dicts[1][1].items():
    if count2[1] < count:
        count2 = (book, count)

print("Groep 1 count: ", count1)
print("Groep 2 count: ", count2)
