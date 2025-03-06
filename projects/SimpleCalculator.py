def addNum(a, b):
    return a + b


def subNum(a, b):
    return a - b


def multiNum(a, b):
    return a * b


def divNum(a: int, b):
    return a / b


operations = {
    "+": addNum,
    "-": subNum,
    "*": multiNum,
    "/": divNum
}


def calculation(first):
    operation = input("Choose operation [+,-,*,/]: ")
    second = int(input("Enter second number: "))
    result = operations[operation](first,second)
    print(f"{first} {operation} {second} = {result}")
    continueToCalculate = input(f"Continue to calculate with {result} [Y/n]: ").lower()
    if continueToCalculate == "y": calculation(result)


print("This is simple calculator operations [+-*/]")
while True:
    first = int(input("Enter first number: "))
    calculation(first)
