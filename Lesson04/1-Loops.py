# ==========================================
# Opgave 1 - Tafels:

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# ==========================================

gebruikers_input = int(input("Voer een getal in: "))

# Probeer het eerst zonder loop
print(f"1 x {gebruikers_input} = {1 * gebruikers_input}")
print(f"2 x {gebruikers_input} = {2 * gebruikers_input}")
print(f"3 x {gebruikers_input} = {3 * gebruikers_input}")
print(f"4 x {gebruikers_input} = {4 * gebruikers_input}")
print(f"5 x {gebruikers_input} = {5 * gebruikers_input}")
print(f"6 x {gebruikers_input} = {6 * gebruikers_input}")
print(f"7 x {gebruikers_input} = {7 * gebruikers_input}")
print(f"8 x {gebruikers_input} = {8 * gebruikers_input}")
print(f"9 x {gebruikers_input} = {9 * gebruikers_input}")
print(f"10 x {gebruikers_input} = {10 * gebruikers_input}")

# Probeer het nu met een loop.
for x in range(1,11):
    print(f"{x} x {gebruikers_input} = {gebruikers_input * x}" )

# ==========================================
# Opgave 2 - Optellen:
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)
# ==========================================

som = 0
for x in range(gebruikers_input + 1):
    som += x
print(som)

# ==========================================
# Opgave 3 - FizzBuzz:

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.
# ==========================================

for x in range(1, 101):
    if (x % 3) == 0 and (x % 5) != 0:
        print("Fizz")
    elif (x % 3) != 0 and (x % 5) == 0:
        print("Buzz")
    elif (x % 3) == 0 and (x % 5) == 0:
        print("FizzBuzz")
    else:
        print(x)


# ==========================================
# Opgave 4 - Fibonacci Reeks:

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# ==========================================

i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
a = 0
b = 1

# Eerst drukken we de eerste twee getallen af
fibonacci = [0, 1]
# print(fibonacci)

# Vervolgens berekenen we de volgende getallen en drukken ze af
for getal in range(i-2):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)