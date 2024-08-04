# ```py
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ```

# ### 初階題

# 1. Explain the difference between map, filter, and reduce.

print(
    "map will take a function and an iterable object as parameters and return a map object."
)
print(
    "filter will take a function which returns a bool and an iterable object as parameters. If item in the iterable object fits the criteria, the item will pass through the filter and stays."
)
print(
    "reduce as a function in functools module will take a function and an iterable object as parameters. It will sum up the current value with accumulation and return a final single value."
)

# 2. Explain the difference between higher order function, closure and decorator


# 3. Define a call function before map, filter or reduce, see examples.


# 4. Use for loop to print each country in the countries list.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]

for country in countries:
    print(country)


# 5. Use for to print each name in the names list.

names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]

for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

# ### 進階題

# 1. Use map to create a new list by changing each country to uppercase in the countries list

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
countries_uppercase = list(map(lambda item: item.upper(), countries))
print(countries_uppercase)

# 2. Use map to create a new list by changing each number to its square in the numbers list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_square = list(map(lambda num: num**2, numbers))
print(numbers_square)


# 3. Use map to change each name to uppercase in the names list

names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
names_uppercase = list(map(lambda name: name.upper(), names))
print(names_uppercase)

# 4. Use filter to filter out countries containing 'land'.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
countries_with_land = list(filter(lambda country: "land" in country, countries))
print(countries_with_land)

# 5. Use filter to filter out countries having exactly six characters.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
countries_with_six_chars = list(filter(lambda country: len(country) == 6, countries))
print(countries_with_six_chars)

# 6. Use filter to filter out countries containing six letters and more in the country list.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
countries_with_six_more_chars = list(
    filter(lambda country: len(country) >= 6, countries)
)
print(countries_with_six_more_chars)

# 7. Use filter to filter out countries starting with an 'E'

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
countries_starts_E = list(filter(lambda country: country[0] == "E", countries))
print(countries_starts_E)

# 8. Chain two or more list iterators (eg. list.map(callback).filter(callback).reduce(callback))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from math import pow
from functools import reduce

nums_power_sum = reduce(lambda x, y: x + y, map(lambda i: pow(i, 2), numbers))
print(nums_power_sum)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.


def get_string_lists(input_list: list) -> list:
    return list(filter(lambda item: isinstance(item, str), input_list))


import unittest


class TestGetStringLists(unittest.TestCase):
    def test_mixed_list(self):
        input_list = ["Hello", 123, "World", 456, "Python"]
        expected_output = ["Hello", "World", "Python"]
        self.assertEqual(get_string_lists(input_list), expected_output)

    def test_all_strings(self):
        input_list = ["a", "b", "c"]
        expected_output = ["a", "b", "c"]
        self.assertEqual(get_string_lists(input_list), expected_output)

    def test_no_strings(self):
        input_list = [1, 2, 3]
        expected_output = []
        self.assertEqual(get_string_lists(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(get_string_lists(input_list), expected_output)

    def test_mixed_types(self):
        input_list = ["a", 1, "b", None, "c", 3.14, "d"]
        expected_output = ["a", "b", "c", "d"]
        self.assertEqual(get_string_lists(input_list), expected_output)


unittest.main()


# 10. Use reduce to sum all the numbers in the numbers list.

import unittest
from typing import Union
from functools import reduce


def sum_numbers(input_list: list) -> Union[int, float]:
    try:
        return reduce(lambda x, y: x + y, input_list)
    except Exception as e:
        return e


class TestSumNumbers(unittest.TestCase):
    def test_int_sum(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = 15
        self.assertEqual(sum_numbers(input_list), expected_output)


unittest.main()


# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# ### 高階題

# 1. Use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    - Sort countries by name, by capital, by population
#    - Sort out the ten most spoken languages by location.
#    - Sort out the ten most populated countries.
