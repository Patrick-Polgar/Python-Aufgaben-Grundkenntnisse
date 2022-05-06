# ML - Bubblesort

def bubblesort(liste):
    i = len(liste)-1
    
    # Äußere Schleife, diese läuft solange bis das erste Element sortiert ist
    while i > 0:
        # Für die Innere Schleife muss immer wieder vorne angefangen werden
        j = 0
        # Die Innere Schleife läuft ab Index 0 bis einen Index vor den schon sortierten Werten
        while j < i:
            if (liste[j].lower() > liste[j+1].lower()):
                # Vertauschen von index j und j+1
                element = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = element
            
            j += 1
        
        i -= 1
        
    return liste
    

# Testen
liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print(bubblesort(liste))