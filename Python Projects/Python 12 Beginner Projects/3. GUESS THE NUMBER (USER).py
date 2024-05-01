# Guess the number (User)

# Import the random module
import random


# Define a function called computer_guess that takes a parameter x
def computer_guess(x):

    # Initialize the lower bound of the guessing range
    low = 1

    # Initialize the upper bound of the guessing range
    high = x

    # Initialize a variable for user feedback
    feedback = ""

    # Start a loop that continues until the feedback is "c" (correct)
    while feedback != "c":
        # Check if the lower bound is not equal to the upper bound
        if low != high:
            # If not equal, generate a random guess within the current range
            guess = random.randint(low, high)
        else:
            # If equal, set the guess to either low or high (they are the same)
            guess = low   # could also be high because low = high

        # Get user feedback (whether the guess is too high, too low, or correct)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        # Adjust the guessing range based on user feedback
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    # Print a message when the correct number is guessed
    print(f"Yay! The Computer guessed your number, {guess}, correctly:")


# Call the function with an example range (e.g., 1 to 10)
computer_guess(10)
