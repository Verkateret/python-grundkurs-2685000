#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
zahl1 = float(input("Geben Sie ihre 1. Zahl ein: "))
# 2. Benutzer gibt die zweite Zahl ein.
zahl2 = float(input("Geben Sie ihre 2. Zahl ein: "))
# 3. Benutzer wählt die Operation (+, -, *, /).
operator = input("Geben sie den Operator (+, -, *, oder /) ein und drücken Sie Enter um die gewünschte Rechnung auszuführen: ")
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.
if operator == "+":
  ergebnis = zahl1 + zahl2
elif operator == "-":
  ergebnis = zahl1 - zahl2
elif operator == "/":
  ergebnis = zahl1 / zahl2
elif operator == "*":
  ergebnis = zahl1 * zahl2

print(zahl1,operator,zahl2,"=",ergebnis)
# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.
