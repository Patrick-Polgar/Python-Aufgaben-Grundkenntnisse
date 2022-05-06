import doctest

# Finden Sie den Fehler im folgenden Skript
# Hinweis: Es ist 1 synaktischer und 1 semantische Fehler enthalten.
     
def maximum(a,b):
    """ 
    Diese Funktion liefert das Maximum von a und b zurück
    
    Doctests:
    
    >>> maximum(3,4)
    4
    >>> maximum(3,3)
    3
    >>> maximum(5,2)
    5
    >>>
    
    """
    if a > b:
        return a
    else:
        return b

if __name__ == "__main__": 
    doctest.testmod()