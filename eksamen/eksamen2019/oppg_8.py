def find_number(string):
    number = [int(symbol) for symbol in string if symbol.isnumeric()]

    number = []
    for symbol in string:
        if symbol.isnumeric():
            number.append(int(symbol))

    return sum(number)


print(find_number("Ab23s249ttu21"))

