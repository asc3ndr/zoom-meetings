# 1. Les in en integer i variabel X
X = int(input())

# 2. Lag en løkke som går fra 1 til X
#       Print ut alle oddetall fra 1 til x
for teller in range(1, X + 1):
    if teller % 2 == 1:
        print(teller)

