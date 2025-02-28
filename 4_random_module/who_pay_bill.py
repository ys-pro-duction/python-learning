import random

friends = ["Bob", "Emanuel", "Alice", "David", "Charlie"]
friends.append("Yogesh")
print(friends)
print(random.choice(friends))
print(friends[random.randint(0,4)])
print(len(friends))
