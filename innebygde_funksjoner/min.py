numbers = [10, 4, 67, 1, 19]


def my_min(iterable):
    lowest = iterable[0]
    for i in range(1, len(iterable)):
        if iterable[i] < lowest:
            lowest = iterable[i]
    return lowest


print(my_min(numbers))
