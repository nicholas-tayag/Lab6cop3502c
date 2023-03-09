# Nicholas Tayag

def encode(password):
    new_password = ""
    for i in password:
        num_3 = int(i)+3
        new_password += str(num_3)
    return new_password

