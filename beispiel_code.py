#!/usr/bin/env python3

# Einführung in Vererbung: Tiere als Beispiel

class Tier:
    """Eine allgemeine Klasse für Tiere."""

    def __init__(self, name: str, alter: int):
        """Initialisiert ein Tier mit einem Namen und einem Alter."""
        print("Ein neues Tier wurde erstellt.")
        self.name = name
        self.alter = alter

    def mache_geraeusch(self):
        """Gibt ein allgemeines Geräusch aus."""
        print(f"Dies ist {self.name}, es ist {self.alter} Jahre alt.")

    def beschreibung(self):
        """Gibt eine Beschreibung des Tieres aus"""
        print(f"Dies ist {self.name}, es ist {self.alter} Jahre alt.")

    def __str__(self) -> str:
        """Gibt eine Beschreibung des Tieres zurück."""
        return f"Tier: {self.name}, Alter: {self.alter}"

class Hund(Tier):
    """Eine spezifische Klasse für Hunde, die von der allgemeinen Klasse Tier erbt."""
    
    def mache_geraeusch(self):
        """Überschreibt die Methode und gibt das typische Geräusch eines Hundes aus."""
        print(f"{self.name} bellt.")

class Katze(Tier):
    """Eine spezifische Klasse für Katzen, die von der allgemeinen Klasse Tier erbt."""
    
    def __init__(self, name: str, alter: int):
        super().__init__(name, alter)
        print("Eine Katze wurde erstellt.")

    def mache_geraeusch(self):
        """Überschreibt die Methode und gibt das typische Geräusch einer Katze aus."""
        print(f"{self.name} miaut.")

hund = Hund("Bello", 5)
katze = Katze("Mia", 3)

hund.mache_geraeusch()

# Aufgabe:
# Erstellen Sie eine weitere spezifische Klasse 'Vogel', die von der allgemeinen Klasse 'Tier' erbt.
# - Überschreiben Sie die Methode 'mache_geraeusch', sodass der Vogel ein typisches Geräusch wie "zwitschern" macht.
# - Erstellen Sie eine Instanz der Klasse 'Vogel' und rufen Sie die Methoden 'beschreibung' und 'mache_geraeusch' auf.

class Vogel(Tier):
    """Eine spezifische Klasse für Vögel, die von der allgemeinen Klasse Tier erbt."""
    
    def mache_geraeusch(self):
        """Überschreibt die Methode und gibt das typische Geräusch eines Vogels aus."""
        print(f"{self.name} zwitschert.")

vogel = Vogel("Piepsi", 2)
vogel.beschreibung()
vogel.mache_geraeusch()
