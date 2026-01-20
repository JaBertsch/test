länge = 150
dehnung = 0.25
ergebnis = dehnung / länge * 100
print(f"Das Ergebnis ist: {ergebnis:.3f}")
print("A", "B", "C", sep="-")
print("1", "2", "3", sep="")
x = 3.141592653589793
print(f"{x:.2f}", sep="")
gewicht = 75.3456
print(f"{gewicht:.2f} kg")
a = 10
b = 3
ergebnis = a + b
print(f"{a} + {b} = {ergebnis}")
y = 42
print(f"{y:´>5}")

print(f"{"Messung":<10} {"Temperatur":>10} {"Status":>8}")
print("-" * 30)
items = [
    ("Messung 1", 22.5, "OK"),
    ("Messung 2", 23.1, "OK"),
    ("Messung 3", 24.8, "WARM")
        ]
for messung, temperatur, status in items:
    print(f"{messung:<13} {temperatur:<10} {status:<10}")