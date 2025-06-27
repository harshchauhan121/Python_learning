# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


def max_bid():
    max = 0
    winner = ""
    for key in bids:
        if bids[key] > max:
            max = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${bids[winner]}")


import art
print(art.logo)
bids={}
flag=True
while flag:
    name=input("What is your name? :")
    bid=int(input("What is your bid? :$"))
    bids[name]=bid
    to_continue=input("Are there any more bidders?\nIf yes type y and if no type n -> ")

    if to_continue=="n" or to_continue=="N":
        max_bid()
        flag=False
    else:
        print("\n"*200)

