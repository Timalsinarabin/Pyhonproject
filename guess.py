import random 
guess=int(input("Enter your guess(0-100): "))
number =random.randint(0,100)

while guess != number:
    print("Guess Higher..." if guess<number else "Guess Lower...")
    guess=int(input("Enter your guess(0-100): "))

print("Correct! You guessed the number.")