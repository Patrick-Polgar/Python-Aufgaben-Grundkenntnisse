# ML - Fibonacci-Zahlenfolge

# Die aktuelle Fibonacci-Zahl berechnet sich aus den beiden vorhergehenden Zahlen.
# für die Zahlen 0 und 1 ist definiert, dass das Ergebnis 0 und 1 ist.
def fibonacciRek(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRek(n-1) + fibonacciRek(n-2)
     

def fibonacciIter(n):
    a = 0
    b = 1
    
    for i in range(0, n):
        a, b = b, a + b
        # die obere Zeile kann auch in einzelne Anweisungen zerlegt werden
        # temp = a
        # a = b
        # b = temp + b
        
    return a
    

# Testen der Funktion
print(fibonacciRek(0))
print(fibonacciRek(1))
print(fibonacciRek(2))
print(fibonacciRek(3))
print(fibonacciRek(4))
print(fibonacciRek(5))
print(fibonacciRek(6))
print(fibonacciRek(20))
print(fibonacciIter(20))
print(fibonacciIter(200))
