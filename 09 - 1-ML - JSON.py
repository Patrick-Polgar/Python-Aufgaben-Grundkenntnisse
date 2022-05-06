import csv
import json

# Erstellen des Containers in den die csv-Daten eingelesen werden sollen
dict= []

# Einlesen von CSV-Dateien mit der DictReader-Funktion
with open('testdaten.csv') as csvdatei:
    # Einlesen der Datei
    obj = csv.DictReader(csvdatei, delimiter=';')

    # Zeilenweises durchgehen des reader-Objektes und anfügen an das Array
    for zeile in obj:
        dict.append(zeile)

    # Schließen der Datei
    csvdatei.close()

# Eingelesene Daten als JSON formatiert in die Datei "adressen.json" ausgeben
json.dump(dict, open('adressen.json', 'w'), indent= 4)