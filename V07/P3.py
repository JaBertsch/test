
nenndurchmesser_schrauben = [3,4,5,6,8,10]

spannungsquerschnitt = 0.8 * (3.14*nenndurchmesser_schrauben[0]**2)/4

zugfestigkeiten = [400, 800, 1000]
vorspannkraft = 0.7 * spannungsquerschnitt * zugfestigkeiten[0]

anziehdrehmoment = 0.2 * nenndurchmesser_schrauben[0] * vorspannkraft

print("=" * 47)
print("Anziehdrehmoment-Tabelle")
print("=" * 47)

print(f"{"Gewinde":<8}|", end="")
for zugfestigkeit in zugfestigkeiten:
    print(f"{zugfestigkeit:>9} [Nm] |", end="")

print()
print("─" * 8 + "|" + "─" * 11 + "|" + "─" * 11 + "|" + "─" * 11 + "|")

for durchmesser in nenndurchmesser_schrauben:
    print(f"M{durchmesser}      |", sep="")


