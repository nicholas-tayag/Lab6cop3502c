#Dion Ming

def decode(encodepass):
    decodepass = ''
    for i in encodepass:
        decoded = int(i)-3
        decodepass += str(decoded)
    #print(decodepass)
    return decodepass


