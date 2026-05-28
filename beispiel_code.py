#!/usr/bin/env python3

liste = [1, 2, 3]
print(f"Liste: {liste}, Speicheradresse: {id(liste)}")

liste.append(4)
print(f"Liste: {liste}, Speicheradresse: {id(liste)}")

dictionary = {"a": 1, "b": 2}
print(f"Dictionary: {dictionary}, Speicheradresse: {id(dictionary)}")
dictionary["c"] = 3
print(f"Dictionary: {dictionary}, Speicheradresse: {id(dictionary)}")

# Mutable Datentypen:
# - Listen (list)
# - Dictionaries (dict)
# - Mengen (set)
# - Bytearrays (bytearray)
# - Benutzerdefinierte Klassen

