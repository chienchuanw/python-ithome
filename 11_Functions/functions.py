# 初階題
# 1. Declare a function `add_two_numbers`. It takes two parameters and it returns a sum.


def add_two_numbers(a, b):
    return a + b


# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates `area_of_circle`.

import math


def area_of_circle(radius):
    return radius**2 * math.pi


# 3. Write a function called `add_all_nums` which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    nums_sum = 0
    for arg in args:
        if isinstance(arg, int, float):
            nums_sum += arg
        else:
            print(f"{arg} is not a number.")
    return nums_sum


# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, `convert_celsius_to_fahrenheit`.


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# 5. Write a function called `check_season`, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def check_season(month: str):
    match month.capitalize():
        case "December" | "January" | "February":
            return "Winter"
        case "March" | "April" | "May":
            return "Spring"
        case "June" | "July" | "August":
            return "Summer"
        case "September" | "October" | "November":
            return "Autumn"
        case _:
            return "Invalid input"


# 6. Write a function called `calculate_slope` which return the slope of a linear equation


def calculate_slope(point_a: tuple, point_b: tuple):
    x1, y1 = point_a
    x2, y2 = point_b

    if x1 == x2:
        return "Slope is undefined"
    slope = (y1 - y2) / (x1 - x2)

    return slope


# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, `solve_quadratic_eqn`.

import math


def solve_quadratic_equ(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2


# 8. Declare a function named `print_list`. It takes a list as a parameter and it prints out each element of the list.


def print_list(input_list: list):
    for item in input_list:
        print(item)


# 9. Declare a function named `reverse_list`. It takes a list as a parameter and it returns the reverse of the list (use loops).

#     ```py
#     print(reverse_list([1, 2, 3, 4, 5]))
#     # [5, 4, 3, 2, 1]
#     print(reverse_list1(["A", "B", "C"]))
#     # ["C", "B", "A"]
#     ```


def reverse_list(input_list: list) -> list:
    output_list = list()

    for item in input_list:
        output_list.insert(0, item)

    return output_list


# 10. Declare a function named `capitalize_list_items`. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(input_list: list) -> list:

    return [item.capitalize() for item in input_list]


# 11. Declare a function named `add_item`. It takes a list and an item parameters. It returns a list with the item added at the end.

#     ```py
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#     numbers = [2, 3, 7, 9]
#     print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
#     ```


def add_item(input_list: list, input_item) -> list:
    input_list.append(input_item)
    return input_list


# 12. Declare a function named `remove_item`. It takes a list and an item parameters. It returns a list with the item removed from it.

#     ```py
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#     numbers = [2, 3, 7, 9]
#     print(remove_item(numbers, 3))  # [2, 7, 9]
#     ```


def remove_item(input_list: list, input_item):
    return [item for item in input_list if item != input_item]


# 13. Declare a function named `sum_of_numbers`. It takes a number parameter and it adds all the numbers in that range.

#     ```py
#     print(sum_of_numbers(5))  # 15
#     print(sum_all_numbers(10)) # 55
#     print(sum_all_numbers(100)) # 5050
#     ```


def sum_of_numbers(num):
    return sum(range(num + 1))


# 14. Declare a function named `sum_of_odds`. It takes a number parameter and it adds all the odd numbers in that range.


def sum_of_odds(num: int):
    return sum([i for i in range(num + 1) if i % 2 != 0])


# 15. Declare a function named `sum_of_even`. It takes a number parameter and it adds all the even numbers in that range.


def sum_of_even(num: int):
    return sum([i for i in range(num + 1) if i % 2 == 0])


# 進階題
# 1. Declare a function named `evens_and_odds` . It takes a positive integer as parameter and it counts number of evens and odds in the number.

#     ```py
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
#     ```


def evens_and_odds(num: int) -> int:
    if num <= 0:
        raise ValueError("Input number must be a positive integer.")
    evens = len([i for i in range(num + 1) if i % 2 == 0])
    odds = num + 1 - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."


# 2. Call your function `factorial`, it takes a whole number as a parameter and it return a factorial of the number


def factorial(num: int) -> int:
    if num == 0:
        return 1
    return 4 * factorial(num - 1)


# 3. Call your function `is_empty`, it takes a parameter and it checks if it is empty or not


def is_empty(data):
    return not bool(data)


# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


def calculate_mean(input_list: list):
    return sum(input_list) / len(input_list)


def calculate_median(input_list: list):
    sorted_list = sorted(input_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]


def calculate_mode(input_list: list):
    from collections import Counter

    # Use Counter to calculate how many times each number shows up
    num_counter = Counter(input_list)

    # Get the highest count
    max_count = max(num_counter.values())

    # Extract all elements with the highest count
    mode = [num for num, count in num_counter.items() if count == max_count]

    return mode


def calculate_range(input_list: list):
    input_list.sort()

    return input_list[-1] - input_list[0]


def calculate_variance(input_list: list):
    avg = sum(input_list) / len(input_list)

    avg_square_diff = [(i - avg) ** 2 for i in input_list]

    return sum(avg_square_diff) / len(input_list)


def calculate_std(input_list: list):
    import math

    avg = sum(input_list) / len(input_list)

    avg_square_diff = [(i - avg) ** 2 for i in input_list]

    variance = sum(avg_square_diff) / len(input_list)

    return math.sqrt(variance)


# 高階題
# 1. Write a function called `is_prime`, which checks if a number is prime.


def is_prime(num: int) -> bool:
    import math

    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# 2. Write a functions which checks if all items are unique in the list.


def is_unique_item(input_list: list) -> bool:
    from collections import Counter

    item_counter = Counter(input_list)

    for num in item_counter.values():
        if num != 1:
            return False
    return True


## better solution


def is_unique_item(input_list: list) -> bool:
    return len(input_list) == len(set(input_list))


# 3. Write a function which checks if all the items of the list are of the same data type.


def is_same_data_type(input_list: list) -> bool:
    # Consider empty list as same data type
    if not input_list:
        return True

    first_type = type(input_list[0])

    return all(isinstance(item, first_type) for item in input_list)


# 4. Write a function which check if provided variable is a valid python variable


def is_valid_variable(var) -> bool:
    return var.isidentifier() if isinstance(var, str) else False


# 5. Go to the data folder and access the `countries_data.py` file.

#    - Create a function called the `most_spoken_languages` in the world. It should return 10 or 20 most spoken languages in the world in descending order

from countries_data import countries_data


def most_spoken_languages(data: list, top_n: int = 10) -> list:
    from collections import Counter

    language_counter = Counter()

    for language in data:
        language_counter.update(language["languages"])

    result = language_counter.most_common(top_n)

    return result


print(most_spoken_languages(countries_data))


#    - Create a function called the `most_populated_countries`. It should return 10 or 20 most populated countries in descending order.

from countries_data import countries_data


def most_populated_countries(data: list, top_n: int = 10) -> list:
    populated_countries = {}

    for country in data:
        populated_countries[country["name"]] = country["population"]

    result = sorted(
        populated_countries.items(), key=lambda item: item[1], reverse=True
    )[:top_n]

    return result


# better solution


def most_populated_countries(data: list, top_n=10) -> list:
    return sorted(data, key=lambda x: x["population"], reverse=True)[:top_n]


print(most_populated_countries(countries_data))
