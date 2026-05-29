# Implementierung eines Schere Stein Papier Spiels. Ein User spielt gegen den 
# Computer. Der Computer wählt zufällig ein Element. Der User wird aufgefordert
# ein Element zu wählen. Das Spiel läuft einmal durch. Dannach wird der Gewinner
# bekannt gegeben.

def schere_stein_papier():
    import random

    # Mögliche Optionen
    optionen = ["Schere", "Stein", "Papier"]

    # User wählt eine Option
    print("Willkommen zum Schere Stein Papier Spiel!")
    while True:
        user_wahl = input("Wähle Schere, Stein oder Papier: ").strip().capitalize()

        if user_wahl in optionen:
            break

        print("Ungültige Eingabe! Bitte Schere, Stein oder Papier wählen.")

    # Computer wählt zufällig eine Option
    computer_wahl = random.choice(optionen)

    print(f"Computer wählt: {computer_wahl}")

    # Bestimmen des Gewinners
    if user_wahl == computer_wahl:
        return "Unentschieden!"
    elif (user_wahl == "Schere" and computer_wahl == "Papier") or \
         (user_wahl == "Stein" and computer_wahl == "Schere") or \
         (user_wahl == "Papier" and computer_wahl == "Stein"):
        return "Du gewinnst!"
    else:
        return "Computer gewinnt!"
    
if __name__ == "__main__":
    ergebnis = schere_stein_papier()
    print(ergebnis)