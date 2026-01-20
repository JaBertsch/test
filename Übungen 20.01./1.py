
drehzahl = int(input(f"drehzahl: "))
if drehzahl >= 3000 :
    print("Warnung: Hohe Drehzahl! Werkzeugverschleiß prüfen")

systemdruck = float(input("Eingabe Hydraulikdruck : "))
if systemdruck < 50:
    print("❌ Fehler: Druck zu niedrig ({druck}bar). Pumpe prüfen!")
else:
    print("✅ Druck OK ({druck} bar). System betriebsbereit.")
