print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_value= tip /100 *bill
final_bill= bill+ tip_value
individual_share=round(final_bill/people,2)
print(f"Each person should pay: ${individual_share}")

