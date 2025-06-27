import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while choice=='y':
    print("\n"*100)
    print(art.logo)
    your_cards=[]
    #test
    comp_cards=[]
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    your_sum=sum(your_cards)
    comp_cards.append(random.choice(cards))
    comp_sum=sum(comp_cards)
    print(f"Your cards: {your_cards}, current score: {your_sum}")
    print(f"Computer's first card: {comp_cards[0]}")
    to_continue=input("Type 'y' to get another card, type 'n' to pass: ")

    while to_continue=='y':
        your_cards.append(random.choice(cards))
        your_sum = sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {your_sum}")
        print(f"Computer's first card: {comp_cards[0]}")
        if your_sum>21:
            #print(f"Your final hand: {your_cards}, final score: {your_sum}")
            break
        to_continue = input("Type 'y' to get another card, type 'n' to pass: y")

    print(f"Your final hand: {your_cards}, final score: {your_sum}")

    while True:
        comp_cards.append(random.choice(cards))
        comp_sum=sum(comp_cards)
        if comp_sum>=17 and comp_sum>your_sum:
            #choice=random.randint(0,1)
            break
        if comp_sum>21:
            break

    print(f"Computer's final hand: {comp_cards}, final score: {comp_sum}")

    if your_sum>21:
        print("You went over. You loose 😁")
    elif comp_sum > 21:
        print("Opponent went over. You win 😁")
    elif comp_sum==your_sum:
        print("Draw")

    elif comp_sum>your_sum:
        print("You lose 😤")
    elif comp_sum<your_sum:
        print("")
    choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")