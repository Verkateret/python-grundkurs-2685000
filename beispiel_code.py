#!/usr/bin/env python3

def aendere_immutable_variable(x: int):
    print(f"Ursprünglicher Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")
    x += 10
    print(f"Geänderter Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")
    return x

zahl = 20
print(f"Vor Funktionsaufruf (immutable): {zahl}")
print(f"    Speicheradresse: {id(zahl)}")
zahl = aendere_immutable_variable(zahl)
print(f"Nach Funktionsaufruf (immutable): {zahl}")
print(f"    Speicheradresse: {id(zahl)}")