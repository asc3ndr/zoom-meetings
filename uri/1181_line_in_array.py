row = int(input())
operation = input()

array = [[float(input()) for y in range(12)] for x in range(12)]


def row_in_array(array, n):
    return array[n]


def col_in_array(array, n):
    return [array[i][n] for i in range(len(array))]


result = sum(row_in_array(array, row))

if operation == "M":
    result = result / len(array[row])

print(round(result, 1))

