import random

head = 0
tail = 0
count = 1100
while count > 0:
    count-=1
    if random.randint(0,1) == 0:
        head+=1
    else:
        tail+=1
print(f"head {head},  tail {tail}")