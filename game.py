import random

def main():
print(&quot;Willst du gewinnen?&quot;)
antwort = input(&quot;Ja oder Nein? &quot;)
if antwort == &quot;Ja&quot;:
print(&quot;Herzlichen Glückwunsch! Du hast gewonnen!&quot;)
else:
while True:
fragen = [&quot;Warum nicht?&quot;, &quot;Hast du das Spiel verstanden?&quot;, &quot;Wie geht es dir heute?&quot;]
print(random.choice(fragen))
antwort = input(&quot;Ja oder Nein? &quot;)
if antwort == &quot;Ja&quot;:
print(&quot;Herzlichen Glückwunsch! Du hast gewonnen!&quot;)
break

if __name__ == &quot;__main__&quot;:
main()
