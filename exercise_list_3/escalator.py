while True:
    N = int(input())

    if N == 0:
        break

    t = [int(time) for time in input().split()]
    seconds = 0

    if N == 1:
        seconds += 10
    else:
        for index, time in enumerate(t):
            try:
                difference = t[index + 1] - time

                if difference < 10:
                    seconds += difference
                else:
                    seconds += 10
            except:
                seconds += 10
                break

    print(seconds)

