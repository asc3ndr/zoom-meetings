def find_smallest(num_liste: list):
    smallest = num_liste[0]

    for num in num_liste:
        smallest = num if num < smallest else smallest

    return smallest


print(find_smallest([100, 105]))

