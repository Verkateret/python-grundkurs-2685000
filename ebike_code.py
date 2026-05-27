# Aufgabe:
# Erstellen Sie eine Klasse 'Ebike', die die Eigenschaften 'marke', 'modell' und 'reichweite' hat.
# - Implementieren Sie eine Methode 'tanken', die die Reichweite um einen gegebenen Wert erhöht.
# - Stellen Sie sicher, dass der Tankinhalt privat ist und nur über eine Methode abgefragt werden kann.
# - Instanzieren Sie ein Elektrofahrrad und testen Sie die Methoden.

class Ebike:
    """Eine Klasse zur Darstellung eines Elektrofahrrads"""
    def __init__(self, marke: str, modell: str, reichweite: int):
        """Initialisiert das Elektrofahrrad mit Marke, Modell und Reichweite"""
        self.marke = marke # Öffentliches Attribut
        self.modell = modell # Öffentliches Attribut
        self.__reichweite = reichweite # Privates Attribut, das die aktuelle Reichweite speichert
    
    def tanken(self, zusätzliche_reichweite: int):
        """Erhöht die Reichweite des Elektrofahrrades um einen bestimmten Wert"""
        self.__reichweite += zusätzliche_reichweite
        print(f"Die Reichweite des Rads wurde um {zusätzliche_reichweite} km erhöht.")
    
    def get_reichweite(self):
        """Gibt die aktuelle Reichweite des Elektrofahrrads zurück."""
        return self.__reichweite

# Instanzieren eines Elektrofahrrads
bike1 = Ebike("ENTICE 5+ MOVE", "Kalkhoff", 20)
print("Marke:", bike1.marke)
print("Modell:", bike1.modell)
print("Reichweite:", bike1.get_reichweite())
bike1.tanken(20)
print("Neue Reichweite:", bike1.get_reichweite())
