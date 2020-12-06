text = "dette er text"


def my_split(string):
    result = []
    last_index = 0

    for i in range(len(string)):
        if string[i] == " ":
            result.append(string[last_index:i])
            last_index = i + 1

    result.append(string[last_index:])

    return result


print(my_split(text))

