# import string
# import random
# import time

def generiere_zeile(laenge=83):
    zeichen = string.ascii_letters + string.digits + "    "
    zeile = ''
    for i in range(laenge):
        zufallszeichen = random.choice(zeichen)
        zeile = zeile + zufallszeichen  # Anhängen
        print(zufallszeichen)
        time.sleep(0.005)
    print()

while True:
    generiere_zeile()

""" 1. Aufgabe:
Füge end='' in Zeile 11 hinzu!
So soll die Zeile dann aussehen:
print(zufallszeichen, end='')
"""

""" 2. Aufgabe:
Lösche: string.ascii_letters + 
"""