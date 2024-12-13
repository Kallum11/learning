guess = int(input("Enter a number: "))

while guess != 0:
    if guess % 2 == 0:
        print(f"{guess} is Even!")
    else:
        print(f"{guess} is Odd!")
    guess = int(input("Enter a number: "))
print("Exiting program. Goodbye!")
