import  random
# a to z array
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 0 to 9 number array
number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# array of special characters
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '<', '>', '|']

al = int(input("Alphabets in password: "))
nu = int(input("Number in password: "))
sc = int(input("Special character in password: "))
password = ""
passwordArr = []
passLength = al+nu+sc
# Easy ########
for i in range(0,al):
    password += alphabet[random.randint(0,len(alphabet)-1)]
    passwordArr.append(alphabet[random.randint(0,len(alphabet)-1)])

for i in range(0,nu):
    password += number_array[random.randint(0,len(number_array)-1)]
    passwordArr.append(number_array[random.randint(0,len(number_array)-1)])
for i in range(0,sc):
    password += special_characters[random.randint(0,len(special_characters)-1)]
    passwordArr.append(special_characters[random.randint(0,len(special_characters)-1)])
print(password)
print(passwordArr)
random.shuffle(passwordArr)
print(passwordArr)

# Hard ###########
hardPassword = ""
pass2DArr = []
if al > 0: pass2DArr.append(alphabet)
if nu > 0: pass2DArr.append(number_array)
if sc > 0: pass2DArr.append(special_characters)
for i in range(0,passLength):
    rArray = random.choice(pass2DArr)
    if rArray == alphabet:
        hardPassword += random.choice(alphabet)
        if len(alphabet) <= 0 : pass2DArr.remove(alphabet)
    if rArray == number_array:
        hardPassword += random.choice(number_array)
        if len(number_array) <= 0 : pass2DArr.remove(alphabet)
    if rArray == special_characters:
        hardPassword += random.choice(special_characters)
        if len(special_characters) <= 0 : pass2DArr.remove(special_characters)
print(hardPassword)
