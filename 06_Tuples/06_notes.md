# Day 6 - Tuples 元組

## Tuples

A tuple is a collection of **different data types** which is **ordered and unchangeable (immutable)**. Tuples are written with round brackets, `()`.  
Since a tuple is immutable, once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple. Unlike list, tuple has only few methods.  

Methods related to tuples:

- `tuple()`: to create an empty tuple
- `count()`: to count the number of a specified item in a tuple
- `index()`: to find the index of a specified item in a tuple
  - operators like to join two or more tuples and create a new tuple

### Creating a Tuple

- Create an empty tuple with `tuple()`

    ```py
    tuple_one = tuple()
    ```

    However, if you are using `tuple()` to create a tuple, the arguments inside must be iterable.

- Create a tuple with initial values

    ```py
    tuple_two = ("item1", "item2", "item3")
    ```

### Tuple length

We can use `len()` to get the length of a tuple.

```py
tuple_three = ("item1", "item2", "item3")
print(len(tuple_three)) # 3
```

### Accessing Tuple Items

- Positive Indexing: Similar to the `list` data type we use positive or negative indexing to access tuple items which starts from `0`.

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    #             0         1        2         3 
    first_fruit = fruits[0]
    second_fruit = fruits[1]
    last_index =len(fruits) - 1
    last_fruit = fruits[las_index]
    ```

- Negative Indexing: Negative indexing means beginning from the end, `-1` refers to the last item, `-2` refers to second to last and the negative of the `list`/`tuple` length refers to the first item.

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
#            -4        -3       -2        -1
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```

### Slicing Tuples

We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

- Range of Positive Indexes

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    all_fruits = fruits[0:4]    # all items
    all_fruits= fruits[0:]      # all items
    orange_mango = fruits[1:3]  # doesn't include item at index 3
    orange_to_the_rest = fruits[1:]
    ```

- Range of Negative Indexes

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    all_fruits = fruits[-4:]    # all items
    orange_mango = fruits[-3:-1]  # doesn't include item at index 3
    orange_to_the_rest = fruits[-3:]
    ```

### Changing a Tuple to a List

We can change tuples to lists and lists to tuples. Because a tuple is immutable if we want to modify a tuple we should change it to a list.

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### Checking an Item in a tuple

We can check if an item exists or not in a tuple using `in`, it returns a **boolean**.

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### Joining Tuples

We can join two or more tuples using + operator

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### Deleting Tuples

It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using **del**.

```py

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

## 練習題

### 初階題

1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

### 進階題

1. Unpack siblings and parents from family_members
2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
5. Slice out the first three items and the last three items from food_staff_lt list
6. Delete the food_staff_tp tuple completely
7. Check if an item exists in  tuple:

    - Check if 'Estonia' is a nordic country
    - Check if 'Iceland' is a nordic country

    ```py
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    ```
