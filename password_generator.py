import string
import random
import sys

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python password_generator.py <length>")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
        password = generate_password(length)
        print(f"[+] Generated Password: {password}")
    except ValueError as e:
        print(f"[-] Error: {e}")
