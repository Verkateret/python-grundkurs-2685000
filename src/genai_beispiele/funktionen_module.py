# Ping Pong Funktion
# Erstelle eine Funktion die als Parameter eine Zahl erhält.
# Ist die Zahl ein Vielfaches von 3, so soll die Funktion "Ping" zurückgeben. Ist
# die Zahl ein Vielfaches von 5, so soll die Funktion "Pong" zurückgeben. Ist die
# Zahl ein Vielfaches von 3 und 5, so soll die Funktion "Ping Pong" zurückgeben.
# Ansonsten gibt die Zahl zurück. Erstelle Unit Tests für die Funktion.
from typing import Union


def ping_pong(zahl: int) -> Union[int, str]:
	"""Gibt je nach Teilbarkeit einen String zurück.

	- Bei Vielfach von 3 und 5: "Ping Pong"
	- Bei Vielfach von 3: "Ping"
	- Bei Vielfach von 5: "Pong"
	- Ansonsten die ursprüngliche Zahl

	Parameter:
	zahl: int - die zu prüfende Zahl
	"""
	if zahl % 3 == 0 and zahl % 5 == 0:
		return "Ping Pong"
	elif zahl % 3 == 0:
		return "Ping"
	elif zahl % 5 == 0:
		return "Pong"
	else:
		return zahl

# Listen Invertieren
# Erstelle eine Funktion die als Parameter eine Liste erhält. Die Funktion soll
# die Liste invertieren und zurückgeben. Beispiel: [1, 2, 3] -> [3, 2, 1].
# Erstelle Unit Tests für die Funktion.
from typing import List

def listen_invertieren(werte: List[int]) -> List[int]:
	"""Gibt eine invertierte Kopie der Liste zurück.
	    Args:
        liste (list): Die zu invertierende Liste.
    Returns:
        list: Die invertierte Liste.
    """
	return list(reversed(werte))

# Finde den Höchsten zahlenwert Unabhängig vom Vorzeichen
# Erstelle eine Funktion die als Parameter eine Liste erhält. Die Funktion soll
# das Element mit dem größten Zahlenwert zurückgeben. Dabei soll der Vorzeichen
# nicht berücksichtigt werden. Beispiel: [1, -2, 3, -4] -> 4. Erstelle Unit Tests.
def hoechster_wert_unabhaengig_vom_vorzeichen(werte: List[int]) -> int:
	"""Gibt den größten Zahlenwert unabhängig vom Vorzeichen zurück.

	Beispiel: [1, -2, 3, -4] -> 4

	Parameter:
	werte: List[int] - Liste mit ganzen Zahlen. Die Liste darf nicht leer sein.

	Raises:
	ValueError: Wenn die Liste leer ist.
	"""
	if not werte:
		raise ValueError("Die Liste muss mindestens ein Element enthalten")
	# Bestimme das Element mit dem größten Betrag und gib dessen Betrag als positiven Wert zurück
	max_abs = max(werte, key=abs)
	return abs(max_abs)