# Day 2: 30 Days of Python programming

first_name, last_name = "Frank", "Wang"
full_name = f"{first_name} {last_name}"

country, city = "Taiwan", "Taipei"

age = 30

year = 2024

is_married = False
is_true = True
is_light_on = False

var_a, var_b, var_c = "a", "b", "c"

print("=" * 20)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(var_a))
print(type(var_b))
print(type(var_c))

print("=" * 20)

print(len(first_name))

print("=" * 20)

print(len(first_name) > len(last_name))

print("=" * 20)

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

print("=" * 20)

import math

radius = 30
area_of_circle = (radius**2) * math.pi
circum_of_circle = (radius * 2) * math.pi

user_radius = float(input("Input radius? "))
print((user_radius**2) * math.pi)

print("=" * 20)

user_first_name = input("What is your first name? ")
user_last_name = input("What is your last name? ")
user_country = input("Where are you come from? ")
user_age = input("How old are you? ")

print("=" * 20)

help("keywords")
