# ML - Primzahlen von 2 bis 10.000

import math;

# Algorithmus zur Primzahlberechnung
# Hier: Sieb des Eratosthenes

def primzahlenBis(n):
    # Liste aller möglichen Zahlen erstellen von 2 bis n
    result = list(range(2, n+1))
    
    index = 0
    
    # Jede in der Liste vorhandene Zahl wird durchgegangen. Die Liste wird während der Bearbeitung immer kürzer
    while index < len(result):
        # Start bei index mit der zutestenden Zahl bei index + 1
        i = index
        i += 1
        
        # Alle in der Liste vorhandenen Zahlen werden durch die aktuelle Zahl geteilt. Wenn dies gelingt, fliegt die jeweilige Zahl aus der Liste
        while i < len(result):
            if result[i] % result[index] == 0:
                result.remove(result[i])
            else:
                i += 1
        
        index += 1
    
    return result


# Aufrufen der Liste von 2 bis 10.000
primzahlen = primzahlenBis(10000)
print(primzahlen)
print('Anzahl gefundener Primzahlen: ' + str(len(primzahlen)))



