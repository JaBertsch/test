datei = open("V09/maschine_01.log")
zeilen = datei.readlines()
print(f"Anzahl Zeilen: {len(zeilen)}")
anzahlAlarm = 0
anzahlError = 0

for zeile in zeilen:
    anzahlAlarm += zeile.count("ALARM")
    anzahlError += zeile.count("ERROR")

print(f"anzahl alarm: {anzahlAlarm}")
print(f"Anzahl error: {anzahlError}")

zeile.