#Get alphabet in list
DECRYPTED_CAP = [chr(x) for x in range(65, 91)]
DECRYPTED_NORM = [chr(y) for y in range(97, 123)]
ENCRYPTED_CAP = [chr(x) for x in range(65, 91)]
ENCRYPTED_NORM = [chr(y) for y in range(97, 123)]

def setup(ENCRYPTED_NORM, ENCRYPTED_CAP):
    step = input("How many steps? ")
    step = int(step)

    for i in range(int(step)):
        ENCRYPTED_NORM.insert(i, ENCRYPTED_NORM[(len(ENCRYPTED_NORM))-(step-i)])
        ENCRYPTED_CAP.insert(i, ENCRYPTED_CAP[(len(ENCRYPTED_CAP))-(step-i)])

    x = ENCRYPTED_NORM[:26]
    y = ENCRYPTED_CAP[:26]
    return x, y

def work_the_magic(msg):
    ask = input("Do you want to (1)encode or (2)decode the message? ")
    new_msg = ""
    if ask == "1":
        for i in msg:
            if i not in ENCRYPTED_LIST:
                new_msg += i
            else:
                new_msg += ENCRYPTED_LIST[DECRYPTED_LIST.index(i)]
        return new_msg
    elif ask == "2":
        for i in msg:
            if i not in ENCRYPTED_LIST:
                new_msg += i
            else:
                new_msg += DECRYPTED_LIST[ENCRYPTED_LIST.index(i)]
        return new_msg

ENCRYPTED_NORM, ENCRYPTED_CAP = setup(ENCRYPTED_NORM, ENCRYPTED_CAP)
ENCRYPTED_LIST = ENCRYPTED_NORM + ENCRYPTED_CAP
DECRYPTED_LIST = DECRYPTED_NORM + DECRYPTED_CAP

msg = input("Your text: ")
print("Decoded: " + work_the_magic(msg))