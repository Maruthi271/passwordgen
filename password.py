import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password (min 8 characters): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    password_length = get_password_length()
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
