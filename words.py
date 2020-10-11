import random

random.seed()


def get_words():
    """Hjelpetekst!"""
    words = [
        "dogs",
        "elephant",
        "pencil",
        "mouse",
        "jazzist",
        "dancer",
        "accident",
        "building",
        "orchid",
        "bamboo",
        "hangman",
        "orangutan",
        "gorilla",
        "mountain",
        "pineapple",
        "window",
        "hurricane",
        "folder",
        "border",
        "literature",
        "throne",
        "computer",
        "binary",
        "number",
        "galaxies",
    ]
    return random.choice(words)
