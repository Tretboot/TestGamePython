import mouse

# Überprüfen Sie, ob die Maus angeschlossen ist
if mouse.is_pressed(button=&apos;left&apos;):
print(&apos;Maus ist angeschlossen&apos;)
else:
print(&apos;Maus ist nicht angeschlossen&apos;)

# Bewegen Sie die Maus um 100 Pixel nach rechts und unten mit einer Dauer von 0,5 Sekunden
mouse.move(100, 100, absolute=False, duration=0.5)

# Klicken Sie mit der linken Maustaste
mouse.click(&apos;left&apos;)

# Klicken Sie mit der rechten Maustaste
mouse.click(&apos;right&apos;)
