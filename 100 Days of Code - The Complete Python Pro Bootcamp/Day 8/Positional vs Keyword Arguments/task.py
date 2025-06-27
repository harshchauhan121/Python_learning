# Functions with input
#
# def greet_with_name(name,location):
#     print(f"Hello {name}")
#     print(f"Hows the weather at {location}?")
#
#
# greet_with_name(location="dehradun",name="Jack Bauer")
def calculate_love_score(name1,name2):
    sum1=0
    sum2=0
    combined_name=(name1+name2).lower()
    for i in "TRUE":
        sum1+=combined_name.count(i.lower())
    print(sum1)
calculate_love_score("Kanye West", "Kim Kardashian")