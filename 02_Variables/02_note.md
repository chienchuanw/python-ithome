# Day 2 - 變數與內建函數

## Built-in functions

使用 `help()` 來查詢 Python 關鍵字（Keyword）。  

```py
# 打開 help 清單
help()
```

```py
# 使用 help 函數查詢 Python keywords 有哪些
help("keywords")
```

- `dir()`
    The `dir()` function, when called without arguments, returns the list of names in the current local scope. This includes all variables, functions, and imported modules that are currently available in the local namespace.

    ```py
    # Example: dir() without arguments

    # Defining a variable
    a = 5

    # Defining a function
    def my_function():
        pass

    # Calling dir() without arguments
    print(dir())

    # Output will include 'a', 'my_function', and other default names
    ```

- `dir(object)`
    When dir() is called with an object as an argument, it attempts to return a list of valid attributes for that object. This list includes methods, properties, and other attributes that the object has.  

  - Example with a Built-in Object:

    ```py
    # Example: dir() with a built-in object

    # Calling dir() with a string object
    print(dir("hello"))

    # Output will include methods like 'upper', 'lower', 'find', etc.
    ```

  - Example with a Custom Class:

    ```py
    # Example: dir() with a custom object

    # Defining a custom class
    class MyClass:
        def __init__(self):
            self.attribute = 10

        def my_method(self):
            pass

    # Creating an instance of MyClass
    obj = MyClass()

    # Calling dir() with the custom object
    print(dir(obj))

    # Output will include 'attribute', 'my_method', and other default attributes
    ```

## Variables  

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated.  
A variable refers to a memory address in which data is stored. **Number at the beginning, special character, hyphen** are **not allowed** when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.  

**Python Variable Name Rules**  

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables

```py
# Valid variable names
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2

# Invalid variable names
first-name
first@name
first$name
num-1
1num
```

Python developers use **snake case** (`snake_case`) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. `first_name`, `last_name`, `engine_rotation_speed`).  

When we assign a certain data type to a variable, it is called **variable declaration**. For instance in the example below my first name is assigned to a variable `first_name`. The equal sign `=` is an **assignment operator**. Assigning means **storing data in the variable**. The equal sign in Python is **not** equality as in Mathematics.  

```py
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

`print()` function takes unlimited number of arguments. An **argument** is a value which we can be passed or put inside the function parenthesis, see the example below.  

```py
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
```

We can also use `len()` to calculate the number of characters in the string. It can also return the number of items in a list.  

```py
first_name = "Frank"
print("First name: ", first_name) # 'First name: Frank'
print("First name length: ", len(first_name))   # 'First name length: 5'
```

### Declaring Multiple Variable in a Line

Multiple variables can also be declared in one line:

```py
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

We can also use `input()` to get user input and use it as a value in a variable.  

```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## Data Types

There are several data types in Python. To identify the data type we use the `type()` built-in function.  

### Checking Data types and Casting

- Check Data types: To check the data type of certain data/variable we use the `type()`.

    ```py
    # Different python data types
    # Let's declare variables with various data types

    first_name = 'Asabeneh'     # str
    last_name = 'Yetayeh'       # str
    country = 'Finland'         # str
    city= 'Helsinki'            # str
    age = 250                   # int, it is not my real age, don't worry about it

    # Printing out types
    print(type('Asabeneh'))     # str
    print(type(first_name))     # str
    print(type(10))             # int
    print(type(3.14))           # float
    print(type(1 + 1j))         # complex
    print(type(True))           # bool
    print(type([1, 2, 3, 4]))     # list
    print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
    print(type((1,2)))                                              # tuple
    print(type(zip([1,2],[3,4])))                                   # set
    ```

- Casting: Converting one data type to another data type. We use `int()`, `float()`, `str()`, `list()`, `set()`. When we do arithmetic operations, string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string.  

    > note: `int()` 是無條件捨去後才轉換為整數。

    ```py
    # int to float
    num_int = 10
    print('num_int',num_int)         # 10
    num_float = float(num_int)
    print('num_float:', num_float)   # 10.0

    # float to int
    gravity = 9.81
    print(int(gravity))             # 9

    # int to str
    num_int = 10
    print(num_int)                  # 10
    num_str = str(num_int)
    print(num_str)                  # '10'

    # str to int or float
    num_str = '10.6'
    print('num_int', int(num_str))      # 10
    print('num_float', float(num_str))  # 10.6

    # str to list
    first_name = 'Asabeneh'
    print(first_name)               # 'Asabeneh'
    first_name_to_list = list(first_name)
    print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
    ```

## 練習題

### 基礎題

1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named `variables.py`
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line

### 進階題

1. Check the data type of all your variables using `type()` built-in function
2. Using the `len()` built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
    i. Add num_one and num_two and assign the value to a variable total
    ii. Subtract num_two from num_one and assign the value to a variable diff
    iii. Multiply num_two and num_one and assign the value to a variable product
    iv. Divide num_one by num_two and assign the value to a variable division
    v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    vi. Calculate num_one to the power of num_two and assign the value to a variable exp
    vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
5. The radius of a circle is 30 meters.
    i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
    ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    iii. Take radius as user input and calculate the area.
6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
7.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
