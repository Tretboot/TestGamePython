import tkinter as tk
import random

class HundemuenzenSpiel:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hundemünzen-Spiel")
        self.window.geometry("400x400")

        self.anzahl_muenzen = 0
        self.anzahl_hunde = 0

        self.muenzen_label = tk.Label(self.window, text="Anzahl Münzen: " + str(self.anzahl_muenzen))
        self.muenzen_label.pack()

        self.hunde_label = tk.Label(self.window, text="Anzahl Hunde: " + str(self.anzahl_hunde))
        self.hunde_label.pack()

        self.muenze_werfen_button = tk.Button(self.window, text="Münze werfen", command=self.muenze_werfen)
        self.muenze_werfen_button.pack()

        self.hund_kaufen_button = tk.Button(self.window, text="Hund kaufen", command=self.hund_kaufen)
        self.hund_kaufen_button.pack()

        self.window.mainloop()

    def muenze_werfen(self):
        ergebnis = random.randint(0, 1)
        if ergebnis == 0:
            self.anzahl_muenzen += 1
            self.muenzen_label.config(text="Anzahl Münzen: " + str(self.anzahl_muenzen))
            print("Gewonnen!")
        else:
            if self.anzahl_muenzen > 0:
                self.anzahl_muenzen -= 1
                self.muenzen_label.config(text="Anzahl Münzen: " + str(self.anzahl_muenzen))
                print("Verloren!")
            else:
                print("Keine Münzen mehr!")

    def hund_kaufen(self):
        if self.anzahl_muenzen >= 10:
            self.anzahl_hunde += 1
            self.anzahl_muenzen -= 10
            self.muenzen_label.config(text="Anzahl Münzen: " + str(self.anzahl_muenzen))
            self.hunde_label.config(text="Anzahl Hunde: " + str(self.anzahl_hunde))
            print("Hund gekauft!")
        else:
            print("Nicht genug Münzen!")

HundemuenzenSpiel()
