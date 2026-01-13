#Validierung von Betriebsparametern einer hydraulischen Presse

Hydraulikdruck = float(input(f"Hydraulikdruck (bar): "))
if (150 <= Hydraulikdruck <= 250 ): 
    print("Druckbereich erfüllt")
if not (150 <= hydraulikdruck <= 250 ):
    print("Druckbereich nicht erfüllt")

Pressengeschwindigkeit = float(input(f"Pressengeschwindigkeit (mm/s): "))
if (10 <= Pressengeschwindigkeit <= 80):
    print("Geschwindigkeit erfüllt")
if not (10 <= Geschwindigkeit <= 80):
    print("Geschwindigkeit nicht erfüllt")