N, A = str(input("enter first name")), str(input("enter last name"))
Exam = "Happy Exam!"

print(Exam, N, A, sep="\n")


###################################################################


navn = input()

fornavn = ""
etternavn = ""

for index, letter in enumerate(navn):
    if letter == " ":
        fornavn = navn[:index]
        etternavn = navn[index + 1 :]
        break

print("Happy Exam!", fornavn, etternavn, sep="\n")

