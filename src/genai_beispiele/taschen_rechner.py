# Klasse TasschenRechner
# Beispiel für eine Klasse, die eine einfache Taschenrechner-Funktionalität 
# bereitstellt. Die Klasse enthält die Methoden add, sub, mul und div. Bei
# der Division soll eine Division durch 0 abgefangen werden und eine Exception
# geworfen werden. Der Taschenrechner beinhaltet die letzeten drei Rechnungen
# Ergebnise in seinem Speicher und können abefragt werden.
# Die Klasse soll mit unit tests getestet werden.

"""Taschenrechner mit Speicher für die letzten drei Rechnungen."""

from collections import deque
from typing import Deque, Dict, List, Union

Number = Union[int, float]


class Taschenrechner:
    """Ein einfacher Taschenrechner mit kleinem Verlaufsspeicher."""

    def __init__(self) -> None:
        self._memory: Deque[Dict[str, Number]] = deque(maxlen=3)

    def _remember(self, operation: str, left: Number, right: Number, result: Number) -> Number:
        self._memory.append(
            {
                "operation": operation,
                "left": left,
                "right": right,
                "result": result,
            }
        )
        return result

    def add(self, left: Number, right: Number) -> Number:
        return self._remember("add", left, right, left + right)

    def sub(self, left: Number, right: Number) -> Number:
        return self._remember("sub", left, right, left - right)

    def mul(self, left: Number, right: Number) -> Number:
        return self._remember("mul", left, right, left * right)

    def div(self, left: Number, right: Number) -> Number:
        if right == 0:
            raise ZeroDivisionError("Division durch 0 ist nicht erlaubt")
        return self._remember("div", left, right, left / right)

    def get_memory(self) -> List[Dict[str, Number]]:
        """Gibt die gespeicherten Rechnungen in chronologischer Reihenfolge zurück."""
        return list(self._memory)

    def memory(self) -> List[Dict[str, Number]]:
        """Alias für die Speicherabfrage."""
        return self.get_memory()