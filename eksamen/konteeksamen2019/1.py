N, A = str(input("enter first name")), str(input("enter last name"))
Exam = "Happy Exam!"

print(Exam, N, A, sep="\n")


###################################################################


def split_name(string):
    last_index = 0
    result = []

    for index, value in enumerate(string):
        if value == " ":
            result.append(string[last_index:index])
            last_index = index + 1

    result.append(string[last_index:])
    return result


name = input()
print("Happy Exam!", *split_name(name), sep="\n")


###################################################################

# Steffen R

name = input('Name: ')

nameString = name.replace(' ', '\n')

print("Happy Exam!")
print(nameString)
