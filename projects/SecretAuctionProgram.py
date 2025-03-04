print("Welcome to secret auction program!")
auction = {}
moreBids = True
while moreBids:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    haveMoreBids = input("Are there any other bidders? [Y/n]: ").lower()
    if haveMoreBids == "y":
        print("\n"*20)
    else: moreBids = False

maxBid = max(auction)
# for key in auction:
#     if maxBid is None: maxBid = key
#     elif auction[maxBid] < auction[key]: maxBid = key
print(f"Auction winner with max bid is {maxBid} with ${auction[maxBid]} bid.")