A, B, C = int(input("First num")), int(input(Second num)), int(input(Third num))
while True:
    if A > B + C or B > A + C or C > A + B:
        print("Not a triangle")
        break
    elif A == B and B == C:
        print("Equilateral triangle")
        break
    elif A == B and B != C or C == B and C != A:
        print("Isosceles triangle")
        break
    elif A != B and B != C:
        print("Scalene triangle")
        break


###################################################################


# def classify_triangle(A, B, C):

#     if A == B == C:
#         print("Equilateral triangle")
#     elif A > (B + C) or B > (C + A) or C > (A + B):
#         print("Not a triangle")
#     elif ((A == C) and A != B) or ((B == C) and B != A) or ((A == B) and A != C):
#         print("Isosceles triangle")
#     elif A != B and A != C and C != B:
#         print("Scalene triangle")


# # classify_triangle(10, 5, 9)

