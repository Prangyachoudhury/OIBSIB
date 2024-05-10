import string
import random

def get_password(length, use_numbers=True, use_special_chars=True):
    # Define the character set
    char_set = string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))

    return password

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def get_yes_or_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == 'yes' or response == 'no':
            return response
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    # Get user preferences
    length = get_valid_length()
    use_numbers = get_yes_or_no("Should the password include numbers? (yes/no): ") == 'yes'
    use_special_chars = get_yes_or_no("Should the password include special characters? (yes/no): ") == 'yes'

    # Generate and print the password
    password = get_password(length, use_numbers, use_special_chars)
    print(f'Your generated password is: {password}')

if __name__ == "__main__":
    main()
