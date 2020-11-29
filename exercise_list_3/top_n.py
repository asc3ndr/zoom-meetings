K = int(input())
kategorier = [1, 3, 5, 10, 25, 50, 100]

for interval in kategorier:
    if K <= interval:
        print(f"Top {interval}")
        break
