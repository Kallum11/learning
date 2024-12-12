print("Very Simple Calculator\n")

menu = ["Addition", "Subtraction", "Multiplication", "Division", "Exit"]

for number, letter in enumerate(menu):
    print(number, letter)

operation = int(input("\nChoose an operation (0/1/2/3/4): "))

if operation == 0:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print(result)
elif operation == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 - num2
    print(result)
elif operation == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    print(result)
elif operation == 3:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Do no divide by zero!")
elif operation == 4:
    print("Exiting program. Goodbye!")