print("Welcome to roller coaster ride")
height = int(input("Enter your height in cm: "))
if height > 120:
    print("You can rid.")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Need to pay $17")
    else:
        print("Need to pay $7")
else:
    print("You can not ride.")