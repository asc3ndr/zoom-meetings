A = float(input())  # Weight: 2
B = float(input())  # Weight: 3
C = float(input())  # Weight: 5

weight = 2 + 3 + 5
A1 = A * 2
B1 = B * 3
C1 = C * 5

# Sjekket online for hvordan man regner ut weight
average = (A1 + B1 + C1) / weight

# Karakterene kan gå fra 0 til og med 10.0
# I output må jeg svare med 1 desimal.
print(f"MEDIA = {average:.1f}")
