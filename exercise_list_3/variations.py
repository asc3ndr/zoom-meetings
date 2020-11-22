T = int(input())

leetspeak = ["A", "E", "I", "O", "S"]

for case in range(T):

    S = input()
    variations = 1

    for letter in S:
        if letter.upper() in leetspeak:
            variations *= 3
        else:
            variations *= 2

    print(variations)

