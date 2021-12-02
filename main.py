print("Welcome to the tip calculator.\n")

bill_amount = float(input("How much is your bill?\n"))
tip_percent = int(input("What percent do you want to tip: 15, 18, or 20?\n"))
bill_split = int(input("How many people are splitting the bill?\n"))

tip_amount = bill_amount * (tip_percent / 100)
bill_with_tip = bill_amount + tip_amount
split_amount = round((bill_with_tip / bill_split),2)

print(f'Each person should pay {split_amount}')