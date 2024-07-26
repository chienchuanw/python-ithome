# Day 5 - Lists 串列

## Lists

There are four collection data types in Python :

- List: is a collection which is **ordered and changeable** (modifiable). Allows duplicate members.
- Tuple: is a collection which is **ordered and unchangeable** or **unmodifiable(immutable)**. Allows duplicate members.
- Set: is a collection which is **unordered, un-indexed and unmodifiable**, but we can add new items to the set. **Duplicate members are not allowed**.
- Dictionary: is a collection which is **unordered, changeable(modifiable)** and indexed. **No duplicate members**.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

### How to create a list

There are two ways to create lists in Python:

- Using list built-in function `list()`

    ```py
    list_one = list()       # list_one is now an empty list with no item inside
    print(len(list_one))    # 0

    list_new = list("apple")
    print(list_new)         # ['a', 'p', 'p', 'l', 'e']
    ```

    However, if you are using `list()` to create a list, the arguments inside must be iterable.

- Using square brackets `[]`

    ```py
    list_two = []
    print(len(list_two))    # 0
    ```

We can use `len()` to find the length of a list. The length is equal to the quantity of items inside a list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))          # 4
```

Lists can have items of **different data types**.

```py
list_three = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]  # A list can contain different data types
```

### Accessing list items using positive index

We access each item in a list using their index. A list index starts from `0`.  
The code below shows clearly where the index starts:

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
# index      0          1        2        3
```

### Accessing list items using negative index

Negative indexing means counting the items from the end.  
`-1` refers to the last item, `-2` refers to the second to last item.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
# index     -4         -3        -2      -1
```

### Unpacking list items

We can use `*` to collect the remaining items. No matter how items left, the item collected by `*` will always be a list.

```py
list_four = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = list_four

print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

a, b, *c, d, e = list_four
print(a, b, c, d, e)    # item1 item2 ['item3'] item4 item5
```

```py
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 

print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']

# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]

print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries

print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### slicing items from a list

- Positive Indexing: We can specify a range of positive indexes by specifying the `start`, `end` and `step`, the return value will be a new **list**. (default values for `start=0`, `end=len(list)`, `step=1`)  

The syntax is `[<start>:<end>:<step>]`

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits

# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
banana_orange_mango = fruits[:3]
banana_and_mango = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
```

- Negative Indexing: We can specify a range of negative indexes by specifying the `start`, `end` and `step`, the return value will be a new **list**.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
no_fruits = fruits[-3:-1] # Since there's no item to slice, it will give an empty list
```

### Modify a list

List is a mutable or modifiable ordered collection of items.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### Checking items in a list

Checking an item if it is a member of a list using `in` operator.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### Adding items to a list

We use the method `append()` to add items to the end of an existing list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### Inserting items to a list

We can use `insert()` method to insert a item at a specified index in a list. **The other items are shifted to the right**.  
`insert()` methods takes two arguments: **index** and **an item to insert**.
Noted that `insert()` method can only **one item** to the list at a time.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### Removing items from a list

- The `remove()` method removes a specified item from a list. It can only remove **one item** at a time.

    ```py
    fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
    fruits.remove('banana')
    print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
    fruits.remove('lemon')
    print(fruits)  # ['orange', 'mango', 'banana']
    ```

- The `pop()` method removes the specific item with an index, or the last item if index is not specified. The difference between `pop()` and `remove()` is that you can assign the item you pop to another variable.

    ```py
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.pop()
    print(fruits)       # ['banana', 'orange', 'mango']

    only_banana = fruits.pop(0)
    print(fruits)       # ['orange', 'mango']
    print(only_banana)  # 'banana'
    ```

- The `clear()` method empties a list.

    ```py
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.clear()
    print(fruits)       # []
    ```

### Deleting a list

The `del` keyword removes the specified index and it can also be used to delete items within index range. It can also delete the entire list. If you delete a list with `del` keyword, it will be **wiped out from the memory**s and the variable will thus be non-existed.

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```

### Copying a list

It is possible to copy a list by reassigning it to a new variable in the following way: `list2 = list1`. Now, `list2` is a reference of `list1`, any changes we make in `list2` will also modify the original, which is `list1`.  
But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using `copy()`.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### Joining a list

There are several ways to join, or in other words, "concatenate," two or more lists in Python.

- Plus operator `+`

    ```py
    positive_numbers = [1, 2, 3, 4, 5]
    zero = [0]
    negative_numbers = [-5,-4,-3,-2,-1]
    integers = negative_numbers + zero + positive_numbers
    print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    fruits = ['banana', 'orange', 'mango', 'lemon']
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
    fruits_and_vegetables = fruits + vegetables
    print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
    ```

- `extend()` method: The `extend()` allows to append an **iterable object** like a list or a string in a list.

```py
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

alphabets = ["a", "b" ,"c"]
word = "nice"
alphabets.extend(word)
print(alphabets)    # ['a', 'b', 'c', 'n', 'i', 'c', 'e']
```

### Counting Items in a List

The `count()` method returns the number of times an item appears in a list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### Finding Index of an Item

The `index()` method returns the index of an item in the list. It will only return the index of the first occurrence item.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

### Reversing a List

The `reverse()` method reverses the order of a list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

### Sorting List Items

To sort lists we can use `sort()` method or `sorted()` built-in functions.  
The `sort()` method reorders the list items in **ascending order** and **modifies the original list**.  
If an argument of `sort()` method `reverse` is equal to `True`, it will arrange the list in **descending order**.

- `sort()`: this method modifies the original list.

    ```py
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.sort()
    print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']

    fruits.sort(reverse=True)
    print(fruits) # ['orange', 'mango', 'lemon', 'banana']

    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    ages.sort()
    print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

    ages.sort(reverse=True)
    print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
    ```

- `sorted()`: returns the ordered list **without modifying the original list**.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```

Noted the main difference `sort()` and `sorted()` are:

- `sort()` is one of the methods of `List`, which can be only used on a list object.
- `sorted()` is a built-in function. It can be used on any iterable objects like lists, tuples, strings, etc. And it will return a list.

## 練習題

### 初階題

1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```

27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

### 進階題

1. The following is a list of 10 students ages:

    ```sh
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ```

   - Sort the list and find the min and max age
   - Add the min age and the max age again to the list
   - Find the median age (one middle item or two middle items divided by two)
   - Find the average age (sum of all items divided by their number )
   - Find the range of the ages (max minus min)
   - Compare the value of (min - average) and (max - average), use _abs()_ method

2. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
