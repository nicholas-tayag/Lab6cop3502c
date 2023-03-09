from lab6 import encode
from decode import decode

def menu():
    print("Welcome to encoder/decoder")
    print("Type '1' to Encode")
    print("Type '2' to Decode")


while True:
    menu()
    option = int(input())
    if option == 1:
        new_password = encode(password)
        print(new_password)
    if option == 2:
        decode()


