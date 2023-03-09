from lab6 import encode
from decode import decode

def menu():
    print("Menu")
    print("------------- ")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

while True:
    menu()
    option = int(input())
    if option == 1:
        password = input("Please enter your password to encode: ")
        new_password = encode(password)
        print("Your password has been encoded and stored!")
    if option == 2:
        decodedpassword = decode(encodepass)
        print(f"The encoded password is {new_password}, and the original password is {decodepassword}")
    if option == 3:
        break




