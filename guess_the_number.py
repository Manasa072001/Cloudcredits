import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    attempts = 0
    max_attempts = 10  # You can change the maximum attempts as desired

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number within the range of {lower_bound} to {upper_bound}.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
