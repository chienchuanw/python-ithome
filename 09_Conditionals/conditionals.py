# 初階題 Q1

user_age = int(input("Enter your age: "))
(
    print("You are old enough to drive.")
    if user_age >= 18
    else print("You meed {} more years to learn to drive".format(18 - user_age))
)

# 初階題 Q2

your_age = int(input("Enter your age: "))
my_age = 30

if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif your_age == my_age:
    print("We are the same age.")
else:
    diff = my_age - your_age
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")



# 初階題 Q3

a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}.")

# 進階題 Q1

score = int(input("What's the score?"))

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

# 進階題 Q2

month = input("What month is it?").capitalize()

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in autumn:
    print("The season is Autumn.")

elif month in winter:
    print("The season is Winter.")

elif month in spring:
    print("The season is Spring.")

else:
    print("The season is Summer.")

# 進階題 Q3

fruits = ["banana", "orange", "mango", "lemon"]
user_fruit = input("What fruit do you want to add? ").lower()

if user_fruit in fruits:
    print("That fruit already exist in the list")

else:
    fruits.append(user_fruit)
    print(fruits)

# 高階題 Q1

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if person["skills"]:
    print(person["skills"][len(person["skills"]) // 2])



# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if person["skills"] and "Python" in person["skills"]:
    print("This person knows Python.")
else:
    print("This person has no such skill.")


# If a person skills has only JavaScript and React, print('He is a frontend developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if (
    len(person(["skills"])) == 2
    and "JavaScript" in person["skills"]
    and "React" in person["skills"]
):
    print("He is a frontend develop")
elif (
    "Node" in person["skills"]
    and "Python" in person["skills"]
    and "MangoDB" in person["skills"]
):
    print("He is a backend developer")
elif (
    "React" in person["skills"]
    and "Node" in person["skills"]
    and "MangoDB" in person["skills"]
):
    print("He is a fullstack developer")
else:
    print("unknown title")

# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

if person["is_marred"] and person["country"] == "Finland":
    print(f"{person["first_name"]} lives in {person['country']} He is married.")
