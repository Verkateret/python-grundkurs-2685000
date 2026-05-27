#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

class BankAccount:
    """Eine Klasse zur Darstellung eines einfachen Bankkontos"""
    def __init__(self, inhaber: str, kontonummer: str, start_kontostand: float = 0.0):
        """Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand."""
        self.inhaber = inhaber # Öffentliches Attribut
        self.kontonummer = kontonummer # Öffentliches Attribut
        self.__kontostand = start_kontostand # Nichtöffentliches Attribut, das den aktuellen Kontostand beinhaltet
    def einzahlen(self, betrag: float) -> None:
        """Erhöht den Kontostand um den eingezahlten Betrag"""
        self.__kontostand += betrag
    def abheben(self, betrag: float) -> None:
        """Verringert den Kontostand, bei ausreichendem Saldo, um den abgehobenen Betrag"""
        if betrag > 0:
            if betrag < self.__kontostand:
                self.__kontostand -= betrag
            else:
                print(f"Kontosaldo nicht ausreichend um {betrag}.- CHF abzuheben")
        else:
            print("Abhebung fehlgeschlagen: Betrag muss positiv sein")
    def get_kontostand(self) -> float:
        """Gibt den aktuellen Kontostand zurück"""
        return self.__kontostand
    def __str__(self) -> str:
        """Gibt eine Benutzerfreundliche Darstellung des Kontos zurück"""
        return (
            f"Konto von: {self.inhaber}\n"
            f"Kontonummer: {self.kontonummer}\n"
            f"Aktueller Kontostand: {f'{self.__kontostand:_.2f}'.replace("_", " ")}.- CHF"
        )
    
konto1 = BankAccount("Ramon Stadelmann", "CH 8080 8008 3847 2940 8320", 1)
print(konto1)
konto1.abheben(2)
konto1.einzahlen(999999)
print(f"Aktueller Kontostand: {f'{konto1.get_kontostand():_.2f}'.replace("_", " ")}.- CHF")
