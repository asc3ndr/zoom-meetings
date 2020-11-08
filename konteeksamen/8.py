N = input().split()
lst = []

for i in N:
    lst.append(int(i))
i = 3

while i > 0:
    for x in lst:
        if i == 3 and x == min(lst):
            print("Gold medal: runner", lst.index(x), "with", x, "s"
            lst.remove(x)
            i = i - 1
        elif i == 2 and x == min(lst):
            print("Silver medal: runner", lst.index(x), "with", x, "s"
            lst.remove(x)
            i = i - 1
        elif i == 1 and x == min(lst):
            print("Bronze medal: runner", lst.index(x), "with", x, "s"
            lst.remove(x)
            i = i - 1


###################################################################


def print_winner(running_times):

    winners = []
    for i in range(3):
        time = min(running_times)
        runner = running_times.index(time) + 1
        running_times.remove(time)
        winners.append((runner, time))

    print(f"Gold medal: runner {winners[0][0]} with {winners[0][1]}s")
    print(f"Silver medal: runner {winners[1][0]} with {winners[1][1]}s")
    print(f"Bronze medal: runner {winners[2][0]} with {winners[2][1]}s")


print_winner([9000, 5000, 4900, 8000, 3781])

