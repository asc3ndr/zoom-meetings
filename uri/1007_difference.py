# 1 les inn 4 int verdier A,B,C,D
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 2 kalkuler "difference" av produktet A og B med produktet C og  D
# (A * B - C * D)
difference = (A * B) - (C * D)

# 3 print resultatet
print(f"DIFERENCA = {difference}")
print("DIFERENCA = %d" % difference)
print("DIFERENCA = {0}".format(difference))
print("DIFERENCA =", difference)
print("DIFERENCA = " + str(difference))

print(help(print))
