import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

# XML-String
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'

# Einlesen von CSV-Dateien mit der DictReader-Funktion
with open('testdaten.csv') as csvdatei:
    # Einlesen der Datei
    obj = csv.DictReader(csvdatei, delimiter=';')

    # Eingelesene Daten als XML aufbauen
    adressen = ET.Element('Adressen')

    # Zeilenweises durchgehen des reader-Objektes und bearbeiten der Informationen
    for zeile in obj:
        adresse = ET.SubElement(adressen, 'Adresse')
        for key in zeile.keys():
            se = ET.SubElement(adresse, key)
            se.text = str(zeile.get(key))

    # Schließen der Datei
    csvdatei.close()

    # Setzen der "schicken" Ausgabe
    ET.indent(adressen, space="\t", level=0)

    # Eingelesene und verarbeitete Daten an den XML-String anfügen. Anmerkung: Der mit "tostring" generierte String ist
    # ein ByteString, welcher in einen String decodiert werden muss
    xml += (ET.tostring(adressen, encoding='utf-8', method='xml')).decode("utf8")

# Den String nun in eine Datei schreiben
file = open('adressen.xml', 'w')
file.write(xml)
file.close()