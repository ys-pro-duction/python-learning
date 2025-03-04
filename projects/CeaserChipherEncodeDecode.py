alphabetArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]


def encode(string, shifts):
    out = ""
    for i in string.lower():
        if not i.isalpha():
            out += i
            continue
        index = alphabetArr.index(i)
        out += alphabetArr[(index + shifts) % 26]
    return out


def decode(string, shifts):
    out = ""
    for i in string.lower():
        if not i.isalpha():
            out += i
            continue
        index = alphabetArr.index(i)
        out += alphabetArr[(index - shifts) % 26]
    return out


while True:
    text = input("Enter text: ")
    shift = int(input("Enter shift(int): "))
    encodec = encode(text, shift)
    print(encodec)
    print(decode(encodec, shift))
    continueToMore = input("Want to convert more [Y/n]: ").lower()
    if continueToMore != "y": break
