systemdruck = float(input("Eingabe Hydraulikdruck : "))
if systemdruck < 50:
    print(f"❌ Fehler: Druck zu niedrig ({systemdruck}bar). Pumpe prüfen!")
else:
    print(f"✅ Druck OK ({systemdruck} bar). System betriebsbereit.")
