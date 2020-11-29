C = int(input())

for case in range(C):

    name, N = input().split()
    N = int(N)

    print("Y" if name.lower() == "thor" else "N")
