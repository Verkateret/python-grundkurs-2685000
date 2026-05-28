from bank_account.jugendbankaccount import JugendBankkonto

def main():
    # Testen des JugendBankAccounts
    jugend_konto = JugendBankkonto("Max Mustermann Junior", "50")
    print(jugend_konto)
    jugend_konto.einzahlen(100)

    try:
        jugend_konto.abheben(30)
    except ValueError as e:
        print(e)

    try:
        jugend_konto.abheben(20)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()