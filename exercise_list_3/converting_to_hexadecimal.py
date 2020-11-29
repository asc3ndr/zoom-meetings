from string import ascii_uppercase


def my_encoding(N, length):
    symbols = [str(num) for num in range(10)] + list(ascii_uppercase)

    if length < 2 or length > 39:
        raise ValueError("Length size wrong. 2 >= lenght <= 39")

    result = []

    while True:
        if N > length - 1:
            result.insert(0, symbols[N % length])
            N = N // length
        else:
            result.insert(0, symbols[N])
            break

    return "".join(result)


print(my_encoding(65536, 2))  # 65536 (BINARY)
print(my_encoding(65536, 10))  # 65536 (DECIMAL)
print(my_encoding(65536, 16))  # 10000 (HEX)
print(my_encoding(65536, 39))  # 10000 (WHAT?)
