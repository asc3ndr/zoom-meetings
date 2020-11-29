T = int(input())

for case in range(T):
    C, D = [int(x) for x in input().split()]

    if C == 0 and D == 0:
        print(0)
    else:
        print(26 ** C * 10 ** D)
