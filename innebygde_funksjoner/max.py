numbers = [10, 4, 67, 1, 19]


def my_max(iterable):
    greatest = iterable[0]
    for i in range(1, len(iterable)):
        if iterable[i] > greatest:
            greatest = iterable[i]
    return greatest


print(my_max(numbers))
