def aendere_mutable_variable(liste: list):
    print(f"Ursprüngliche Liste in der Funktion (mutable): {liste}")
    print(f"    Speicheradresse: {id(liste)}")
    liste.append(100)
    print(f"Geänderte Liste in der Funktion (mutable): {liste}")
    print(f"    Speicheradresse: {id(liste)}")

meine_liste = [1, 2, 3]
print(f"Vor Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")
aendere_mutable_variable(meine_liste)
print(f"Nach Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")
