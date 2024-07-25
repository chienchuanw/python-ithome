# 1. Create an empty tuple

empty_tuple = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters = ("Mary", "Susan")
brothers = ("Frank", "James")

# 3. Join brothers and sisters tuples and assign it to siblings

siblings = sisters + brothers

# 4. How many siblings do you have?

print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = siblings + ("Jane", "Seth")

# 6. Unpack siblings and parents from family_members

*siblings, mother, father = family_members
parents = (mother, father)

# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("apple", "grape", "orange")
vegetables = ("carrot", "onion", "potato")
animal_products = ("cat food", "dog food")

food_stuff_tp = fruits + vegetables + animal_products

# 8. Change the about food_stuff_tp  tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

# 9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.


if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[
        (len(food_stuff_tp) // 2 - 1) : len(food_stuff_tp) // 2 + 1
    ]
    print(middle_items)
else:
    middle_item = food_stuff_tp[len(food_stuff_tp) // 2]
    print(middle_item)

# 10. Slice out the first three items and the last three items from food_staff_lt list

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# 11. Delete the food_staff_tp tuple completely

del food_stuff_tp


# 12. Check if an item exists in tuple:

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

# - Check if 'Estonia' is a nordic country

print("Estonia" in nordic_countries)

# - Check if 'Iceland' is a nordic country

print("Iceland" in nordic_countries)
