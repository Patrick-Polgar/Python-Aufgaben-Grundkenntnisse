# ML - Primzahlen von 2 bis 10.000

import math;

# Algorithmus zur Primzahlberechnung
# Hier: Divisionsansatz

def istPrimzahl(n):
    # Es wird davon ausgegangen, dass die übergebene Zahl eine Primzahl ist
    prim = True
    
    # Alle Zahlen, die kleiner als 2 sind, sind keine Primzahlen
    if n < 2:
        prim = False
    
    # Die übergebene Zahl wird durch alle Zahlen geteilt, die kleiner oder gleich der Quadratwurzel der Zahl selbst sind. Bei der 2 wird angefangen
    k = 2
    while k <= math.sqrt(n):
        # Sollte die übergebene Zahl durch den aktuellen Teiler teilbar sein, so kann es sich nicht um eine Primzahl handeln und der Algorithmus ist beendet
        if n % k == 0: 
            prim = False
            break
        k += 1
    return prim
    

# Liste von Primzahlen
def primzahlenBis(n):
    # Start der Primzahlberechnung bei der Zahl 2
    zahl = 2
    
    # Ergebnisliste definieren
    result = []
    
    while (zahl <= n):
        # Wenn die aktuelle Zahl eine Primzahl ist, dann soll sie der Ergebnisliste hinzugefügt werden
        if istPrimzahl(zahl):
            result.append(zahl)
        zahl += 1
        
    # Ergebnisliste zurückgeben
    return result
        

# Aufrufen der Liste von 2 bis 10.000
primzahlen = primzahlenBis(10000)
print(primzahlen)
print('Anzahl gefundener Primzahlen: ' + str(len(primzahlen)))



