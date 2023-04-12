# Ein Programm, das zufällig Sprüche von Held der Steine ausgibt

# Eine Liste von Sprüchen
sprueche = [
    "Das ist kein Lego, das ist Kunst!",
    "Das ist kein Spielzeug, das ist ein Modell!",
    "Das ist kein Bausatz, das ist eine Herausforderung!",
    "Das ist kein Preis, das ist ein Witz!",
    "Das ist kein Set, das ist eine Legende!",
    "Das ist kein Lego, das ist ein Traum!",
    "Das ist kein Plastik, das ist Magie!",
    "Das ist kein Karton, das ist eine Schatzkiste!",
    "Das ist kein Katalog, das ist eine Bibel!",
    "Das ist kein Hobby, das ist eine Leidenschaft!"
]

# Die Bibliotheken random und tkinter importieren
import random
import tkinter as tk

# Eine Funktion definieren, die einen zufälligen Spruch auswählt und in einem neuen Fenster anzeigt
def spruch_anzeigen():
    spruch = random.choice(sprueche)
    # Ein neues Fenster erstellen und die Größe an den Spruch anpassen
    neues_fenster = tk.Toplevel()
    neues_fenster.title("Spruch von Held der Steine")
    # Die Fensterbreite um 20% erhöhen
    fensterbreite = int(len(spruch) * 10 * 1.2)
    neues_fenster.geometry(f"{fensterbreite}x100")
    # Das Fenster an einer zufälligen Position auf dem Bildschirm platzieren
    x = random.randint(0, fenster.winfo_screenwidth() - fensterbreite)
    y = random.randint(0, fenster.winfo_screenheight() - 100)
    neues_fenster.geometry(f"+{x}+{y}")
    # Ein Textwidget erstellen, das den Spruch anzeigt, und die Größe, Schriftart und Ausrichtung festlegen
    textwidget = tk.Text(neues_fenster, font=("Comic Sans MS", 20, "bold"))
    textwidget.pack(expand=True, fill=tk.BOTH)
    # Einen Tag definieren, der den Text mittig ausrichtet
    textwidget.tag_configure("center", justify=tk.CENTER)
    # Den Spruch mit dem Tag einfügen
    textwidget.insert(1.0, spruch, "center")
    # Die Farbe des Textes und des Hintergrunds ändern
    textwidget.config(fg="red", bg="yellow")
    # Den Text nicht umbrechen lassen
    textwidget.config(wrap=tk.NONE)

# Ein Fenster erstellen und die Größe festlegen
fenster = tk.Tk()
fenster.title("Sprüche von Held der Steine")
fenster.geometry("400x200")

# Ein Knopf erstellen, der die Funktion spruch_anzeigen aufruft, und die Schriftart festlegen
knopf = tk.Button(fenster, text="Spruch anzeigen", command=spruch_anzeigen, font=("Arial", 16))
knopf.pack()

# Ein Label erstellen, das den Code by Bing und Tretboot anzeigt
label = tk.Label(fenster, text="Code by Bing and Tretboot", font=("Arial", 12))
label.pack()

# Die Hauptschleife des Fensters starten
fenster.mainloop()
