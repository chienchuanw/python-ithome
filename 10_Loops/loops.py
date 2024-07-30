# 1. Iterate 0 to 10 using for loop, do the same using while loop.

# Using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1


# 2. Iterate 10 to 0 using for loop, do the same using while loop.

# Using for loop
for i in reversed(list(range(11))):
    print(i)

# Using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1


# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```

for i in range(1, 8):
    print("#" * i)


# 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

for _ in range(8):
    for _ in range(8):
        print("#", end=" ")
    print()

# 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```

for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

for i in ["Python", "Numpy", "Pandas", "Django", "Flask"]:
    print(i)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(101):
    if i % 2 == 0:
        print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(101):
    if i % 2 != 0:
        print(i)

# 進階 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.

#    ```sh
#    The sum of all numbers is 5050.
#    ```
sum_all = 0
for i in range(101):
    sum_all += i
print(f"The sum of all numbers is {sum_all}")

# 進階 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#     ```sh
#     The sum of all evens is 2550. And the sum of all odds is 2500.
#     ```

even_list = []
odd_list = []

for i in range(101):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(
    f"The sum of all evens is {sum(even_list)}. And the sum of all odds is {sum(odd_list)}."
)

# 高階 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word 'land'.

from countries import countries

word = "land"
for country in countries:
    if word in country:
        print(country)

# 高階 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ["banana", "orange", "mango", "lemon"]
reverse_fruits = []

for fruit in fruits:
    reverse_fruits.insert(0, fruit)

print(reverse_fruits)

# 高階 3. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.

#    1. What are the total number of languages in the data

from countries_data import countries_data

languages = []

for country in countries_data:
    for language in country["languages"]:
        if language not in languages:
            languages.append(language)

print(len(languages))

#    2. Find the ten most spoken languages from the data

from collections import Counter

language_counter = Counter()

for country in countries_data:
    language_counter.update(country["languages"])

most_common_languages = language_counter.most_common(10)
print(most_common_languages)

#    3. Find the 10 most populated countries in the world

populated_countries = {}

for country in countries_data:
    populated_countries[country["name"]] = country["population"]

most_populated_countries = sorted(
    populated_countries.items(), key=lambda item: item[1], reverse=True
)[:10]
print(most_populated_countries)
