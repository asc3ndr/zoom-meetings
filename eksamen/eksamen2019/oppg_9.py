def print_matrix(rows, columns):

    print("*" * columns)

    for row_num in range(rows - 2):
        print("*", " " * (columns - 2), "*", sep="")

    print("*" * columns)


print_matrix(5, 10)

