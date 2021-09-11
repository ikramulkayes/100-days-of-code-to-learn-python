print("Welcome to the tip calculator.")
bill = input("What was the total bill: ")
bill = float(bill)
tip = float(input("What percentage tip would you like to give? "))
ppl = float(input("How many people to split the bill? "))
sum1 = (bill/ppl) + (bill*(tip/100))/ppl
sum1 = round(sum1,2)
print("Each person should pay:",sum1)