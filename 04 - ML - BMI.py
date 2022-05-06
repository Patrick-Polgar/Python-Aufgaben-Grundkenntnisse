# ML - Übung Einfaches Programm mit Ein- und Ausgabe

# Formel für BMI
def bmi(gewicht, groesse):
    return gewicht / (groesse**2)

# Funktion für Ausgabe
def ausgabe(bmi):
    result = ''

    if bmi < 10:
        result = 'Überprüfen Sie ihre Eingabe'
    elif bmi < 15:
        result = 'Magersucht'
    elif bmi < 20:
        result = 'Untergewicht'
    elif bmi < 25:
        result = 'Normalgewicht'
    elif bmi < 30:
        result = 'Übergewicht'
    elif bmi < 40:
        result = 'Fettsucht'
    elif bmi < 50:
        result = 'morbide Fettsucht'
    else:
        result = 'Überprüfen Sie ihre Eingabe'
        
    return result
    

print('Herzlich Willkommen zur BMI-Berechnung. Bitte geben Sie Kommawerte mit einem Punkt ein.\n')
gewicht = float(input('Bitte geben Sie ihr Gewicht in kg ein: '))
groesse = float(input('Bitte geben Sie ihre Größe in m ein: '))
bmi = bmi(gewicht, groesse)
print('\nIhr berechneter BMI liegt bei: ' + str(bmi))
print('Somit ergibt sich folgende Diagnose: ' + ausgabe(bmi))