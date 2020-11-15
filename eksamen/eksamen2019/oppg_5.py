def product(num_list):
    result = 1

    for num in num_list:
        result *= num

    return int(result)


print(product([1.5, 20, -1]))

