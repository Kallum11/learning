# Program to split bills.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
# Calculate tip add it to the bill and divide the split.
total = round((bill + (bill * (tip / 100))) / split, 2)
print(f"Each person should pay: £{total}")
