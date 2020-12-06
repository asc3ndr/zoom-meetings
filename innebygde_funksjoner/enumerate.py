text = ["en", "string"]


def my_enumerate(iterable):
    result = list(iterable)

    for i in range(len(iterable)):
        result[i] = (i, iterable[i])
    return result


print(my_enumerate(text))

