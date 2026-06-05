import random

print("🎯 Welcome to Guess the Number!")
computer = random.randint(1, 100)

def guessing():
    level=input("easy or hard")
    if level=="easy":
        attempts = 10
    if level=="hard":
        attempts=5
        while attempts > 0:
            try:
                num = int(input(f"\nYou have {attempts} attempts left. Guess a number between 1 and 100: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if num > computer:
                print("Too high!")
                attempts -= 1
            elif num < computer:
                print("Too low!")
                attempts -= 1
            else:
                print("🎉 Correct guess! You win!")
                return

        print(f"\n Game over! The number was {computer}.")

guessing()

