# ==========================================
# HOOFDSTUK 4.2 EXPRESSIES
# Opgave 1
# ==========================================

x = 5
print(f"x = {x}")
print(x > 0 and x < 10)
x -= 10
print(f"x = {x}")
print (x > 0 and x < 10)

# ==========================================
# Opgave 2:
# A. False
# B. True
# ==========================================

print(False and 0/0)
print(True or 1/0)

# ==========================================
# HOOFDSTUK 4.3
# Opgave 1:
# ==========================================

nummer = 42
even_of_oneven = "even" if 42 % 2 == 0 else "oneven"

print(even_of_oneven)

# ==========================================
# Opgave 2:
# ==========================================

uur = int(input("Hoelaat is het?: "))
begroeting = "Goedemorgen!" if uur < 12 else "Goedemiddag!" if uur < 18 else "Goedenavond!"

print(begroeting)

# ==========================================
# HOOFDSTUK 4.5
# Opgave 1 & 2:
# ==========================================

getal_1 = int(input("Vul een getal in: "))
getal_2 = int(input("Vul nog een getal in: "))

grootste_getal = getal_1 if getal_1 > getal_2 else getal_2

print(f"Opdr 1: {getal_1} + {getal_2} is {getal_1 + getal_2}")
print(f"Opdr 2: Het grootste getal is: {grootste_getal}")

