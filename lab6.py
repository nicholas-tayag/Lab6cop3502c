# Nicholas Tayag

def encode(password):
    password = ""
    for digit in password:
        digit = str((int(digit) + 3))
        password += digit
    return password

