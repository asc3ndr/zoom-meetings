def find_number(string):
    number = [int(symbol) for symbol in string if symbol.isnumeric()]
    return sum(number)


print(find_number("Ab23s249ttu21"))

