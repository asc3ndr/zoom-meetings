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


def print_winner(running_times: list):
    times = [(value, index + 1) for index, value in enumerate(running_times)]

    for i in range(3):
        lowest = times[i]

        for j in range(i, len(times)):
            if times[j] < lowest:
                lowest = times[j]
                times[i], times[j] = times[j], times[i]

        times[i] = lowest

    print(f"Gold medal: runner {times[0][1]} with {times[0][0]}s")
    print(f"Silver medal: runner {times[1][1]} with {times[1][0]}s")
    print(f"Bronze medal: runner {times[2][1]} with {times[2][0]}s")


print_winner([9000, 5000, 4900, 8000, 3781])

                  
###################################################################
                  
                  
def print_winner(running_times: list):
    times = [(value, index + 1) for index, value in enumerate(running_times)]
    winners = [0, 1, 2]

    for i in range(3):
        lowest = 0

        for j in range(len(times)):
            if lowest == 0 or (times[j] < lowest and times[j] not in winners):
                lowest = times[j]

        winners[i] = lowest

    print(f"Gold medal: runner {winners[0][1]} with {winners[0][0]}s")
    print(f"Silver medal: runner {winners[1][1]} with {winners[1][0]}s")
    print(f"Bronze medal: runner {winners[2][1]} with {winners[2][0]}s")


print_winner([9000, 5000, 4900, 8000, 3781])

                  
###################################################################                  
# Steffen R
                  
times = [9000, 5000, 4900, 8000, 3781]

def medals(lst):
    copy = [[i + 1, time] for i, time in enumerate(lst)]
    for i in range(len(copy)):
        sorted = True
        for j in range(len(copy)-i-1):
            if copy[j+1][1] < copy[j][1]:
                copy[j], copy[j+1] = copy[j+1], copy[j]
                sorted = False
        if sorted:
            break
    print(f"Gold medal: runner {copy[0][0]} with {copy[0][1]}s")
    print(f"Silver medal: runner {copy[1][0]} with {copy[1][1]}s")
    print(f"Bronze medal: runner {copy[2][0]} with {copy[2][1]}s")

medals(times)
