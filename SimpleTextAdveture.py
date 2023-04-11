print("Willkommen zu meinem Spiel!")
name = input("Wie ist dein Name? ")
print("Hallo,", name)

antwort = input("Möchtest du das Spiel spielen? ").lower()
if antwort == "ja":
 print("Lass uns anfangen!")
else: print("Okay, vielleicht ein anderes Mal.")

antwort = input("Du stehst vor einem dunklen Wald. Möchtest du hineingehen? ").lower()
if antwort == "ja":
 print("Du gehst in den Wald.")
else:
 print("Okay, vielleicht ein anderes Mal.")

antwort = input("Du siehst einen Fluss. Möchtest du schwimmen gehen? ").lower()
if antwort == "ja":
 print("Du gehst schwimmen und ertrinkst. Das Spiel ist vorbei.")
else:
 print("Okay, vielleicht ein anderes Mal.")
