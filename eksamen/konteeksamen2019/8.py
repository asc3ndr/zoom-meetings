# N = input().split()
# lst = []

# for i in N:
#     lst.append(int(i))
# i = 3

# while i > 0:
#     for x in lst:
#         if i == 3 and x == min(lst):
#             print("Gold medal: runner", lst.index(x), "with", x, "s"
#             lst.remove(x)
#             i = i - 1
#         elif i == 2 and x == min(lst):
#             print("Silver medal: runner", lst.index(x), "with", x, "s"
#             lst.remove(x)
#             i = i - 1
#         elif i == 1 and x == min(lst):
#             print("Bronze medal: runner", lst.index(x), "with", x, "s"
#             lst.remove(x)
#             i = i - 1


###################################################################

# Med innebygde funksjoner
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


# Uten innebygde. Basert på selection sort.
def print_winner(running_times: list):
    times = [(value, index) for index, value in enumerate(running_times, 1)]

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


# print_winner([9000, 5000, 4900, 8000, 3781])


# ###################################################################
# Steffen R

times = [9000, 5000, 4900, 8000, 3781]


def medals(lst):
    copy = [[i + 1, time] for i, time in enumerate(lst)]
    for i in range(len(copy)):
        sorted = True
        for j in range(len(copy) - i - 1):
            if copy[j + 1][1] < copy[j][1]:
                copy[j], copy[j + 1] = copy[j + 1], copy[j]
                sorted = False
        if sorted:
            break

    print(f"Gold medal: runner {copy[0][0]} with {copy[0][1]}s")
    print(f"Silver medal: runner {copy[1][0]} with {copy[1][1]}s")
    print(f"Bronze medal: runner {copy[2][0]} with {copy[2][1]}s")


# medals(times)


###################################################################
# # Joar


def who_is_top_three1(list_of_results):
    winner = [0, 0]
    second = [0, 0]
    third = [0, 0]

    for i, x in enumerate(list_of_results):
        if winner == [0, 0] or x < winner[1]:
            winner[0], second[0], third[0] = i + 1, winner[0], second[0]
            winner[1], second[1], third[1] = x, winner[1], second[1]

        elif second == [0, 0] or x < second[1]:
            second[0], third[0] = i + 1, second[0]
            second[1], third[1] = x, second[1]

        elif third == [0, 0] or x < third[1]:
            third[0] = i + 1
            third[1] = x

    print(f"Gold medal: runner {winner[0]} with {winner[1]}s")
    print(f"Silver medal: runner {second[0]} with {second[1]}s")
    print(f"Bronze medal: runner {third[0]} with {third[1]}s")

