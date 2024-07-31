# Day 11 - Function 函式

## Functions

What is a function? Before we start making functions, let us learn what a function is and why we need them?

### Defining a Function

A function is **a reusable block of code or programming statements designed to perform a certain task**. To **define** or **declare** a function, Python provides the `def` keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is **called** or **invoked**.

### Declaring and Calling a Function

When we make a function, we call it **declaring a function**. When we start using the it, we call it **calling** or **invoking** a function. Function can be declared **with or without parameters**.

```py
# Function syntax

# Declaring a function
def function_name():
    codes
    codes

# Calling a function
function_name()
```

### Function without Parameters

Function can be declared without parameters.

```py
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name() # calling a function

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers() # calling a function
```

### Function Returning a Value - Part 1

Function can also return values, if a function does not have a `return` statement, the value of the function is `None`. Let us rewrite the above functions using `return`. From now on, we get a value from a function when we call the function and print it.

```py
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())
```

### Function with Parameters

In a function we can pass different **data types** (number, string, boolean, list, tuple, dictionary or set) as a parameter.

- Single Parameter: If our function takes a parameter we should call our function **with an argument**.

    ```py
    # Syntax

    # Declaring a function
    def function_name(parameter):
        codes
        codes

    # Calling function
    function_name(argument)
    ```

    ```py
    # Examples

    def greetings(name):
        message = name + ', welcome to Python for Everyone!'
        return message

    print(greetings('Asabeneh'))

    def add_ten(num):
        ten = 10
        return num + ten

    print(add_ten(90))

    def square_number(x):
        return x * x

    print(square_number(2))

    def area_of_circle(r):
        PI = 3.14
        area = PI * r ** 2
        return area

    print(area_of_circle(10))

    def sum_of_numbers(n):
        total = 0
        for i in range(n+1):
            total+=i
        print(total)

    print(sum_of_numbers(10)) # 55
    print(sum_of_numbers(100)) # 5050
    ```

- Two or more Parameter: A function may also have two or more parameters. If our function takes multiple parameters, we should call it with **arguments**.

    ```py
    # Syntax

    # Declaring a function
    def function_name(para1, para2):
        codes
        codes

    # Calling function
    function_name(arg1, arg2)
    ```

    ```py
    # Examples

    def generate_full_name(first_name, last_name):
        space = ' '
        full_name = first_name + space + last_name
        return full_name

    print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

    def sum_two_numbers(num_one, num_two):
        sum = num_one + num_two
        return sum

    print('Sum of two numbers: ', sum_two_numbers(1, 9))

    def calculate_age(current_year, birth_year):
        age = current_year - birth_year
        return age

    print('Age: ', calculate_age(2021, 1819))

    def weight_of_object (mass, gravity):
        weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
        return weight

    print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
    ```

### Passing Keyword Arguments

Previously, we passed the arguments in the order of parameters. Therefore we can call these arguments as **Positional Arguments**. What if we want to assign a value to a specific parameter regardless of the order? We can use **Keyword Arguments** to achieve it.

```py
# Syntax

# Declaring a function
def function_name(para1, para2):
    codes
    codes

# Calling function
function_name(para1='John', para2='Doe') # the order of arguments does not matter here
```

```py
# Examples

def get_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname

    return full_name

print(get_fullname(firstname='Asabeneh', lastname='Yetayeh'))

def add_two_numbers(num1, num2):
    total = num1 + num2

    return total

print(add_two_numbers(num2=3, num1=2)) # Order does not matter
```

### Function Returning a Value - Part 2

If we do not return a value with a function, then our function is returning `None` by default. To return a value with a function we use the keyword `return` followed by the variable we are returning. We can return **any kind of data types from a function**. Notice that a function will execute **only one `return` statement** at a time. When a `return` statement is being executed, the function ends as well.

- Return a String

    ```py
    def print_name(firstname):
        return firstname

    print_name('Asabeneh') # Asabeneh

    def print_full_name(firstname, lastname):
        space = ' '
        full_name = firstname  + space + lastname
        return full_name

    print_full_name(firstname='Asabeneh', lastname='Yetayeh')
    ```

- Return a Number

    ```py
    def add_two_numbers(num1, num2):
        total = num1 + num2
        return total

    print(add_two_numbers(2, 3))

    def calculate_age (current_year, birth_year):
        age = current_year - birth_year
        return age

    print('Age: ', calculate_age(2019, 1819))
    ```

