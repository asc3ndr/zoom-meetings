def average(num_1, num_2):

    if num_2 < num_1:
        num_1, num_2 = num_2, num_1

    summen = 0
    lengden = 0
    for num in range(num_1, num_2 + 1):
        summen += num
        lengden += 1

    return summen / lengden


print(average(100, 105))
