import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by zero"

opoerations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide }

def calculator():
    print(art.logo)
    a=float(input("Enter the first number : "))
    choice= True
    while choice:
        key = input("+\n-\n*\n/\nPick an operation : ")
        b = float(input("Enter the second number: "))
        ans=opoerations[key](a,b)
        print(f"{a} {key} {b} = {ans}")

        choice=input(f"type 'y' to continue calculating with {ans}, or type 'n' to start new calculations")
        if choice=='y':
            a=ans
        else:
            choice=False
            print("\n"*20)
            calculator()
calculator()