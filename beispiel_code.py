x = 10
print(f"x: {x}, Speicheradresse: {id(x)}")
x += 5
print(f"x: {x}, Speicheradresse: {id(x)}")

s = "Hallo"
print(f"s: {s}, Speicheradresse: {id(s)}")
s += " Welt"
print(f"s nach Änderung: {s}, Speicheradresse: {id(s)}")

# Immutable Variablen:
# - Integer
# - Float
# - String
# - Tuple
# - Bytes
# - Frozenset