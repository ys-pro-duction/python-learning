p = ""
for i in range(1,101):
    p = ""
    if i % 3 == 0:
        p = "Fizz"
    if i % 5 == 0:
        p +="Buzz"
    if p == "": p = i
    print(p)