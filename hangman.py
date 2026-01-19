import random

words = ["python", "coding", "alpha", "intern", "script"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")
print("_ " * len(word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        continue

    if guess in guessed_letters:
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("You won!")
        break

if attempts == 0:
    print("Game Over. Word was:", word)
