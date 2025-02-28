arr = [52,69,12,2,36,77,10,2,0,8]
print("max = "+ str(max(arr)))
print("sum = "+ str(sum(arr)))

myMax = 0
mySum = 0
for num in arr:
    if myMax < num: myMax = num
    mySum += num
print("myMax = "+ str(myMax))
print("mySum = "+ str(mySum))

s = 0
for i in range(1,10,2):
    s += i
print(s)