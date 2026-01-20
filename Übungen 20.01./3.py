Kraft = int(input("Eingabe Kraft in Newton (N): "))
Querschnittsfläche = int(input("Eingabe Querschnittsfläche in Quadratmillimetern (mm^2): "))

if Querschnittsfläche == 0:
    print("Fehlermeldung")
pass 

Spannung = Kraft / Querschnittsfläche
print(f"{Spannung:.2f}")

if Spannung < 100:
    print("Niedrigspannung, weit unter Streckgrenze, daher sicher")
elif Spannung < 235:
    print("Betriebsspannung => Normal, im zulässigen Bereich ")
elif Spannung < 360:
    print("Grenzspannung => Achtung! Nahe/über Streckgrenze")
elif Spannung >= 360:
    print("Bruchspannung => GEFAHR! Material versagt!")
