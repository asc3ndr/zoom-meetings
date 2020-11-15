# A, B = int(input("First integer")), int(input("Second integer"))
# X, Z, Y = 0, 0, 0
# while True:
#     if A < B:
#         X = B and Z = A
#         break
#     else:
#         X = A and Z = B
#         break
# for i in range(Z, X + 1):
#     if i % 3 == 1:
#         Y = Y + i
# print(Y)


###################################################################


def divisible_by_three(one, two):

    if one > two:
        one, two = two, one

    prod = 1
    for num in range(one, two + 1):
        if num % 3 == 0 and num & 1:
            prod *= num

    return prod


print(divisible_by_three(100, 106))

