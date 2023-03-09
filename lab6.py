# Nicholas Tayag

def encode(password):
    password = ""
    for i in password:
        num_3 = int(i) + 3
        password = str(num_3) + 3
    return password

