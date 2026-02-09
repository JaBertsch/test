import math

# Gewinde-Größen
gewinde = ["M3", "M4", "M5", "M6", "M8", "M10"]

# Festigkeitsklassen mit Zugfestigkeit
festigkeitsklassen = {
    "4.6": 400,
    "8.8": 800,
    "10.9": 1000
}

print("═" * 47)
print("  Anziehdrehmoment-Tabelle (trocken, verzinkt)")
print("═" * 47)

# Kopfzeile
print(f"{'Gewinde':<8}|", end="")
for klasse in festigkeitsklassen.keys():
    print(f"{klasse:>5} [Nm] |", end="")
print()
print("─" * 8 + "|" + "─" * 11 + "|" + "─" * 11 + "|" + "─" * 11 + "|")

# Datenzeilen
for g in gewinde:
    d = int(g[1:])  # Durchmesser aus "M6" → 6
    print(f"{g:<8}|", end="")
    
    for r_m in festigkeitsklassen.values():
        # Vereinfachte Berechnung
        a_s = 0.8 * math.pi * (d**2) / 4  # Spannungsquerschnitt
        f_v = 0.7 * a_s * r_m  # Vorspannkraft
        m_a = 0.2 * d * f_v / 1000  # Drehmoment in Nm
        
        print(f"{m_a:10.1f} |", end="")
    print()