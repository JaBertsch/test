sensor_wert = (input("empfangene Nachricht: "))
print(f"Ursrünglicher Wert: {sensor_wert} ", end="  ")
print(f"Typ: {type(sensor_wert)}")

wert_int = int(sensor_wert)
print(f"Als Integer: {wert_int} ,  Typ: {type(wert_int)} ,  Drehzahl: {wert_int} U/min")

wert_float = float(sensor_wert)
print(f"Als Float: {wert_float} ,  Typ: {type(wert_float)} ,  Temperatur: {wert_float} °C")

wert_bool = bool(sensor_wert)
print(f"Als Boolean: {wert_bool},  Typ: {type(wert_bool)} ,  Motor: LÄUFT ")