# Lijst van studenten en cijfers aanmaken.
# Input van de gebruiker toevoegen aan de lijst als tuples: [(naam, cijfer), (naam, cijfer)...]

cijfer_lijst = []
aantal_studenten = int(input("Hoeveel studenten hebben de toets gemaakt?: "))

for student in range(aantal_studenten):
    naam_student = input("Student naam: ")
    cijfer_student = float(input("Cijfer van de student: "))
    cijfer_lijst.append((naam_student.capitalize(), cijfer_student))

# ----------------------------------------------------------------------------------------
# De lijst sorteren op cijfers van laag naar hoog en de gesorteerde lijst printen.

cijfer_lijst.sort(key=lambda x: x[1])

print()
for x, y in cijfer_lijst:
    print(f"{x} - {y}")

# ----------------------------------------------------------------------------------------
# Gemiddelde van alle cijfers berekenen en printen.
# De beste student printen. Omdat de lijst gesorteerd is, de laatste index selecteren.

gemiddelde = round((aantal_studenten / len(cijfer_lijst)), 1)
print()
print(f"Gemiddelde score: {gemiddelde}")
print(f"De beste student is {cijfer_lijst[-1][0]}, met een {cijfer_lijst[-1][1]}!")
print()

# ------------------------------------------------------------------------------------------
# De gebruiker cijfers laten opzoeken adhv invoer van de studenten naam.
# Fout controle invoer; gebruiker moet ja of nee invullen en anders nog een keer kunnen proberen.
# Fout controle invoer; gebruiker moet de naam correct spellen en ander nog een keer kunnen proberen.
# Invoer moet níet hoofdletter gevoelig zijn.
# Gebruiker moet cijfers kunnen opzoeken van meerdere studenten en aangeven wanneer gebruiker wil stoppen.
# Bij beëindiging programma, begroeting.

opzoeken = input("Wilt u een cijfer opzoeken? ja/nee: ")
while opzoeken.capitalize() != "Ja" and opzoeken.capitalize() != "Nee":
    print("U heeft geen geldig antwoord ingevuld.")
    print()
    opzoeken = input("Wilt u een cijfer opzoeken? ja/nee: ")

while opzoeken.capitalize() == "Ja":
    zoek_naam = input("Van wie wilt u het cijfer inzien?: ")
    print()
    gevonden = False
    for x, y in cijfer_lijst:
        if zoek_naam.capitalize() == x:
            print(f"{x}'s cijfer is: {y}")
            print()
            gevonden = True
            opzoeken = input("Wilt u een cijfer opzoeken? ja/nee: ")
    if not gevonden:
        print(f"Er is geen cijfer bekend van {zoek_naam}")
        print()
        opzoeken = input("Wilt u het nog een keer proberen? ja/nee: ")

print()
print("Tot ziens!")