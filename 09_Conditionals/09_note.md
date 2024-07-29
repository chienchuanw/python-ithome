# Day 8 - Conditionals 條件

## Conditionals

By default, statements in Python script are executed sequentially **from top to bottom**. If the processing logic require so, the sequential flow of execution can be altered in two way:

- Conditional execution: a block of one or more statements will be executed if a certain expression is `True`.
- Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is `True`. In this section, we will cover `if`, `else`, `elif` statements. The **comparison and logical operators** we learned in previous sections will be useful here.

### `if` condition

In python and other programming languages the key word `if` is used to check if a condition is `True` and to execute the block code. Remember the **indentation after the colon**.

```py
# Example
a = 3
if a > 0:
    print('A is a positive number') # A is a positive number
```

As you can see in the example above, 3 is greater than 0. The condition is `True` and therefore block code was executed. However, if the condition is `False`, we will not see the result. In order to see the result of the falsy condition, we should have another block, which is going to be `else`.

### `else` condition

If condition is `True` the first block will be executed, if not, which means it is `False`, the `else` condition will run.

```py
# Example

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

The example above could be shortened in one line as following syntax: `<code> if <condition> else <code>`.

```py
print('A' is a negative number) if a < 0 else print('A is a positive number')
```

The condition above shows that if the condition is `False`, the `else` block will be executed.  
How about if our condition is more than two? We could use `elif`.

### `elif` condition

In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use `elif` when we have **multiple conditions**.

```py
a = -1
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

Since `a = -1` matches the condition of `elif` statement, it will execute `print('A is a negative')`, and skip checking the `else` condition.

### Nested Conditions

Conditions can be nested.

```py
# Example

a = 2

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')   # This line will be executed
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

### `if` condition and Logical operators

#### `and` operator

Sometimes, writing nested conditions can be messy. We can avoid writing nested conditions by using the logical operator `and`. The `and` operator will check the conditions in order. If a condition is `True`, it will continue to examine the next condition and execute the code if all conditions return `True`. If any condition returns `False`, it will stop the evaluation immediately and jump to the next conditional statement, if there is one.

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')  # This line will be executed
else:
    print('A is negative')
```

#### `or` operator

Similar to the `and` operator, the `or` operator evaluates conditions in order. If any condition returns `True`, it will stop the evaluation and execute the nested code. Otherwise, it will examine all the conditions and jump to the next conditional statement if all the conditions return `False`.

```py
# Example

user = 'James'
access_level = 6
if user == 'admin' or access_level >= 4:
        print('Access granted!')    # it will execute this line since access_level is above 4
else:
    print('Access denied!')
```

## 練習題

### 初階題

1. Get user input using `input(“Enter your age: ”)`. If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. Compare the values of `my_age` and `your_age` using `if … else`. Who is older (me or you)? Use `input(“Enter your age: ”)` to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if `my_age == your_age`. Output:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. Get two numbers from the user using `input` prompt. If `a` is greater than `b` return `a` is greater than `b`, if `a` is less `b` return `a` is smaller than `b`, else `a` is equal to `b`. Output:

    ```sh
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
    ```

### 進階題

1. Write a code which gives grade to students according to theirs scores:

    ```sh
    90-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F
    ```

2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    - September, October or November, the season is Autumn.
    - December, January or February, the season is Winter.
    - March, April or May, the season is Spring
    - June, July or August, the season is Summer

3. The following list contains some fruits:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    If a fruit doesn't exist in the list, add the fruit to the list and print the modified list. If the fruit exists, print `'That fruit already exist in the list'`

### 高階題

1. Here we have a person dictionary. Feel free to modify it!

    ```py
    person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    ```

    - Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
    - Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    - If a person skills has only JavaScript and React, print('He is a frontend developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
    - If the person is married and if he lives in Finland, print the information in the following format:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```
