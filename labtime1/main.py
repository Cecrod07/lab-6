
def encode(password):
    encode = []
    for num in password:
        num = int(num)
        num += 3
        if num >= 10:
            print("x")
            x = 1
            for val in str(num):
                if x == 1:
                    x = 2
                else:
                    num = int(val)
                    x = 2
        encode += [num]
    return encode

def decode (encoded):
    decode = ''
    for num in encoded:
        num = int(num)
        if num == 2:
            num = 9
        elif num == 1:
            num = 8
        elif num == 0:
            num = 7
        else:
            num -= 3
        decode += str(num)
    return decode

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    opt = int(input("Please enter an option: "))
    if opt == 1:
        password = (input("Please enter your password to encode: "))
        encode = encode(password)
        print("Your password has been encoded and stored!\n")
    elif opt == 2:
        ogpass = decode(encode)
        encoded = ''
        for num in encode:
            encoded += str(num)
        print(f"The encoded password is {encoded}, and the original password is {ogpass}.\n")
    elif opt == 3:
        break

