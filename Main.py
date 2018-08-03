alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(inMsg, offset):
    mySecret = ""
    for z in inMsg:
        if z in alphabetList:
            mySecret += alphabetList[(alphabetList.index(z) + offset) % 26]
        else:
            mySecret += z

    return mySecret

def decode(cipher, offset):

    decodedMsg = ""

    for z in cipher:
        if z in  alphabetList:
            decodedMsg += alphabetList[(alphabetList.index(z) - offset) % 26]
        else:
            decodedMsg += z

    return decodedMsg


if __name__ == '__main__':
    msg = "this-is-a-secret"
    print("original message: " + msg)
    cipher = encode(msg, 145)
    print("encoded message: " + cipher)
    decoded = decode(cipher, 145)
    print("decoded message: " + decoded)