# Dateiname: 4-laufband.py

import random
import string
import tkinter as tk

# Zeichenmenge und Starttext definieren
zeichen = string.ascii_letters + string.digits + string.punctuation +"                                  "
zeile = ''.join(random.choice(zeichen) for _ in range(83))

# GUI einrichten
fenster = tk.Tk()
fenster.title("Zufallszeichen Laufband")
fenster.configure(bg="black")
FPS = 10

ausgabe = tk.Label(fenster, text=zeile, font=("Courier", 14), fg="lime", bg="black")
ausgabe.pack(padx=20, pady=20)

def update():
    global zeile
    neuer_buchstabe = random.choice(zeichen) # Zufallszeichen
    zeile = zeile[1:] + neuer_buchstabe      # Buchstabenmagie (1.Zeichen weg, am Ende eins dazu)
    ausgabe.config(text=zeile)               # Dem Ausgabe-Ding wird unsere zeile übergeben
    fenster.after(int(1000 / FPS), update)
    # fenster.after() definiert wann die Funktion namens "update" wieder aufgerufen werden soll.

# -------------------------------
# Hier erst startet das Programm!
# Zuvor wurde nur definiert.
# -------------------------------

update()           # Startet die Funktion update() einmal
fenster.mainloop() # Startet das tkinter Fenster
# Dem tkinter Fenster wurde mit fenster.after(zeit, update) erklärt,
# dass es nach einer gewissen Zeit die Funktion "update" wieder ausführen soll.