- Return a Boolean

    ```py
    def is_even (n):
        if n % 2 == 0:
            print('even')
            return True # if return statement is being executed here, it stops further execution of the function, similar to break 
        return False

    print(is_even(10)) # True
    print(is_even(7)) # False
    ```

- Return a List

    ```py
    def find_even_numbers(n):
        evens = []
        for i in range(n + 1):
            if i % 2 == 0:
                evens.append(i)
        return evens
        
    print(find_even_numbers(10))
    ```

### Function with Default Parameters

We can also give parameters a default. So when invoke a function without passing an argument, the function will use the default value instead.

```py
# Syntax

# Declaring a function with a with a default value
def function_name(param=value):
    codes
    codes

# Calling function
function_name() # This will pass the default as an argument when invoking the function
function_name(arg)
```

```py
# Examples

def greetings(name='Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings())
print(greetings('Asabeneh'))

def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age(birth_year,current_year=2021):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(1821))

def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight

print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

### Arbitrary Number of Arguments

If we do not know the number of arguments we pass to our function, we can create a function which can take **arbitrary number of arguments** by adding `*` before the parameter name.

```py
# Syntax

# Declaring a function
def function_name(*args):
    codes
    codes

# Calling function
function_name(param1, param2, param3,..)
```

```py
# Example

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total

print(sum_all_nums(2, 3, 5)) # 10
```

### Combining Named Parameters with *args in Python Functions

```py
def generate_groups(team, *args):
    print(f"team={team}")
    for i in args:
        print(i)

generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

# team=Team-1
# Asabeneh
# Brook
# David
# Eyob
```

### Passing a Function as a Parameter in Another Function

In Python, functions are **first-class objects**, meaning they can **be passed around as arguments to other functions, assigned to variables, and returned from other functions**. This capability allows you to pass a function as a parameter to another function, enabling higher-order functions and more flexible code.

```py
def greeting(name):
    return f"Hello, {name}!"

def process_name(func, name):
    result = func(name)
    return result

# Pass the greeting function as a parameter to the process_name function
output = process_name(greeting, "Alice")
print(output)  # Output: Hello, Alice!
```

## 練習題

### 初階題

1. Declare a function `add_two_numbers`. It takes two parameters and it returns a sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates `area_of_circle`.
3. Write a function called `add_all_nums` which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, `convert_celsius_to-fahrenheit`.
5. Write a function called `check-season`, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
6. Write a function called `calculate_slope` which return the slope of a linear equation
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, `solve_quadratic_eqn`.
8. Declare a function named `print_list`. It takes a list as a parameter and it prints out each element of the list.
9. Declare a function named `reverse_list`. It takes an array as a parameter and it returns the reverse of the array (use loops).

    ```py
    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list1(["A", "B", "C"]))
    # ["C", "B", "A"]
    ```

10. Declare a function named `capitalize_list_items`. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named `add_item`. It takes a list and an item parameters. It returns a list with the item added at the end.

    ```py
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
    numbers = [2, 3, 7, 9]
    print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
    ```

12. Declare a function named `remove_item`. It takes a list and an item parameters. It returns a list with the item removed from it.

    ```py
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9]
    print(remove_item(numbers, 3))  # [2, 7, 9]
    ```

13. Declare a function named `sum_of_numbers`. It takes a number parameter and it adds all the numbers in that range.

    ```py
    print(sum_of_numbers(5))  # 15
    print(sum_all_numbers(10)) # 55
    print(sum_all_numbers(100)) # 5050
    ```

14. Declare a function named `sum_of_odds`. It takes a number parameter and it adds all the odd numbers in that range.
15. Declare a function named `sum_of_even`. It takes a number parameter and it adds all the even numbers in that - range.

### 進階題

1. Declare a function named `evens_and_odds` . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    ```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
    ```

2. Call your function `factorial`, it takes a whole number as a parameter and it return a factorial of the number
3. Call your function `is_empty`, it takes a parameter and it checks if it is empty or not
4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

### 高階題

1. Write a function called `is_prime`, which checks if a number is prime.
2. Write a functions which checks if all items are unique in the list.
3. Write a function which checks if all the items of the list are of the same data type.
4. Write a function which check if provided variable is a valid python variable
5. Go to the data folder and access the `countries-data.py` file.

   - Create a function called the `most_spoken_languages` in the world. It should return 10 or 20 most spoken languages in the world in descending order
   - Create a function called the `most_populated_countries`. It should return 10 or 20 most populated countries in descending order.
