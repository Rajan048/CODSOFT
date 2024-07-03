import random
import string

def generate_password(length):
    # Define the character set to include lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
