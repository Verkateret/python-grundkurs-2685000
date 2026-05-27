#!/usr/bin/env python3

# Einführung in Klassen in Python

class Buch:
    """Eine einfache Klasse zur Darstellung eines Buches im Bücherregal."""

    def __init__(self, titel: str, autor: str):
        """Initialisiert das Buch mit einem Titel und einem Autor."""
        self.titel = titel  # Öffentliches Attribut
        self.autor = autor  # Öffentliches Attribut
        self._status = "verfügbar"  # Nicht öffentliches Attribut, das den Ausleihstatus des Buches angibt

    def ausleihen(self):
        """Markiert das Buch als ausgeliehen, wenn es verfügbar ist."""
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits ausgeliehen.")

    def zurueckgeben(self):
        """Markiert das Buch als verfügbar."""
        if self._status == "ausgeliehen":
            self._status = "verfügbar"
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits verfügbar.")

    def get_status(self) -> str:
        """Gibt den aktuellen Ausleihstatus des Buches zurück."""
        return self._status

class Buecherregal:
    """Eine Klasse zur Verwaltung eines Bücherregals."""

    def __init__(self):
        """Initialisiert das Bücherregal als leeres Regal."""
        self._buecher = []  # Privates Attribut, das eine Liste von Büchern speichert

    def buch_hinzufuegen(self, buch: Buch):
        """Fügt ein Buch zum Bücherregal hinzu."""
        self._buecher.append(buch)
        print(f"Das Buch '{buch.titel}' wurde dem Regal hinzugefügt.")

    def buch_entfernen(self, buch: Buch):
        """Entfernt ein Buch aus dem Bücherregal."""
        if buch in self._buecher:
            self._buecher.remove(buch)
            print(f"Das Buch '{buch.titel}' wurde aus dem Regal entfernt.")
        else:
            print(f"Das Buch '{buch.titel}' ist nicht im Regal.")

    def alle_buecher_anzeigen(self):
        """Zeigt alle Bücher im Bücherregal an."""
        if self._buecher:
            print("Bücher im Regal:")
            for buch in self._buecher:
                status = buch.get_status()
                print(f" - {buch.titel} von {buch.autor} (Status: {status})")
        else:
            print("Das Bücherregal ist leer.")

# Erstellung von Büchern
buch1 = Buch("Der Hobbit", "J.R.R. Tolkien")
print("Titel lautet", buch1.titel)  # Zugriff auf das öffenliche Attribut 'titel'
buch2 = Buch("1984", "George Orwell")
print("Autor lautet", buch2.autor)  # Zugriff auf das öffenliche Attribut 'autor'
print("Status lautet", buch2.get_status())  # Zugriff auf das private Attribut 'status' durch eine Methode
print("Status lautet", buch2._status)  # 'Fehler': Zugriff auf ein privates Attribut

regal = Buecherregal()
regal.buch_hinzufuegen(buch1)
regal.buch_hinzufuegen(buch2)

regal.alle_buecher_anzeigen()