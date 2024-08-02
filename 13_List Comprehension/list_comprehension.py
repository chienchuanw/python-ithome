# 1. Filter only negative and zero in the list using list comprehension

#    ```py
#    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
#    ```

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers_with_zero = [num for num in numbers if num <= 0]
print(negative_numbers_with_zero)

# 2. Flatten the following list of lists of lists to a one dimensional list :

#    ```py
#    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    ```

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [
    i for second_list in list_of_lists for items in second_list for i in items
]
print(flatten_list)

# 3. Using list comprehension create the following list of tuples:

#    ```py
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#    ```

list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# 4. Flatten the following list to a new list:

#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#    ```

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
output = [
    [item[0].upper(), item[0].upper()[:3], item[1].upper()]
    for country in countries
    for item in country
]
print(output)

# 5. Change the following list to a list of dictionaries:

#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
#    ```

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
output = [
    {"country": item[0].upper(), "city": item[1].upper()}
    for country in countries
    for item in country
]
print(output)

# 6. Change the following list of lists to a list of concatenated strings:

#    ```py
#    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#    ```

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
output = [f"{item[0]} {item[1]}" for name in names for item in name]
print(output)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2: (y1 - y2) / (x1 - x2)

# solution for y-intercept
intercept = lambda x1, y1, x2, y2: y1 - ((y1 - y2) / (x1 - x2)) * x1
