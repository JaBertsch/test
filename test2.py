print("A", "B","C",sep="-")
print("Frage:")
name = "Anna"
alter = 20
print("Hallo, ich bin", name, "und bin", alter, "Jahre alt." )
print(f"hallo, ich bin {name} und {alter} Jahre alt")
artikel = ["Schraube", "Mutter", "Unterlegscheibe"]
preise = [0.05, 0.08, 0.03]
for art, preis in zip(artikel, preise):
    print(f"{art:20} {preis:8.2f} EUR")
print("Einkaufsliste:")
print(f"{"Artikel":<30} {"Menge":>6} {"a Preis":>8} {"Summe":>10}")
print("-" * 50)
Artikel = [
    ("Schrauben M5x20", 50, 0.08),
    ("Muttern M5", 50, 0.06),
    ("Unterlegscheiben", 100, 0.02)
     ]
for artikel, menge, preis in Artikel:
    summe = menge * preis
    print(f"{artikel:<30} {menge:>6} {preis:>8.2f} {summe:>10.2f}")