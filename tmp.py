# 1. Ta inn et variabel n (heltall)
n = int(input())

# 2. Skriv ut successor n+1
print(n + 1)

# Input: 7 14 106

n = "7 14 106"
n1 = n[2:4]
print(n1)

# Lister
en_liste = [2, 4, "a", "x", 2.543]  # kontainer som holder andre verdier

en_liste[3]  # Index starter alltid på 0

# Split
"7;14;106".split(";")

a, b, c = ["7", "14", "106", "4"]

en_liste = input().split()

# Slice
et_input = "7 14 106"  # En string
et_input[2:4]  # Fra : til
et_input[:4]  # Fra 0 : til
et_input[0:]  # Fra Fra : til enden

# abs
# EKSEMPEL "URI 1013" THE GREATEST

# Format
var = "P"
f"{var}ekst" == var + "ekst"
"{0}ekst".format(var)

var = "en"
f"Dette er {var} tekst"
"Dette er {0} tekst".format(var)

# replace
tekst = "Hello, World!"
print(tekst.replace("H", "J"))

tekst = "Hello, World!"
tekst = tekst.replace("H", "J")

# Math
import math

tall = 10
math.sqrt(tall)

# String
from string import ascii_letters

"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# map

list(map(int, input().split()))
[int(x) for x in input().split()]


# list comprehension

[] = Lag ny liste
int(x) for x = For løkke
in input().split() = liste


gammel_liste = input().split()
ny_liste = []

for x in gammel_liste:
    ny_liste.append(int(x))


ny_liste = [int(x) for x in input().split()]

[int(x)**0.5 for x in ['1', '2', '3', '4', '5', '6', '7', '8']]

# [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903]
# ['1', '2', '3', '4', '5', '6', '7', '8']
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

