minScore = int(input("Enter the minimal score required: "))
score = input(
    "Enter scores sparated by space"
).split()  # using split to create a list with inputs
lst = []
summ
for (
    i
) in (
    score
):  # converting from string to int with using another list, but only if i is greater than minScore.
    if i > minScore:
        lst.append(i)
for x in lst:  # standard adding and averaging.
    summ = summ + x
avg = summ / len(lst)
print(
    round(avg, 2)
)  # not sure if necessary, but I chose to limit to 2 decimals because that makes sense to me.

