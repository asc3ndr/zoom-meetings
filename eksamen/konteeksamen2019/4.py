A = int(input("Enter a number to check occurences in list: "))
B = input().split()
lst = []
Z = 0
for i in B:
    lst.append(int(i))
for i in lst:
    if A in lst(i):
        Z += 1
print(Z)


###################################################################


def times_occuring(num, num_list):
    count = 0
    for number in num_list:
        if num == number:
            count += 1

    return count


# print(times_occuring(88, [38, 40, 88, 60, 71, 70, 82, 88]))
