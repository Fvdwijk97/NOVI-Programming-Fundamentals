# ==========================================
# Schrijf een functie die het gemiddelde berekent van een lijst met getallen.
# ==========================================

grades = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}
total = 0
count = 0

for sub, grade in grades.items():
    total += grade
    count += 1

average = round(total/count, 1)
print(f"Average of all grades is: {average}")