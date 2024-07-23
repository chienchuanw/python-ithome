# Day 3 - 運算子

## Boolean 布林值

```py
print(True)
print(False)
```

## Operators 運算子

### Assignment Operators

Assignment operators are used to **assign values to variables**.  
Equal sign `=` in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable.  

Operator    Example     Same As  
`=`         `x = 5`     `x = 5`  
`+=`        `x += 5`    `x = x + 5`  
`-=`        `x -= 3`    `x = x - 3`  
`*=`        `x *= 3`    `x = x * 3`  
`/=`        `x /= 3`    `x = x / 3`  
`%=`        `x %= 3`    `x = x % 3`  
`//=`       `x //= 3`   `x = x // 3`  
`**=`       `x **= 3`   `x = x ** 3`  
`&=`        `x &= 3`    `x = x & 3`  
`|=`        `x |= 3`    `x = x | 3`  
`^=`        `x ^= 3`    `x = x ^ 3`  
`>>=`        `x >>= 3`    `x = x >> 3`  
`<<=`        `x <<= 3`    `x = x << 3`  

**Bitwise 按位運算**  
將數字轉為二進位，然後執行按位與操作。  

- `&`: 按位與運算 bitwise AND
    按位與運算符 `&` 對兩個數字的每一位執行按位與操作。如果對應位都為 `1`，則結果為 `1`，否則為 `0`。
- `|`: 按位或運算 bitwise OR
    按位或運算符 `|` 對兩個數字的每一位執行按位或操作。如果對應位中至少有一位是 `1`，則結果為 `1`，否則為 `0`。  
- `^`: 按位異或運算 bitwise XOR
    按位異或運算符 `^` 對兩個數字的每一位執行按位異或操作。如果對應位不同，則結果為 `1`，如果對應位相同，則結果為 `0`。
- `>>`: 右移運算 bitwise right shift
    右移運算符 `>>` 將數字的二進制表示向右移動指定的位數。移動後左邊的空位由 `0` 補充，右邊移出的位置被丟棄。
- `<<`: 左移運算 bitwise left shift
    左移運算符 `<<` 將數字的二進制表示向左移動指定的位數。移動後右邊的空位由 `0` 補充，左邊移出的位數被丟棄。

### Arithmetic Operators

- Addition(`+`): `a + b`
- Subtraction(`-`): `a - b`
- Multiplication(`*`): `a * b`
- Division(`/`): `a / b`
- Modulus(`%`): `a % b`
- Floor division(`//`): `a // b`
- Exponentiation(`**`): `a ** b`

```py
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)
```

### Comparison Operators

We use comparison operators to **compare two values**. We check if a value is greater or less or equal to other value.  

Operator    Name                        Example  
`==`        Equal                       `x == y`  
`!=`        Not equal                   `x != y`  
`>`         Greater                     `x > y`  
`<`         Less than                   `x < y`  
`>=`        Greater than or equal to    `x >= y`  
`<=`        Less than or equal to       `x <= y`  

In addition to the above comparison operator Python uses:

- `is`: Returns true if both variables are the same object (`x is y`)
- `is not`: Returns true if both variables are not the same object (`x is not y`)
- `in`: Returns `True` if the queried list contains a certain item (`x in y`)
- `not in`: Returns `True` if the queried list doesn't have a certain item (`x not in y`)

```py
print('1 is 1', 1 is 1)                     # True - because the data values are the same
print('1 is not 2', 1 is not 2)             # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')   # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')   # False - there is no uppercase B
print('coding' in 'coding for all')         # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')              # True
print('4 is 2 ** 2:', 4 is 2 ** 2)          # True
```

### Logical Operators

Logical operators are used to combine conditional statements.  

Operator    Description                                                 Example  
`and`       Returns `True` if both statements are true                  `x < 5 and x < 10`
`or`        Returns `True` if one of the statements is true             `x < 5 or x < 4`  
`not`       Reverse the result, returns `False` if the result is true   `not (x < 5 and x < 10)`  

```py
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

## 練習題

1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

    ```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
    ```

5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

    ```py
    Enter side a: 5
    Enter side b: 4
    Enter side c: 3
    The perimeter of the triangle is 12
    ```

6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text python and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

    ```py
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
    ```

22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.

    ```py
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
    ```

23. Write a Python script that displays the following table

    ```py
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
    ```
