from lab6 import encode

def menu():
    print("Welcome to encoder/decoder")
    print("Type '1' to Encode")
    print("Type '2' to Decode")


while True:
    menu()
    option = int(input())
    if option == 1:
        password = (input("Encode Password: "))
        encode(password)
        print(password)
    if option == 2:
        decode = int(input("Decode Password: "))