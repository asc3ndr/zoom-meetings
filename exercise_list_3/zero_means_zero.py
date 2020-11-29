while True:
    M, N = [int(x) for x in input().split()]

    if M == 0 and N == 0:
        break

    summen = list(str(M + N))

    for index, letter in enumerate(summen):
        if letter == "0":
            summen.pop(index)

    print("".join(summen))
