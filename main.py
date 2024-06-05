import itertools
import string

# Function to load passwords from a file
def load_passwords(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: File not found.")
        return []

# Brute force password generator
def generate_brute_force(characters, max_length):
    for length in range(1, max_length + 1):
        for candidate in itertools.product(characters, repeat=length):
            yield ''.join(candidate)

# Dictionary-based password check
def check_with_dictionary(password_list, dictionary):
    for password in password_list:
        if password in dictionary:
            yield password

# Pattern matching in passwords
def search_pattern(password_list, search_term):
    for password in password_list:
        if search_term in password:
            yield password

# Main function to execute the chosen attack
def execute_attack():
    # Load passwords from user-provided file
    password_file = input("Enter the password file name: ")
    passwords = load_passwords(password_file)
    print("Passwords loaded:", passwords)

    # Attack options for the user
    print("Select an attack method:")
    print("1. Brute Force Attack")
    print("2. Dictionary Attack")
    print("3. Pattern Matching")

    selection = input("Enter your choice (1/2/3): ")

    if selection == '1':
        charset = string.ascii_letters + string.digits + string.punctuation
        max_length = int(input("Enter the maximum length for brute force attack: "))
        print("Initiating brute force attack...")
        for attempt in generate_brute_force(charset, max_length):
            if attempt in passwords:
                print(f"Password cracked: {attempt}")
                break
        else:
            print("Brute force attack unsuccessful.")
    elif selection == '2':
        dictionary_file = input("Enter the dictionary file name: ")
        dictionary = load_passwords(dictionary_file)
        for cracked_password in check_with_dictionary(passwords, dictionary):
            print(f"Password cracked: {cracked_password}")
            break
    elif selection == '3':
        pattern = input("Enter the pattern to search for: ")
        for matched_password in search_pattern(passwords, pattern):
            print(f"Password matched: {matched_password}")
            break
    else:
        print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    execute_attack()
