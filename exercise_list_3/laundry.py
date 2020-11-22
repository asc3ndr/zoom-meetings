N = int(input())

LA, LB = [int(x) for x in input().split()]
SA, SB = [int(x) for x in input().split()]

L = [int(x) for x in range(LA, LB + 1)]
S = [int(x) for x in range(SA, SB + 1)]

print("possivel" if (N in L) and (N in S) else "impossivel")

#############################################################


# LA, LB = [int(x) for x in input().split()]

# <===>

# new_list = []
# the_input = input().split()

# for x in the_input:
#     new_list.append(int(x))

# LA = new_list[0]
# LB = new_list[1]


# #############################################################

# print("possivel" if (N in L) and (N in S) else "impossivel")

# <===>

# if (N in L) and (N in S):
#     print("possivel")
# else:
#     print("impossivel")

