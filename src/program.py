# Author : Harnish Prajapati, Krish Patel
# Date : February 28, 2025
# Purpose : Lab 1
# description : Random password generator

import random
import string


# Function to get user input
def get_user_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to generate a password
def generate_password(length, num_letters, num_digits, num_specials):
    if num_letters + num_digits + num_specials > length:
        raise ValueError("Sum of letters, digits, and special characters exceeds total length.")

    password = []

    # Generate required characters
    password += random.choices(string.ascii_letters, k=num_letters)
    password += random.choices(string.digits, k=num_digits)
    password += random.choices(string.punctuation, k=num_specials)

    # Fill the remaining characters
    remaining_length = length - len(password)
    password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Main function
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs for password length and character distribution
    total_length = get_user_input("Enter the total password length: ", 1, 100)
    num_letters = get_user_input("Enter the number of letters: ", 0, total_length)
    num_digits = get_user_input("Enter the number of digits: ", 0, total_length - num_letters)
    num_specials = get_user_input("Enter the number of special characters: ", 0,
                                  total_length - num_letters - num_digits)

    # Step 2: Generate the password
    password = generate_password(total_length, num_letters, num_digits, num_specials)

    # Step 3: Display the generated password
    print(f"\nGenerated Password: {password}")

    # Step 4: Save password to file
    with open("generated_password.txt", "w") as file:
        file.write(password)
    print("Password saved to generated_password.txt")


# Entry point of the script
if __name__ == "__main__":
    main()
