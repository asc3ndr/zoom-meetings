# 1. Les inn en start tid og en slutt tid i timer
start, end = [int(x) for x in input().split()]

# 2. Kalkuler spilltid. Merk: tiden kan starte på en dag og slutte på en annen

# hvis b > a: abs(a - b)
if end > start:
    spilltid = abs(start - end)
# hvis a > b: 24 - a + b
else:
    spilltid = 24 - start + end

# 3. Print med formatet “O JOGO DUROU X HORA(S)”
print(f"O JOGO DUROU {spilltid} HORA(S)")

