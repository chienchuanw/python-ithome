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
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
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
