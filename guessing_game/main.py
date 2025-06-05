import random

def nuber_guessing_game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 to 100")

    secret_number = random.randint(1, 10)

    guesses_taken = 0

    while True:

        try:
            user_guess_str = input("Take a guess: ")
            user_guess = int(user_guess_str)
            guesses_taken += 1

            if user_guess < secret_number:
                print("Your guess is too low! Try again.")
            
            elif user_guess > secret_number:
                print("Your guess is too high! Try again.")

            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {guesses_taken} guess ")

                break

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue


if __name__=="__main__":
    nuber_guessing_game()
