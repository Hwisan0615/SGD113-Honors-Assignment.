import random

def up_and_down_game():
    while True:
        number_to_guess = random.randint(1, 25)
        attempts = 0
        max_attempts = 5
        print("Welcome to the Up and Down Game!")
        print("I have selected a number between 1 and 25. Try to guess it!")
        print(f"You have {max_attempts} attempts.")

        while attempts < max_attempts:
            guess = input("Enter your guess: ")
            attempts += 1

            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a valid number.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        else:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    up_and_down_game()