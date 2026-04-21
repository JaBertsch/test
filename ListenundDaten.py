
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 100 / zahl
    print(f"Ergebnis: {ergebnis}")
except ValueError:
    print("Fehler: Die Eingabe ist keine gültige Zahl.")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")
finally:
    print("wird immer ausgegeben")