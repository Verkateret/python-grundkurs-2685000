from bank_account.account import BankAccount

class JugendBankkonto(BankAccount):
    """Eine spezifische Klasse JugendBankkonto die von der allgemeinen Klasse BankAccount erbt"""
    def abheben(self, betrag: float) -> None:
        """Verringert den Kontostand um den Angegebenen Betrag,
        wenn genügend Guthaben vorhanden ist und der Betrag nicht über 50 Euro liegt."""
        if betrag <= 25:
            super().abheben(betrag)
        else:
            raise ValueError("Abhebung fehlgeschlagen: Maximalbetrag von 25 EUR überschritten.")
