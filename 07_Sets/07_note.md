# Day 7 - Sets 集合

## Set

Set is a collection of **unordered and un-indexed** distinct elements (items). In Python set is used to store **unique items**, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

### Creating a Set

- Creating an empty set with `set()`

    ```py
    # Create an empty set
    set1 = set()

    # Create a set with "h", "a", "p", "y" inside
    set2 = set("happy")
    ```

    However, if you are using `set()` to create a set, the arguments inside must be iterable.

- Creating a set with initial items

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    ```

    Noted that if you write something like this `vegetables = {}`, it will **NOT** create an empty set but an empty **dictionary**. You can use `type()` to check.

### Getting Set's Length

We can use `len()` to find the length of a set.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))  # 4
```

### Accessing Items in a Set

We use loops to access items.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}

for fruit in fruits:
    print(fruit)    # This will print out all items in set fruits
```

However, since a set in unordered, each time you execute the for loop, result might be different.

### Checking an item

To check if an item exist in a set we use `in` membership operator.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print("mango" in fruits)    # True
print("lime" in fruits)     # False
```

### Adding Items to a Set

Once a set is created we **cannot change any individual items**. But we can add or remove items from the set.

- Add one item using `add()`

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    fruits.add("lime")
    print(fruits)   # {'lemon', 'lime', 'orange', 'banana', 'mango'}
    ```

- Add multiple items using `update()`. The `update()` allows to add multiple items to a set. The `update()` takes a **list** as an argument.

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    fruits.update(["grape", "apple"])
    print(fruits)   # {'lemon', 'grape', 'apple', 'orange', 'banana', 'mango'}
    ```

### Removing Items from a Set

We can remove an item from a set using `remove()` method. If the item is not found `remove()` method will **raise errors**, so it is good to check if the item exist in the given set.  
However, you can also use `discard()` method, which doesn't raise any errors.

- Using `remove()`

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    fruits.remove("banana")
    print(fruits)   # {'lemon', 'orange', 'mango'}

    fruits.remove("apple") # Because there is no "apple" in the set, it will raise a KeyError.
    ```

- Using `discard()`

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    fruits.discard("banana")
    print(fruits)   # {'lemon', 'orange', 'mango'}

    fruits.discard("apple") # Although there is no "apple" in the set, Python will not raise any error and the set stay the same.
    ```

- Using `pop()`: Remove a **random** item from a set and it returns the removed item.

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    removed_fruit = fruits.pop()    # Removes a random item from the set which can be assigned to a variable as a value.
    print(removed_fruit)
    ```

### Clearing Items in a Set

If we want to clear or empty the set we use `clear()` method.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### Deleting a Set

If we want to delete the set itself we use `del` operator.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### Converting a List to a Set

We can convert a list to a set or convert a set to a list.  
Converting a list to a set will **remove duplicates and only unique items will be reserved**.

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Joining sets

We can join two sets using the `union()` or `update()` method.

- `union()` method returns a new set

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}

    foods = fruits.union(vegetables)

    print(fruits)       # {'banana', 'lemon', 'orange', 'mango'}
    print(vegetables)   # {'tomato', 'carrot', 'onion', 'cabbage', 'potato'}
    print(foods)        # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
    ```

- `update()` method inserts a set into a given set

    ```py
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
    fruits.update(vegetables)
    print(fruits)       # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
    ```

### Finding Intersection Items

`intersection()` returns a set of items which are in both the sets.

```py
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

word_set = python.intersection(dragon)
print(word_set)                 # {'o', 'n'}
print(python)               # {'h', 'p', 'n', 't', 'y', 'o'}
print(dragon)               # {'r', 'n', 'a', 'd', 'g', 'o'}
```

### Checking Subset and Super Set

A set can be a subset or super set of other sets, so we can check whether it is a subset or a super set by using `issubset()` and `issuperset()`. It will return a boolean.

- `issubset()`: Check if a subset or not

    ```py
    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.issubset(even_numbers) # False, because it is a super set
    ```

- `issuperset()`: Check if a superset or not

    ```py
    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.issuperset(even_numbers) # True
    ```

### Checking the difference between two sets

We can use `difference()` to check the difference between two sets and it returns **the difference as a set** between two sets.

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
different_numbers = whole_numbers.difference(even_numbers)
print(different_numbers)    # {1, 3, 5, 7, 9}
```

### Finding Symmetric Difference Between Two Sets

We can use `symmetric_difference()` to find symmetric different between two sets. It returns the the symmetric difference as a set between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

> Symmetric difference 對稱差集：該集合包含所有在 A 或 B 中但不在兩者同時存在的元素。這也可以理解為集合的對稱差集。

```py
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
sym_diff = python.symmetric_difference(dragon)
print(sym_diff)     # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

### Checking two sets are disjoint

If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are disjoint using `isdisjoint()` method.

> disjoint 是指兩個集合之間沒有任何共同元素。如果兩個集合是 disjoint，則它們的交集為空集。

```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
```

## 練習題

### 初階題

```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard

### 進階題

1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely

### 高階題

1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2. Explain the difference between the following data types: string, list, tuple and set
3. `I am a teacher and I love to inspire and teach people`. How many unique words have been used in the sentence? Use the `split` methods and set to get the unique words.
