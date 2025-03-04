def calculate_love_score(name1, name2):
    trueOccur = 0
    loveOccur = 0
    combined = (name1 + name2).lower()
    for i in combined:
        if i == "t":
            trueOccur += 1
        elif i == "r":
            trueOccur += 1
        elif i == "u":
            trueOccur += 1
        elif i == "e":
            trueOccur += 1
            loveOccur += 1

        if i == "l":
            loveOccur += 1
        elif i == "o":
            loveOccur += 1
        elif i == "v":
            loveOccur += 1
    print(f"{trueOccur}{loveOccur}")

calculate_love_score("Kanye West", "Kim Kardashian")

