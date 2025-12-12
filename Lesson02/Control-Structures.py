# ==========================================
# Voorbeeld Opdracht
# Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# ==========================================

a = 3
b = 10

if a > b:
    print(a)
else:
    print(b)

# ==========================================
# Opgave 1:
# Gegeven is een int input getal_1 en getal_2 en drie print methodes. Schrijf een if statement dat controleert of getal1 een veelvoud is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================

getal_1 = int(input("voer een getal in: "))
getal_2 = int(input("voer een getal in: "))

if getal_1 % getal_2 == 0:
    print(f"{getal_1} is een veelvoud van {getal_2}")
elif getal_2 % getal_1 == 0:
    print(f"{getal_2} is een veelvoud van {getal_1}")
else:
    print(f"{getal_1} en {getal_2} zijn geen veelvoud van elkaar.")

# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================

leeftijd = int(input("voer je leeftijd in: "))

if leeftijd < 5:
    print("Toegang is gratis!")
elif leeftijd < 12:
    print("Ticket is 6 euro.")
elif leeftijd < 54:
    print("Ticket is 12 euro.")
else:
    print("Toegang is gratis!")

# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de variabelen num1, num2 en num3 (maak deze variabelen met inputs zelf aan). Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================

input1 = int(input("Vul een getal in: "))
input2 = int(input("Vul nog een getal in: "))
input3 = int(input("Vul nog een getal in: "))

if input1 < input2 and input1 < input3:
    num1 = input1
    if input2 < input3:
        num2 = input2
        num3 = input3
    else:
        num2 = input3
        num3 = input2
elif input2 < input1 and input2 < input3:
    num1 = input2
    if input1 < input3:
        num2 = input1
        num3 = input3
    else:
        num2 = input3
        num3 = input1
elif input3 < input1 and input3 < input2:
    if input1 < input2:
        num2 = input1
        num3 = input2
    else:
        num2 = input2
        num3 = input1

print(num1, num2, num3)

# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0. Schrijf een programma dat herhaaldelijk een getal als input vraagt. Elk getal dat je invoert moet moet worden opgeteld bij het totaal. Als je 0 invoert moet het programma stoppen en met een print statement het totaal en het gemiddelde van de getallen afdrukken (dus totaal / aantal inputs). Als er geen getallen zijn ingevoerd moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================

totaal = 0
aantal_inputs = 0

while True:
    getal = int(input("Vul een getal in, vul in '0' om te stoppen: "))
    if getal == 0:
        print("Je hebt geen getal ingevuld.")
        break
    else:
        totaal += getal
        aantal_inputs += 1

print(f"Het totaal is: {totaal} en het gemiddelde is: {totaal / aantal_inputs}")

# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt, Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15    # enz. tot en met 10
# ==========================================

factor = int(input("Voer een getal in: "))

for getal in range (1,11,1):
    print(f"{getal} x {factor} is: {getal * factor}")