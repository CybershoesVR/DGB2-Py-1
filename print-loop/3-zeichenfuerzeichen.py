import random
import string
import time

def generiere_zeile(laenge=83):
    zeichen = string.ascii_letters + string.digits + "    "
    #zeichen = string.digits + "      "
    zeile = ''
    for i in range(laenge):
        zufallszeichen = random.choice(zeichen)
        zeile = zeile + zufallszeichen  # Anhängen
        print(zufallszeichen, end='')
        time.sleep(0.005)
    print()

while True:
    generiere_zeile()

