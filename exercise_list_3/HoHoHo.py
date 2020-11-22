N = int(input())

ho = ""
for i in range(N):
    if i == N - 1:
        ho += "Ho"
    else:
        ho += "Ho "

print(ho + "!")

###########################################3

ho = ["Ho" for n in range(int(input()))]
print(" ".join(ho), end="!")

