#!/usr/bin/env python3

# Bedingte Anweisungen in Python

# Variablen
x = 10
y = 5

# Einfache if-Bedingung
if x > y:
  print("x ist grösser als y")

# if-else-Bedingung
if x <= y:
  print("x ist kleiner als y")
else:
  print("x ist nicht kleiner als y")

if x == y:
  print("x ist gleich y")
elif x > y:
  print("x ist grösser als y")
else:
  print("x ist kleiner als y")

zahl1 = 5
zahl2 = 7
zahl3 = 14

if(zahl1>zahl2 and zahl3<zahl2):
  print("zahl1 ist grösser als zahl2 und zahl3 ist kleiner als zahl2")


if(zahl2>zahl3 or zahl2<zahl1):
  print("zahl2 ist entweder grösser als zahl3 oder kleiner als zahl1")
