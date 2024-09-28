# Day 10 - Loops 迴圈

## Loop

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use **loops**. Python programming language also provides the following types of two loops:

- `while` loop
- `for` loop

### While loop

We use the reserved word `while` to make a while loop. It is used to execute a block of statements repeatedly **until a given condition is satisfied**. When the condition becomes `False`, the lines of code after the loop will be continued to be executed.

```py
# Example
count = 0
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4
```

In the above while loop, the condition becomes `False` when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use `else`.

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

The above loop condition will be `False` when count is 5 and the loop stops, and execution starts the `else` statement. As a result `5` will be printed.

### Break and Continue - Part 1

#### `break`

We use `break` get out of or stop the loop.

```py
# Example
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

The above while loop only prints `0`, `1`, `2`, but when it reaches `3` it stops.

#### `continue`

With the `continue` statement we can **skip** the current iteration, and continue with the next.

```py
# Example
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
```

The above while loop only prints `0`, `1`, `2` and `4` (skips `3`).

### For loop

A `for` keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for **iterating over a sequence** (that is either a list, a tuple, a dictionary, a set, or a string).

- For loop with a list

    ```py
    numbers = [0, 1, 2, 3, 4, 5]
    for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
        print(number)       # the numbers will be printed line by line, from 0 to 5
    ```

- For loop with a string

    ```py
    language = 'Python'
    for letter in language:
        print(letter)   # print "P", "y", "t", "h", "o", "n" in separate lines


    for i in range(len(language)):
        print(language[i])  # print "P", "y", "t", "h", "o", "n" in separate lines
    ```

- For loop with a tuple

    ```py
    numbers = (0, 1, 2, 3, 4, 5)
    for number in numbers:
        print(number)
    ```

- For loop with a dictionary

    ```py
    person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_marred':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }

    for key in person:
        print(key)  # This will print out all keys in the dictionary

    for key, value in person.items():
        print(key, value)   # This will print out all key-value pairs in the dictionary
    ```

- For loop with a set

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)  # This will print out all item in the set in separate line.
```

### Break and Continue - Part 2

#### `break` in for loop

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

In the above example, the loop stops when it reaches `3`.

#### `continue` in for loop

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) 
    if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

In the example above, if the number equals `3`, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

### The Range Function

The `range()` function is used list of numbers. The `range(start, end, step)` takes three parameters: **starting, ending and increment**. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end).

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### Nested For Loop

We can write loops inside a loop.

```py
person = {
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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)    # This will print out 'JavaScript', 'React', 'Node', 'MongoDB', 'Python' in separate lines
```

### `else` in for loop

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number) # 'The loop stops at 10'
```

### Pass

In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word `pass` to avoid errors. Also we can use it as a placeholder, for future statements.

```py
for number in range(6):
    pass    # This will do nothing but keep running the for loop until it ends
```

## 練習題

### 初階題

1. Iterate 0 to 10 using for loop, do the same using while loop.
2. Iterate 10 to 0 using for loop, do the same using while loop.
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Use nested loops to create the following:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Print the following pattern:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
7. Use for loop to iterate from 0 to 100 and print only even numbers
8. Use for loop to iterate from 0 to 100 and print only odd numbers

### 進階題

1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.

   ```sh
   The sum of all numbers is 5050.
   ```

2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

    ```sh
    The sum of all evens is 2550. And the sum of all odds is 2500.
    ```

### 高階題

1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
3. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.

   1. What are the total number of languages in the data
   2. Find the ten most spoken languages from the data
   3. Find the 10 most populated countries in the world
