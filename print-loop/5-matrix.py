import tkinter as tk
import random
import string

BREITE = 800
HOEHE = 600
SPALTENBREITE = 20
ZEICHENGROESSE = 16
ZEILENANZAHL = HOEHE // ZEICHENGROESSE
FPS = 15  # 15 Frames pro Sekunde
#ZEICHEN = "01"  # oder z. B. string.ascii_uppercase
ZEICHEN = string.ascii_letters + string.digits + string.punctuation
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
        self.zeichen = [canvas.create_text(
            self.x,
            -i * ZEICHENGROESSE,
            text=random.choice(ZEICHEN),
            fill="lime",
            font=("Courier", ZEICHENGROESSE)
        ) for i in range(random.randint(5, 16))]
        self.geschwindigkeit = random.randint(1, 15)

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
