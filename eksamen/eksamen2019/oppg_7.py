def find_num_in_list(num_liste, num):

    for index, value in enumerate(num_liste):
        if value == num:
            return index

    return -1


print(find_num_in_list([-124, -18, 0], 1.1))
