import random

def nuber_guessing_game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 to 100")

    secret_number = random.randint(1, 10)

    guesses_taken = 0

    while True:

        user_guess = int(input("Take a Guess:- "))
        guesses_taken += 1

        if user_guess < secret_number:
            print("Your guess is too low! Try again.")
        
        elif user_guess > secret_number:
            print("Your guess is High low! Try again.")

        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {guesses_taken} guess ")

            break


if __name__=="__main__":
    nuber_guessing_game()
