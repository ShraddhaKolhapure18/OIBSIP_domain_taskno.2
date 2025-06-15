import secrets
import string

def get_user_input():
    try:
        length = int(input("Enter length of password you want to create: "))
        if length <= 0:
            print("Please enter postive intger ")
            return None

        use_letters = input("Include letters?  Enter yes/no: ").strip().lower() == 'yes'
        use_numbers = input("Include numbers?  Enter yes/no: ").strip().lower() == 'yes'
        use_symbols = input("Include symbols?  Enter yes/no: ").strip().lower() == 'yes'

        if not (use_letters or use_numbers or use_symbols):
            print("You must select at least one character type.")
            return None

        return length, use_letters, use_numbers, use_symbols
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return None

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    user_input = get_user_input()
    if user_input:
        length, use_letters, use_numbers, use_symbols = user_input
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
