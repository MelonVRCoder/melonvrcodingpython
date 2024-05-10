booler = input('Was willst du rechnen Plus oder Mal: ')
zahl = int(input('Erste Zahl eingeben: '))
zahl_zwei = int(input('Zweite Zahl eingebn: '))

if booler == "Mal":
    print(zahl * zahl_zwei)
if booler == "Plus":
    print(zahl + zahl_zwei)
input('Drücke eine Taste um das Promgramm zuschließen: ')