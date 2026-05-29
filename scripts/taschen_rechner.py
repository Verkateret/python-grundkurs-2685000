# Implementiert die Usereingabe und die Ausgabe der Ergebnisse in der Konsole
# für den Taschenrechner in der Klasse TasschenRechner. Das Script soll dauerhaft
# laufen und der User kann die Rechenoperationen und zwei Eingabewerte wählen.
# Der User kann das Script über den Befehlt "exit" beenden. Der User kann den Speicher
# des Taschenrechners über den Befehlt "memory" ausgeben lassen.

"""Ein einfacher Taschenrechner für die Konsole.

Der Benutzer kann Operationen auswählen, zwei Zahlen eingeben,
das Programm mit "exit" beenden und den letzten Wert mit "memory" anzeigen.
"""

from genai_beispiele.taschen_rechner import Taschenrechner


def main() -> None:
	rechner = Taschenrechner()

	while True:
		eingabe = input("Bitte geben Sie 'exit', 'memory' oder eine Rechenoperation ein (z.B. '4 + 7.4'): ").strip().lower()

		if eingabe == "exit":
			print("Programm wird beendet.")
			break

		if eingabe == "memory":
			history = rechner.memory() if callable(getattr(rechner, "memory", None)) else rechner.get_memory()
			print("Vorherige Rechnungen:")
			for item in history:
				print(f"  {item['left']} {item['operation']} {item['right']} = {item['result']}")
			continue

		# Versuche, die Eingabe zu parsen (z.B. "4 + 7.4")
		try:
			# Ersetze Komma durch Punkt für deutsche Zahlen
			eingabe = eingabe.replace(",", ".")
			
			# Finde den Operator
			operator = None
			for op in {"+", "-", "*", "/"}:
				if op in eingabe:
					operator = op
					break
			
			if operator is None:
				print("Ungültige Eingabe. Bitte verwenden Sie das Format: 'Zahl1 Operator Zahl2'")
				continue
			
			# Teile die Eingabe auf
			parts = eingabe.split(operator)
			if len(parts) != 2:
				print("Ungültige Eingabe. Bitte verwenden Sie das Format: 'Zahl1 Operator Zahl2'")
				continue
			
			erste_zahl = float(parts[0].strip())
			zweite_zahl = float(parts[1].strip())
			
			if operator == "+":
				result = rechner.add(erste_zahl, zweite_zahl)
			elif operator == "-":
				result = rechner.sub(erste_zahl, zweite_zahl)
			elif operator == "*":
				result = rechner.mul(erste_zahl, zweite_zahl)
			elif operator == "/":
				result = rechner.div(erste_zahl, zweite_zahl)
			else:
				print("Ungültige Eingabe. Bitte verwenden Sie das Format: 'Zahl1 Operator Zahl2'")
				continue
			print(f"Ergebnis: {result}")
		except ValueError:
			print("Ungültige Eingabe. Bitte verwenden Sie das Format: 'Zahl1 Operator Zahl2'")
		except ZeroDivisionError as exc:
			print(exc)
		except Exception as exc:
			print(exc)


if __name__ == "__main__":
    main()
