#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen Taschenrechner mit ausgelagerten Funktionen.

# 1. Erstellen Sie für jede der Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) eine separate Funktion.
#    - Jede Funktion sollte zwei Argumente (Zahlen) als Eingabe akzeptieren und das Ergebnis der Berechnung zurückgeben.
#    - Die Funktionen sollten klar benannt und gemäß PEP8 formatiert sein.

# 2. Implementieren Sie eine Hauptfunktion (main), die:
#    - Den Benutzer auffordert, zwei Zahlen einzugeben.
#    - Den Benutzer auffordert, die gewünschte Operation auszuwählen (Addition, Subtraktion, Multiplikation, Division).
#    - Die entsprechende Rechenfunktion aufruft und das Ergebnis ausgibt.
#    - Eine Fehlerbehandlung integriert, um ungültige Eingaben und Division durch Null zu vermeiden.

# 3. Stellen Sie sicher, dass Ihr Code PEP8-konform ist:
#    - Verwenden Sie vier Leerzeichen für Einrückungen.
#    - Fügen Sie Leerzeichen um Operatoren ein.
#    - Halten Sie Zeilenlängen unter 79 Zeichen.
#    - Schreiben Sie geeignete Kommentare und verwenden Sie docstrings für Funktionen.

# Beispielablauf:
# - Der Benutzer gibt die Zahlen 10 und 5 ein.
# - Der Benutzer wählt die Operation 'Multiplikation'.
# - Die Funktion zur Multiplikation wird aufgerufen und das Ergebnis (50) wird ausgegeben.

# Optional: 
# - Fügen Sie weitere Funktionen hinzu, wie z.B. Potenzierung oder Modulo.
# - Implementieren Sie eine Schleife, um mehrere Berechnungen hintereinander durchzuführen, bis der Benutzer das Programm beendet.

# Funktionen für die Rechenoperationen
# Funktion für die Addition
def addiere(zahl1: float, zahl2: float) -> float:
    """Zahl 1 und Zahl 2 werden zusammen addiert"""
    return zahl1 + zahl2

# Funktion für die Subtraktion
def subtrahiere(zahl1: float, zahl2: float) -> float:
    """Zahl 2 wird von Zahl 1 subtrahiert"""
    return zahl1 - zahl2

# Funktion für die Multiplikation
def multipliziere(zahl1: float, zahl2: float) -> float:
    """Zahl 1 und Zahl 2 werden miteinander multipliziert"""
    return zahl1 * zahl2

# Funktion für die Division
def dividiere(zahl1: float, zahl2: float) -> float:
    """Zahl 1 wird durch Zahl 2 dividiert. Fehlerbehandlung für Division durch Null."""
    if zahl2 == 0:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        return None
    return zahl1 / zahl2

# Hauptfunktion
def main():
    """Hauptfunktion die den Benutzer durch die Berechnungen führt"""
    try:
        zahl1 = float(input("Geben Sie ihre erste Zahl ein: "))
        zahl2 = float(input("Geben Sie ihre zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.")
        return  
    print("Wählen Sie die Operation:")
    print("+: Addition")
    print("-: Subtraktion")
    print("*: Multiplikation")
    print("/: Division")
    operation = input("Geben Sie zum auswählen das Symbol der gewünschten Operation ein: ")  
    if operation == "+":
        result = addiere(zahl1, zahl2)
        operation_name = "Addition"
    elif operation == "-":
        result = subtrahiere(zahl1, zahl2)
        operation_name = "Subtraktion"
    elif operation == "*":
        result = multipliziere(zahl1, zahl2)
        operation_name = "Multiplikation"
    elif operation == "/":
        result = dividiere(zahl1, zahl2)
        operation_name = "Division"
    else:
        print("Ungültige Operation! Bitte wählen Sie eine gültige Operation aus.")
        return
    if result is not None:
        print(f"Das Ergebnis der {operation_name} von {zahl1} und {zahl2} ist: {result}")    
if __name__ == "__main__":
    main()
