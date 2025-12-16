# ==========================================
# Palindrome Checker
# Een Palindrome is een woord dat hetzelfde is als je het van voor naar achter leest als andersom.
# Bijvoorbeeld: lepel, radar en fiets zijn palindromes.
# Schrijf een programma dat een lijst van woorden heeft en voor elk woord aangeeft of het een palindrome is of niet.
# Het programma moet een dictionary maken waarbij de key het woord is en de value een boolean die aangeeft of het woord een palindrome is of niet.
# De dictionary moet er als volgt uitzien:
# {
#     "radar": True,
#     "fiets": False,
#     "lepel": True,
#     "python": False
# }
# ==========================================

words = ['radar', 'fiets', 'lepel', 'python']
dict = {}

for word in words:
    forward = []
    backwards = []
    for letter in word:
        backwards.insert(0, letter)
        forward.append(letter)
    if forward == backwards:
        dict[word] = True
    else:
        dict[word] = False

print("Palindromen:")
for key, value in dict.items():
    print(f"{key}: {value}")
print()
# ==========================================
# Bonus opdracht:
# 2 zinnen, 1 zin is geen palindrome, de andere wel. Bepaal welke zin een palindrome is.
# Tip 1: Gebruik de replace() functie om alle spaties uit de zin te halen.
# ==========================================

zin1 = "dit is een testzin om te testen of dit programma werkt"
zin2 = "eva can i see bees in a cave"

def is_palindrome(zin):
    backwards = []
    forward = []
    for letter in zin:
        backwards.insert(0, letter)
        forward.append(letter)
    if forward == backwards:
        return True
    else:
        return False

zin1_geplakt = zin1.replace(" ","")
zin2_geplakt = zin2.replace(" ","")

if is_palindrome(zin1_geplakt):
    print(f"'{zin1}' is een palindrome")
if is_palindrome(zin2_geplakt):
    print(f"'{zin2}' is een palindrome")



