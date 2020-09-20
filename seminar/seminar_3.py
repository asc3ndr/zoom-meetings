# Write a program that, given a name and the force in Newtons applied to
# try to lift the Thunder Hammer, inform the person succeeded in lifting it.

#  Each test case begins with one word, which is the first name of who is trying to raise Mjölnir, and an integer N (1 ≤ N ≤ 25000), indicating the force applied upward in Newtons to pull the hammer off to try to lift it.
# Output

# For each test case, print True if the person managed to raise the hammer,
# or False if he couldn't. (Hint: Only Thor can do it!)


# Input Sample 	Output Sample
# Hulk 5000     False
# Tony 1000     False
# Thor 50       True
# Steve 500	    False

# 1 boolean expression
name, force = input().split()

print(name.lower() == "thor")

# 2 if / else
if name == "thor":
    print(True)
else name == "hulk":
    print(False)
    
# 3 Walrus Operator
print((name := input() == "thor"))
