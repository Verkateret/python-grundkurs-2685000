import sys

#Liste von Zahlen
x = [1, 2, 3]

print("Reference count of x:", sys.getrefcount(x))

y = [4, 5, 6]
y.append(x)

print("Reference count of x:", sys.getrefcount(x))

del y
print("Reference count of x after deleting y:", sys.getrefcount(x))