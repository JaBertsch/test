
x = 5
print(f"|{x:0>10}|")
pi = 3.14159265358979
"pi ist ungefähr {:.2f}".format(pi)
print("Kraft-Berechnung: F = m * a")

masse = float(input("Masse in kg eingeben: "))
beschleunigung = float(input("Beschleunigung in m/s² eingeben: "))

kraft = masse * beschleunigung

print(f"Masse: {masse:>10.2f} kg")
print(f"Beschleunigung: {beschleunigung:>10.2f} m/s²")
print(f"Resultierende: {kraft:>10.2f} N")
print("-" * 50)
