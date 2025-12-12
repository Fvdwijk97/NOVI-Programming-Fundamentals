# ==========================================
# Maak een game, waar minimaal 3 lagen in zitten. Dus er zijn 2 if-statements tot het eind.
# Zorg dat je input valideert.
# Denk ook na over welke tekst je wilt printen, welk verhaal je wilt vertellen.
# ==========================================

print("Race tegen de Tijd - De Jubileum Missie")
print()
print("""Dit is Marco:
             O
            /|\\
             |
            /|\\""")

print("""Vanavond is het jubileum van Marco en zijn vrouw Maria. 
Marco heeft zijn vrouw beloofd om op tijd thuis te zijn vanavond, 
maar Marco heeft een probleem; zijn baas zit hem altijd op de hielen met last-minute taken.
Als Marco vanavond niet op tijd thuis is, wacht hem een koude nacht... op de bank. 
Marco houdt van zijn vrouw, maar ontsnappen van werk is een kunst.

Vanavond zet hij alles op alles om op tijd thuis te komen. 
Help Marco! Kies slimme routes, ontwijk files en beslis wat Marco moet doen bij ontverwachte situaties.

Lukt het jou om Marco op tijd thuis te krijgen? Of slaapt Marco alsnog op de bank? :( """)
print()

situatie1 = False
situatie2 = False
situatie3 = False
situatie4 = False
situatie5 = False

foutcode = "Je hebt geen geldige keuze gemaakt, kies A of B: "
opnieuw_of_stop = True

while True:
    print(
        "Het is 17:00, tijd om naar huis te gaan! Je hoort je baas uit de verte aankomen mompelen... Hij is op zoek naar jou!")

    keuze1 = input("""Wat doe je?
  A. Snel wegwezen! 
  B. Netjes vragen wat er is. 
  Vul in A of B: """)
    print()

    while not (keuze1 == "A" or keuze1 == "B"):
        keuze1 = input(foutcode)

    if keuze1 == "B":
        situatie1 == True
    elif keuze1 == "A":
        print(
            "Net op tijd! Je zit in de auto! Je hoorde vandaag dat er een wegafsluiting was maar de weg lijkt rustig..")
        keuze2 = input("""Wat doe je?
    A. Je neemt het risico, je pakt de snelweg
    B. Zekere voor het onzekere! Je neemt de langere route binnendoor
    Vul in A of B: """)
        print()
        if keuze2 == "A":
            print("Oh nee, file! Had ik maar naar mijn collega's geluisterd..")
            print()
        while not (keuze2 == "A" or keuze2 == "B"):
            keuze2 = input(foutcode)
            print()

        print("Je tank is bijna leeg! Tanken kost tijd, maar langs de weg staan zonder brandstof nog meer!")
        keuze3 = input("""Wat doe je?
    A. Je gaat tanken
    B. Je neemt het risico, zo snel mogelijk naar huis!
    Vul in A of B: """)
        print()
        print()
        while not (keuze3 == "A" or keuze3 == "B"):
            keuze3 = input(foutcode)
            print()

        print("Het begin te stormen.. Op de radio praten ze over code rood!")
        keuze4 = input("""Wat doe je?
    A. Je zoekt een parkeerplek om te schuilen voor de storm
    B. Door weer en wind, zo snel mogelijk naar mijn vrouw!
    Vul in A of B: """)
        print()
        while not (keuze4 == "A" or keuze4 == "B"):
            keuze4 = input(foutcode)
            print()

    if keuze1 == "B":
        situatie1 = True
    elif keuze2 == "A":
        if keuze3 == "A" and keuze4 == "A":
            situatie1 = True
        elif keuze3 == "A" and keuze4 == "B":
            situatie2 = True
        elif keuze3 == "B" and keuze4 == "A":
            situatie3 = True
        elif keuze3 == "B" and keuze4 == "B":
            situatie3 = True
    elif keuze2 == "B":
        if keuze3 == "A" and keuze4 == "A":
            situatie1 = True
        elif keuze3 == "A" and keuze4 == "B":
            situatie1 = True
        elif keuze3 == "B" and keuze4 == "A":
            situatie4 = True
        elif keuze3 == "B" and keuze4 == "B":
            situatie3 = True

    if situatie1:
        print("Sukkel! Je bent te laat!")
    elif situatie2:
        print("Je bent op tijd! Je slaapt vanavond lekker warm in je bedje.")
    elif situatie3:
        print("Brandstof is op en je boze vrouw moet je komen halen! Je slaapt een maand in het hondenhok")
    elif situatie4:
        print("Helaas! Je bent dood door een blikseminslag")

    opnieuw_of_stop = input("Wil je nog een keer spelen? Vul in ja of nee: ").lower()
    if opnieuw_of_stop == "nee":
        break