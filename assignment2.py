#!/usr/bin/python3
# 1. Get the number of seconds from the users input and store the number in a variable
input_seconds = int(input())


# 2. Convert seconds to the H:M:S format.

# 2.1 convert seconds to hours and save the number in a variable
hours = input_seconds // 3600  # floored => rounded down

# 2.2 convert seconds to minutes and save the number in a variable
minutes = (input_seconds % 3600) // 60

# 2.3 convert seconds to seconds and save the number in a variable
seconds = (input_seconds % 3600) % 60


# 3. print the time using the H:M:S format with the converted variables
print(f"{hours}:{minutes}:{seconds}")


# DIV MOD OPERATORS
# I normal deling blir en dividend delt på en divisor
# og vi står igjen med det som kalles en kvotient og en rest.
# Dividend / Divisor = (kvotient, rest)

# Heltallsdeling ( // )  gir deg kvotienten, og kan sies å
# være det samme som å dele og deretter runde ned.

# Modulo ( % ) gir deg rest, altså tallet
# som blir til overs etter hver divisjon.
