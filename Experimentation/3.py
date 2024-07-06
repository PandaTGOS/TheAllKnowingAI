import string
import random
import getpass
import time

# Get user's input without echoing it to the console
user_input = getpass.getpass('Please type something and press enter: ')

# Initialize an empty string to store the user's actual input
actual_input = ''

# For each character in the user's input
for character in user_input:
    # Generate a random letter
    random_letter = random.choice(string.ascii_letters)
    # Print the random letter to the console
    print(random_letter, end='', flush=True)
    time.sleep(0.1)  # sleep to mimic typing
    # Add the actual character to the actual_input string
    actual_input += character

print("\n")  # to move to new line after input

# Now the variable actual_input holds the user's actual input
# And the console has displayed random letters instead
print("You typed:", actual_input)