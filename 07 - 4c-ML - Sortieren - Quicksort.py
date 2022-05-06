# ML - Sortieren Quicksort
# https://de.wikipedia.org/wiki/Quicksort

def quicksort(links, rechts):
    if links < rechts:
        teiler = teile(links, rechts)
        quicksort(links, teiler - 1)
        quicksort(teiler + 1, rechts)


def teile(links, rechts):
    i = links
    # Starte mit j links vom Pivotelement
    j = rechts - 1
    pivot = liste[rechts].lower()

    while i < j: # solange i an j nicht vorbeigelaufen ist 
        # Suche von links ein Element, welches größer oder gleich dem Pivotelement ist
        while i < rechts and liste[i].lower() < pivot:
            i += 1
        
        # Suche von rechts ein Element, welches kleiner als das Pivotelement ist
        while j > links and liste[j].lower() >= pivot:
            j -= 1

        # Daten tauschen, falls i kleiner ist als j, also falls ein Tausch sinnvoll ist
        if i < j:
             temp = liste[i]
             liste[i] = liste[j]
             liste[j] = temp

    # Tausche Pivotelement (liste[rechts]) mit neuer endgültiger Position (liste[i])
    # und gib die neue Position des Pivotelements zurück, beende Durchlauf
    if liste[i].lower() > pivot:
        temp = liste[i]
        liste[i] = liste[rechts]
        liste[rechts] = temp
    
    return i
    

# Testen
# Die Liste wird als globale Variable definiert. Dies dient dazu, dass sie im gesamten Quellcode verfügbar ist und nicht immer übergeben werden muss
global liste
liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print('Unsortierte Liste: ' + str(liste))
quicksort(0, len(liste)-1)
print('Sortierte Liste: ' + str(liste))

