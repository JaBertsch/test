print("Der tolle Taschenrechner")

print("Operationen:")
print("- addition/a")
print("- subtraktion/s")
print("- multiplikation/m")
print("- division/d")
print("- exit/e")


while True:
    operator = input("Gib eine Rechenoperation an:")
    if operator == "exit" or operator =="e":
        break
    zahl1 = float(input("Gib die erste Zahl ein:"))
    zahl2 = float(input("Gib die zweite Zahl ein:"))

    if operator == "addition" or operator == "a" :
        ergebnis = zahl1 + zahl2
    else:
        if operator == "subtraktion" or operator == "s" :
            ergebnis = zahl1 - zahl2
        else: 
            if operator == "multiplikation" or operator == "m" : #funktioniert nicht => "m" die ganze zeit konstant
                ergebnis = zahl1 * zahl2
            else:
                if operator == "division" or operator == "d":
                    ergebnis = zahl1 // zahl2
                else:
                    print("operation kann nicht ausgeführt werden")

    print(f"Das Ergebnis ist: {ergebnis} :))))))))")
    print()
                
