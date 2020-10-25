import matplotlib.pyplot as plt

plt.autoscale(True)
plt.plot(
    [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300],
    [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300],
)
plt.plot(
    [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300],
    [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 220, 230],
)
plt.xlabel("N")
plt.ylabel("Time in seconds")
plt.show()

