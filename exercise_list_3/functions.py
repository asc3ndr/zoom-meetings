def find_greatest(x, y):
    rafael = ((3 * x) ** 2) + (y ** 2)
    beto = (2 * (x ** 2)) + ((5 * y) ** 2)
    carlos = ((-100) * x) + (y ** 3)

    if rafael > beto and rafael > carlos:
        return "Rafael"
    elif beto > rafael and beto > carlos:
        return "Beto"
    else:
        return "Carlos"


N = int(input())

for case in range(N):
    x, y = [int(x) for x in input().split()]

    print(f"{find_greatest(x, y)} ganhou")

