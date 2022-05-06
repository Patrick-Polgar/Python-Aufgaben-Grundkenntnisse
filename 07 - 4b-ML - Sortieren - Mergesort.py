# ML - Text sortieren

def sortieren(liste):
    result = []
    # Wenn zwei Elemente in der Liste vorhanden sind, dann werden diese sortiert und zurückgegeben
    if len(liste) == 2:
        if (liste[0].lower() > liste[1].lower()):
            result.append(liste[1])
            result.append(liste[0])
        else:
            result.append(liste[0])
            result.append(liste[1])
            
    # Ist nur ein Element in der Liste, dann wird dieses als Liste zurückgegeben
    elif len(liste) == 1:
        result.append(liste[0])
    # Sind mehr Elemente in der Liste, so muss diese in 2 Listen geteilt werden
    else:
        # Mitte der Anzahl der Elemente bestimmen
        mitte = len(liste) // 2

        # Aufteilen der Listen
        listeA = liste[:mitte]
        listeB = liste[mitte:]
      
        listeA = sortieren(listeA)
        listeB = sortieren(listeB)
        
        # Beide sortierten Listen miteinander verbinden
        i = 0
        j = 0
        
        while i < len(listeA) and j < len(listeB):
            if (listeA[i] > listeB[j]):
                result.append(listeB[j])
                j += 1
            else:
                result.append(listeA[i])
                i += 1
        result += listeA[i:]
        result += listeB[j:]
    return result

# Testen der Funktion
liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print(sortieren(liste))
# print(liste)
# print(sortieren(liste))





