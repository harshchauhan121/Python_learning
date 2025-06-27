import art
import random
import game_data
print(art.logo)
score=0
to_continue=True

while to_continue:

    v1=random.choice(game_data.data)
    v2=random.choice(game_data.data)
    if v1==v2:
        v2 = random.choice(game_data.data)

    print(f"Compare A: {v1['name']}, {v1['description']}, {v1['country']}")
    print(art.vs)
    print(f"Against B: {v2['name']}, {v2['description']}, {v2['country']}")

    choice=input("Who has more followers? Type 'A' or 'B':")
    print("\n"*10)
    if v1['follower_count']>v2['follower_count'] and choice == 'A':
        score+=1
        print(art.logo)
        print(f"You're right! Current score {score}")

    elif v1['follower_count']<v2['follower_count'] and choice == 'B':
        print(art.logo)
        score+=1
        print(f"You're right! Current score {score}")

    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        to_continue=False