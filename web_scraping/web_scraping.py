import sys, os
import requests
import timeit
from PIL import Image
from bs4 import BeautifulSoup

from json import load, dump

# # Lagre data
# with open("data.json", "w") as file:
#     dump(data, file)


# # Hente data
# data = []

# with open("data.json", "r") as file:
#     data = load(file)

# # Lambda
# min_print = lambda: print(data)

# min_print()

# # PIL Img local
# img = Image.open("/home/rovik/Pictures/fantastisk.png")
# img.show()

# # PIL img remote
# img = Image.open(
#     requests.get("https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg", stream=True).raw
# )
# img.show()


# # Finn storrelse med OS.stat
# print(os.stat("/home/rovik/Pictures/fantastisk.png").st_size)

# # Eksempel framgangsmate
# html = requests.get("https://xkcd.com/1/")
# soup = BeautifulSoup(r.text, "html.parse")

# url = ...

# img = requests.head("https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg")
# print(img.headers)
# print(img.headers.get("content-length"))


# data = [
#     ["241", "navn", "url"],
#     ["512", "navn", "url"],
#     ["135", "navn", "url"],
#     ["765", "navn", "url"],
# ]

# for lst in data:
#     lstint = int(lst[0])
#     lst[0] = lstint


# lst = [[int(number[0]), number[1], number[2]] for number in data]

# print(lst)


def test(nummer):
    for i in range(nummer):
        print(i ** 2)


for i in range(1000):
    start = timeit.default_timer()

    test(100)

    end = timeit.default_timer()

    print(end - start)

