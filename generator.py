import random
import string

def generate_password():
    print("=== Python Password Generator ===")
    
    # Get password length input
    try:
        length = int(input("Enter password length (minimum 6): "))
        if length < 6:
            print("Length too short! Setting minimum to 6.")
            length = 6
    except ValueError:
        print("Invalid input! Defaulting length to 8 characters.")
        length = 8

    # Define character choices
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = lower + upper + digits + symbols

    # Generate random password
    password_list = [random.choice(all_characters) for _ in range(length)]
    password = "".join(password_list)

    print(f"\nYour Secure Password: {password}\n")

if __name__ == "__main__":
    generate_password()