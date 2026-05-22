#!/usr/bin/python3

# Eingaben über die Kommandozeile
# Einlesen eines Strings
name = input("Bitte geben Sie Ihren Namen ein: ")
print("Hallo, " + name + "!")

# Einlesen eines Integers und Umwandlung
alter = input("Bitte geben Sie Ihr Alter ein: ")
alter = int(alter)  # Umwandlung von String zu Integer
print("Sie sind", alter, "Jahre alt.")
print("Sie sind " + str(alter) + " Jahre alt.")  # Alternative mit String-Konkatenation

# Berechnung mit der Eingabe
jahre_bis_30 = 30 - alter
if jahre_bis_30 > 0:
    print("In", jahre_bis_30, "Jahren werden Sie 30 Jahre alt sein.")
else:
    print("Sie sind bereits 30 Jahre alt oder älter.")

# Benutzer wird nach Lieblingsfilm gefragt
lieblingsfilm = input("Was ist Ihr Lieblingsfilm?\n>")

# Benutzer wird nach Lieblingszahl gefragt
lieblingszahl = int(input("Was ist Ihre Lieblingszahl?\n>"))

# Adition mit 14.5 und personalisiert Nachricht
ausgabezahl = lieblingszahl + 14.5
print("Hallo", name, "Ihr Lieblingsfilm ist", lieblingsfilm, "und Ihre Lieblingszahl addiert mit 14.5 ergibt", ausgabezahl)

