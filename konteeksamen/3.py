# first, n = map(int, input("Enter two positive integers separated with space").split(' '))
# if first > 0 or n > 0:
#     print("You can only enter positive integeres.") # checks that the input is positive.
# while n < 0:
#     for i in range(1, first + 1):  # the idea is that hopefully this would loop while n is above 0.
#     summen = 0
#         if i == 11:  # this checks if i has reached 11, and if it has, it prints a newline and adds one to "first"
#             print("\n")
#             first = first + 1
#         else:
#             summen == first * i  # this is the core of the function, the part that does the multiplication.
#             print(first, "*", i, "=", summen)  # This is the output.
#         n = n - 1  # counter


###################################################################

# first, n = map(
#     int, input("Enter two positive integers separated with space").split(" ")
# )

# if first < 0 or n < 0:
#     print("You can only enter positive integeres.")

# while n > 0:
#     for i in range(1, first + 1):
#         summen = 0

#         if i == 11:
#             print("\n")
#             first = first + 1
#         else:
#             summen == first * i
#             print(first, "*", i, "=", summen)
#         n = n - 1

###################################################################


def print_multiplication_table(first, n):
    for i in range(1, 12):
        print(f"{first} * {i} = {first * i}")

    print("")
    successor = first + (n - 1)

    for i in range(1, 12):
        print(f"{successor} * {i} = {successor * i}")


print_multiplication_table(5, 2)

