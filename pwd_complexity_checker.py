import re

def password_complexity_checker(password):

    strength = 0

    length = bool(len(password) >= 13)
    upperCase = bool(re.search("[A-Z]", password))
    lowerCase = bool(re.search("[a-z]", password))
    digits = bool(re.search("[0-9]", password))
    specialChar = bool(re.search("[!@#$%^&*<>?~]", password))

    #atleast 8 characters is mandatory in a password
    if len(password)<8:
        print("Password must be at least 8 characters long")

    # Summing up the conditions to assess the strength
    strength = length + upperCase + lowerCase + digits + specialChar

    if strength == 5:
        print("Strong password!")
    elif strength >= 3:
        print("Good password.")
    else:
        print("Weak password...")

    return

pwd = input("Enter your password: ")
password_complexity_checker(pwd)

