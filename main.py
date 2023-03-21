
def encode(password):
    encode = []
    for num in password:
        num = int(num)
        num += 3
        encode += [num]
    return encode

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    opt = int(input("Please enter an option: "))
    if opt == 1:
        password = (input("Please enter your password to encode: "))
        encode = encode(password)
        print("Your password has been encoded and stored!\n")
    elif opt == 2:

        print(f"The encoded password is {encodepass}, and the original password is {ogpass}.\n")
    elif opt == 3:
        break

