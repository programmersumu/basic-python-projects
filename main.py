import random

def number_guesser():
    random_number = random.randint(1, 100)
    guessed = False

    while not guessed:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            guessed = True
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

number_guesser()