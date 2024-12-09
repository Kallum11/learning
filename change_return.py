# Program to calculate your change after buying an item.

# Taking inputs and converting to it to a float.
cost = float(input("How much is the item: "))
paid = float(input("How much did you pay? "))

# Calculating the change or owed amounts.
change = paid - cost
owe = cost - paid

# If you paid more than the item you will get change. If you pay less it will tell you what you owe.
if paid >= cost:
    print(f"You paid £{paid} for an item that costs £{cost}. Your change is £{change}.")
else:
    print(f"you still owe £{owe}.")
