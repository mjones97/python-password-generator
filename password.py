import random
import string

# Function to generate a password based on user inputs
def generate_password(min_length, numbers=True, special_characters=True):
    # Define sets of characters to be used in the password
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Initialize the character set with letters
    characters = letters
    # Add digits to the character set if numbers are required
    if numbers:
        characters += digits
    # Add special characters to the character set if special characters are required
    if special_characters:
        characters += special

    # Initialize variables
    pwd = ""
    meets_criteria = False
    has_number = False 
    has_special = False

    # Generate the password
    while not meets_criteria or len(pwd) < min_length:
        # Choose a random character from the character set
        new_char = random.choice(characters)
        # Add the chosen character to the password
        pwd += new_char

        # Update flags if the chosen character is a number or special character
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Check if the password meets the criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

# Function to get user input with validation
def get_user_input(prompt, valid_options):
    while True:
        # Prompt the user for input
        user_input = input(prompt).lower()
        # Check if the input is one of the valid options
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

# Main program
while True:
    try:
        # Get the minimum length of the password from the user
        min_length = int(input("Enter minimum length of password: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Get user input for including numbers in the password
has_number = get_user_input("Do you want to include numbers (y/n)? ", ["y", "n"]) == "y"

# Get user input for including special characters in the password
has_special = get_user_input("Do you want to include special characters? (y/n)? ", ["y", "n"]) == "y"

# Generate the password based on user inputs
pwd = generate_password(min_length, has_number, has_special)

# Print the generated password
print("Generated Password:", pwd)
