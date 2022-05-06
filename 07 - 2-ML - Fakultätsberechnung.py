# ML - Fakultätsberechnung

# Die Berechnung der Fakultät mittels Rekursion beruht darauf, dass die aktuelle Zahl multipliziert wird
# mit dem Ergebnis der Fakultät der aktuellen Zahl minus Eins
def fakultaetRek(n):
    # Sollte die aktuelle Zahl n kleiner oder gleich 1 sein, ist die Abbruchbedingung erreicht und 1 wird zurückgegeben
    if (n <= 1):
        return 1
    else:
        return n * fakultaetRek(n-1)


# Bei der iterativen Berechnung wird das bisherige Ergebnis immer mit der aktuellen Zahl multipliziert.
# Dies wird solange fortgeführt, bis die aktuelle Zahl dem übergebenen Wert von n gleicht.
def fakultaetIter(n):
    i = 1
    result = 1
    
    while i <= n:
        result *= i
        i += 1
        
    return result

# Testen der Funktion
print(fakultaetRek(20))
print(fakultaetIter(20))

# Während rekursiv keine Berechnung der Fakultät von 1000 mehr möglich ist, da die maximale Rekursionstiefe erreicht wurde.
# Ist dies Iterativ kein Problem. Hier lassen sich auch noch größere Fakultäten berechnen
#print(fakultaetRek(1000))
print(fakultaetIter(1000))
print(fakultaetIter(10000))