# ==========================================
# Onderstaande code is een puzzel.
# De 7 coördinaten vormen een woord van 7 letters.
# Ontcijfer elk coördinaat één voor één tot een letter uit de puzzel lijst.
# Sla jou ontcijferde letters op in de "antwoord" variabele.
# (Tip: bekijk een woord als een lijst van letters.)
# Print je antwoord uit.
# ==========================================

puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0,0), (2,0), (0,-2), (1,3), (0,3), (2,4), (1,-1)]

antwoord1 = []
for x, y in coordinaten:
    antwoord1.append(puzzel[x][y])

# Óf:

antwoord2 = [puzzel[x][y] for x, y in coordinaten]
print("".join(antwoord2))