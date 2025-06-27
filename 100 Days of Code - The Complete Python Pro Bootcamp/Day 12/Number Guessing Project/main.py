import art
import random
print(art.logo)
difficulty_level=input('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard':''')

number=random.randint(1,100)
life=0
if difficulty_level=="easy":
    life=10
    print("You have 10 attempts remaining to guess the number.")
elif difficulty_level=="hard":
    life=5
    print("You have 5 attempts remaining to guess the number.")



while life>0:
    guess=int(input("Guess a number "))
    if guess<number:
        print("Too low.")

    elif guess>number:
        print("Too high.")

    else:
        print(f"You got it! The answer was {number}")
        break

    life -= 1
    print(f"You have {life} attempts remaining to guess the number.")
    if life != 0:
        print("Guess again.")

if life==0:
    print("You've run out of guesses, you lose.")