import random
import string
import tkinter as tk

# Zeichenmenge definieren
zeichen = string.ascii_letters + string.digits + string.punctuation +"                                  "

# Starttext erzeugen
text = ''.join(random.choice(zeichen) for _ in range(83))

# GUI einrichten
fenster = tk.Tk()
fenster.title("Zufallszeichen Laufband")
fenster.configure(bg="black")
FPS = 10

ausgabe = tk.Label(fenster, text=text, font=("Courier", 14), fg="lime", bg="black")
ausgabe.pack(padx=20, pady=20)

def update():
    global text
    # Neuen Buchstaben hinzufügen und den ersten Buchstaben entfernen
    neuer_buchstabe = random.choice(zeichen)
    text = text[1:] + neuer_buchstabe
    ausgabe.config(text=text)
    fenster.after(int(1000 / FPS), update)

update()
fenster.mainloop()
