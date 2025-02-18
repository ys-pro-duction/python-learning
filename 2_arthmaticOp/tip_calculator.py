bill = input("Total bill amount: $")
tip = input("Tip you want to give in % (eg. 10): ")
member = input("Split bill in how many member's: ")

print(f"Member's need to pay ${round((int(bill)+(int(bill) * (int(tip)/100)))/int(member),2)}")