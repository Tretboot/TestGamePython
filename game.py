import random
fragen = ["Warum nicht?", "Hast du das Spiel verstanden?", "Wie geht es dir heute?"]
def main():
    print("Willst du gewinnen?")
antwort = input("Ja oder Nein? ").lower()
if antwort == "ja":
    print("Herzlichen Glückwunsch! Du hast gewonnen!")
else:
    while True:
            print(random.choice(fragen))
antwort = input("Ja oder Nein? ")
if antwort == "Ja":
    print("Herzlichen Glückwunsch! Du hast gewonnen!")
break

if __name__ == "__main__":
    main()
