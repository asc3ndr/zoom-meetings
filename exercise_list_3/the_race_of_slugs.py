while True:
    try:
        L = int(input())
        V = [int(speed) for speed in input().split()]

        fastest = max(V)

        if fastest >= 20:
            print(3)
        elif fastest >= 10 and fastest < 20:
            print(2)
        else:
            print(1)

    except EOFError:
        break

