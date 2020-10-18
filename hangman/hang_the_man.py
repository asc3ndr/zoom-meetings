import words
import os
import random

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

clear()


class font_color:
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    NOCOL = "\033[0m"
    YELLOW = "\033[33m"


def create_header(color):
    """
    Prints the header in a color specified as an agrument
    """
    print(color)
    print("  _    _          _   _  _____ __  __          _   _ ")
    print(" | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |")
    print(" | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |")
    print(" |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |")
    print(" | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |")
    print(" |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|")
    print(font_color.NOCOL)


### THE GAME ###


def print_play_area(word, history):
    create_header(font_color.CYAN)
    print(f"Your word: ", end=" ")
    for index in range(0, len(word)):
        if word[index] in history:
            print(word[index], end=" ")
        elif index == 0:
            print(word[index], end=" ")
        else:
            print("___", end=" ")
    print("\n")
    print("Wrong characters:", end=" ")
    for letter in history:
        if letter not in word:
            print(letter, end=" ")
    print("\n")


def increment_guess_count(word, userinput, wrong_g, hp):
    if userinput not in word:
        hp.pop(0)
        guess_count = wrong_g = wrong_g + 1
        return guess_count
    else:
        return wrong_g


def show_health_bar(hp):
    print("HP:", end=" ")
    for heart in hp:
        print(font_color.RED + heart, end=" ")
    print(font_color.NOCOL + "\n")


def check_winner(word, guessed_letters):
    temp = word.copy()
    temp.pop(0)  # Removes the first character before comparison
    result = True
    for letter in temp:
        if letter not in guessed_letters:
            result = False
    return result


def verified_input(userinput, history):
    if userinput.isalnum() and userinput not in history and len(userinput) == 1:
        return True
    return False


def play():
    word = list(words.get_words().upper())
    wrong_guesses = 0
    history = []
    hp = 10
    health_bar = [heart for heart in "♥" * hp]
    clear()
    print_play_area(word, history)  # Prints the starting play area
    show_health_bar(health_bar)
    while wrong_guesses < hp and not check_winner(word, history):
        user_input = input("Input one character: ").upper()

        while not verified_input(user_input, history):
            print(font_color.RED + "Wrong input! Try again" + font_color.NOCOL)
            user_input = input("Input one character: ").upper()
        history.append(user_input)
        clear()
        print_play_area(word, history)
        wrong_guesses = increment_guess_count(
            word, user_input, wrong_guesses, health_bar
        )  # Increment count and also removes one life (heart)
        show_health_bar(health_bar)

    if check_winner(word, history):
        print(font_color.GREEN + "Congratulations, you have won!" + font_color.NOCOL)
    else:
        print(
            font_color.RED
            + "Game Over! Try again! The word was: "
            + " ".join(word).replace(" ", "")
            + font_color.NOCOL
        )
    replay = input("Want to play again? (y/n):")
    if replay == "y":
        play()


play()
