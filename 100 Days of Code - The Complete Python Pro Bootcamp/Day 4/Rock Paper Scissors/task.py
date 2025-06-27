rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice=int(input("What do you choose? \nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors "))
import random
comp_choice=random.randint(0,2)
if user_choice==0 and comp_choice==1:
    print(rock)
    print("Computer chose:\n"+paper)
    print("You lose")
if user_choice==0 and comp_choice==2:
    print(rock)
    print("Computer chose:\n"+scissors)
    print("You win")
if user_choice==0 and comp_choice==0:
    print(rock)
    print("Computer chose:\n"+rock)
    print("Draw")
if user_choice==1 and comp_choice==1:
    print(paper)
    print("Computer chose:\n"+paper)
    print("Draw")
if user_choice==1 and comp_choice==2:
    print(paper)
    print("Computer chose:\n"+scissors)
    print("You loose")
if user_choice==1 and comp_choice==0:
    print(paper)
    print("Computer chose:\n"+rock)
    print("YOu win")
if user_choice==2 and comp_choice==1:
    print(scissors)
    print("Computer chose:\n"+paper)
    print("You Win")
if user_choice==2 and comp_choice==2:
    print(scissors)
    print("Computer chose:\n"+scissors)
    print("Draw")
if user_choice==2 and comp_choice==0:
    print(scissors)
    print("Computer chose:\n"+rock)
    print("You loose")
else:
    print("Invalid input!try again")
