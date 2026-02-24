datei = open("V09/maschine_01.log")
zeilen = datei.readlines()

for zeile in zeilen:
    print(zeile)