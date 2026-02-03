Getriebestufen = int((input("Anzahl der Getriebestufen:")))
stufen = []
for i in range(Getriebestufen):
   temp = float(input(f"Übersetzung Stufe {i+1}: "))
stufen.append(temp)
#oder stufen[i] = ...
print("----------------")

Gesamtübersetzung = 1
for i in stufen:
    Gesamtübersetzung = Gesamtübersetzung + i

print(stufen)