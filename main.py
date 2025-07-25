from art import logo
import random

def game():
    def set_difficulty(easy_or_hard):
        if easy_or_hard == "easy":
            return 10
        else:
            return 5

    def random_number():
        return random.randint(1,99)

    def compare(u_guess):
        if u_guess == number_to_guess:
            return "a"
        elif u_guess > number_to_guess:
            return "b"
        elif u_guess < number_to_guess:
            return "c"

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print()

    print("I'm thinking of a number between 1 and 100")
    number_to_guess = random_number()
    print()

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print()
    lives = set_difficulty(difficulty)

    game_over = False
    while not game_over:
        print(f"You have {lives} attempt(s) remaining to guess the number")
        guess = int(input("Make a guess: "))
        print()

        if compare(guess) == "a":
            game_over = True
            print("\n" * 5)
            print(f"You got it! The number is '{number_to_guess}'")
        elif compare(guess) == "b":
            lives -= 1
            print("Too high")
        else:
            lives -= 1
            print("Too low")

        if lives == 0:
            game_over = True
            print("\n" * 5)
            print(f"The number is '{number_to_guess}'")
        print()

while input("You want to play? 'y' or 'n': ").lower() == "y":
    print("\n" * 50)
    game()