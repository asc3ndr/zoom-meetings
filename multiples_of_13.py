# 1. Les inn 2 integers X og Y
x = int(input())
y = int(input())

# 2. Kalkuler summen av alle tall som ikke er delelig med 13 mellom de.
#       Inkludert X og Y

teller = 0
summen = x + y

if x > y:
    x, y = y, x

for index in range(x, y + 1):
    if not index % 13 == 0:
        teller = teller + index

# 3. print output
print(teller)
