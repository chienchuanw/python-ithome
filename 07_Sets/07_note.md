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