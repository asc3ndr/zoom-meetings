# Ask the user to enter two integer numbers.
# If the first number is divisible by the second, print True,
# otherwise print False.
tall1 = int(input())
tall2 = int(input())

# Samples:
# Input 3  5  Output False
# Input -20  4  Output True
# Input 5  1 Output True

if tall1 % tall2 == 0:
    print(True)
else:
    print(False)
