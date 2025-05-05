# Dateiname: 5-matrix.py

import tkinter as tk
import random
import string

# ==============================
# Steuerzentrale
BREITE = 800
HOEHE = 600
SPALTENBREITE = 20
ZEICHENGROESSE = 16
FPS = 15  # 15 Frames pro Sekunde

ANTEIL_GROß = 0.1       # 10 % große Ströme
ANTEIL_MITTEL = 0.15    # 15 % mittelgroße Ströme
FAKTOR_GROß = 2.0       # Faktor für große Schrift
FAKTOR_MITTEL = 1.2     # Faktor für mittlere Schrift
FAKTOR_KLEIN = 0.5      # Faktor für kleine Schrift
GESCHWINDIGKEIT_GROß = 2.0
GESCHWINDIGKEIT_MITTEL = 1.75
GESCHWINDIGKEIT_KLEIN = 1.0
# ==============================

#ZEICHEN = "01"
ZEICHEN = string.ascii_letters + string.digits + string.punctuation + "☠☠☠"
#ZEICHEN = "⚡✨🌟🌀💥🔥☠️"
#ZEICHEN = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄ0123456789"

root = tk.Tk()
root.title("MEGA-Matrix!")
canvas = tk.Canvas(root, width=BREITE, height=HOEHE, bg="black", highlightthickness=0)
canvas.pack()

anzahl_spalten = BREITE // SPALTENBREITE

# Zeichenstrom-Klasse
class ZeichenStrom:
    def __init__(self, x):
        self.x = x
        self.reset()
    
    def reset(self):
        zufall = random.random()
        if zufall < ANTEIL_GROß:
            self.stufe = "groß"
            faktor = FAKTOR_GROß
            geschwindigkeitsfaktor = GESCHWINDIGKEIT_GROß
        elif zufall < ANTEIL_GROß + ANTEIL_MITTEL:
            self.stufe = "mittel"
            faktor = FAKTOR_MITTEL
            geschwindigkeitsfaktor = GESCHWINDIGKEIT_MITTEL
        else:
            self.stufe = "klein"
            faktor = FAKTOR_KLEIN
            geschwindigkeitsfaktor = GESCHWINDIGKEIT_KLEIN

        self.fontgroesse = int(ZEICHENGROESSE * faktor)
        self.geschwindigkeit = random.randint(1, 15) * geschwindigkeitsfaktor

        self.zeichen = [canvas.create_text(
            self.x,
            -i * self.fontgroesse,
            text=random.choice(ZEICHEN),
            fill="lime",
            font=("Courier", self.fontgroesse)
        ) for i in range(random.randint(5, 16))]

    def update(self):
        for i, z in enumerate(self.zeichen):
            canvas.move(z, 0, self.geschwindigkeit)
            y = canvas.coords(z)[1]
            # Farbverlauf
            if i == len(self.zeichen) - 1:
                canvas.itemconfig(z, fill="white")
            elif i == len(self.zeichen) - 2:
                canvas.itemconfig(z, fill="lightgreen")
            else:
                canvas.itemconfig(z, fill="lime")
            # Zeichen zufällig ändern
            if random.random() < 0.1:
                canvas.itemconfig(z, text=random.choice(ZEICHEN))
        
        # Wenn Strom unten: reset
        y_letzter = canvas.coords(self.zeichen[-1])[1]
        if y_letzter > HOEHE + 20:
            for z in self.zeichen:
                canvas.delete(z)
            self.reset()

# Ströme vorbereiten
stroeme = []
for _ in range(anzahl_spalten * 3):
    x_spalte = random.randint(0, anzahl_spalten - 1)
    x = x_spalte * SPALTENBREITE
    stroeme.append(ZeichenStrom(x))

def update():
    for strom in stroeme:
        strom.update()
    root.after(int(1000 / FPS), update)

update()
root.mainloop()
