import os
import words

clear = lambda: os.system("cls" if os.name == "nt" else "clear")
secret_word = list(words.get_words())
hangman_word = ["___" for letter in secret_word]
wrong_guesses = []
num_guesses = 10


while num_guesses > 0 and hangman_word != secret_word:

    print(" ".join(hangman_word))
    print(f"Du har {num_guesses} forsøk igjen.")
    print("\nDu har brukt: " + " ".join(wrong_guesses))

    guessed_letter = input("Guess a letter: ").lower()

    if (guessed_letter in hangman_word) or (guessed_letter in wrong_guesses):
        continue

    for index, letter in enumerate(secret_word):
        if guessed_letter == letter:
            hangman_word[index] = guessed_letter

    if guessed_letter not in secret_word:
        wrong_guesses.append(guessed_letter)
        num_guesses -= 1

    clear()


if hangman_word == secret_word:
    print("Du vant")
else:
    print("Du tapte")
