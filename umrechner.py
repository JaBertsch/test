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
    if operator == "multiplikation" or operator =="m":
        ergebnis = 1
    else:
        ergebnis = 0
    i = 1
    while True:
    
        zahl = float(input(f"Gib die {i} Zahl ein:"))
        if zahl == 0:
            break

        if operator == "addition" or operator == "a" :
            ergebnis = ergebnis + zahl
        else:
            if operator == "subtraktion" or operator == "s" :
                ergebnis = ergebnis - zahl
            else: 
                if operator == "multiplikation" or operator == "m" : # or "m" funktioniert nicht => "m" die ganze zeit konstant
                    ergebnis = ergebnis * zahl
                else:
                    if operator == "division" or operator == "d":
                        ergebnis = ergebnis / zahl
                    else:
                        print("operation kann nicht ausgeführt werden")
        i+=1
    
    print(f"Das Ergebnis ist: {ergebnis} :))))))))")
    print()
                
