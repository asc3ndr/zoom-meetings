# 1. Hent 3 heltall
a, b, c = input().split()
# a, b, c = [int(x) for x in input().split()]
a, b, c = int(a), int(b), int(c)

# 2. Bruk formel for å regne ut det største tallet
utregning = (a + b + abs(a - b)) / 2
siste_utregning = (utregning + c + abs(utregning - c)) / 2

# 3. Vis det største tallet
print(f"{int(siste_utregning)} eh o maior")
print(f"{siste_utregning:.0f} eh o maior")
print(f"{round(siste_utregning)} eh o maior")
