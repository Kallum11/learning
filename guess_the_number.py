import random
print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

selection = random.randint(0, 100)
print(selection)
guess = int(input("Enter your guess: "))

attempts = 0


while guess < selection:
    print("Too low! Try again.")
    attempts += 1
    guess = int(input("Enter your guess: "))
    while guess > selection:
        print("Too high! Try again.")
        attempts += 1
        guess = int(input("Enter your guess: "))
        if guess == selection:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")