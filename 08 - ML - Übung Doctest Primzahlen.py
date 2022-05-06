import math
import doctest

"""
    1. Schreiben Sie für die Funktion istPrimzahl(n) Doctests
    2. korrigieren Sie die sematischen Fehler
    
    Hinweis: Es sind 3 sematische Fehler enthalten - Die Kommentare können Ihnen etvl. bei der Suche behilflich sein.
"""


# Algorithmus zur Primzahlberechnung
# Hier: Divisionsansatz

def istPrimzahl(n):
    
    """
    
    >>> istPrimzahl(-2)
    False
    >>> istPrimzahl(-1)
    False
    >>> istPrimzahl(0)
    False
    >>> istPrimzahl(1)
    False
    >>> istPrimzahl(2)
    True
    >>> istPrimzahl(3)
    True
    >>> istPrimzahl(4)
    False
    >>> istPrimzahl(5)
    True
    >>> istPrimzahl(6)
    False
    >>> istPrimzahl(7)
    True
    >>> istPrimzahl(8)
    False
    >>> istPrimzahl(9)
    False
    >>> istPrimzahl(10)
    False
    >>> istPrimzahl(11)
    True
    >>>
    
    """
    
    # Es wird davon ausgegangen, dass die übergebene Zahl eine Primzahl ist
    prim = True
    
    # Alle Zahlen, die kleiner als 2 sind, sind keine Primzahlen
    if n <= 1:
        prim = False
    
    # Die übergebene Zahl wird durch alle Zahlen geteilt, die kleiner oder gleich der Hälfte der Zahl selbst sind. Bei der 2 wird angefangen
    k = 2
    while k <= n/2:
        # Sollte die übergebene Zahl durch den aktuellen Teiler teilbar sein, so kann es sich nicht um eine Primzahl handeln und der Algorithmus ist beendet
        if n % k == 0: 
            prim = False
            break
        k += 1
    return prim
    

if __name__ == "__main__": 
    doctest.testmod()