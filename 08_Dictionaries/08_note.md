# Day 8 - Dictionaries 字典

## Dictionaries

A dictionary is a collection of **unordered, modifiable(mutable) paired (key: value)** data type. And a value of dictionary could be any data types: strings, boolean, list, tuple, set, or dictionary as well.

### Creating a Dictionary

To create a dictionary we use curly brackets, `{}` or the `dict()` built-in function.

- Using `{}` to create a dictionary

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
    ```

- Using `dict()` to create a dictionary

    ```py
    # Passing an iterable object as an argument
    dict1 = dict([('name', 'John'), ('age', 30), ('city', 'New York')])
    print(dict1)  # {'name': 'John', 'age': 30, 'city': 'New York'}

    # Using keyword arguments 
    dict2 = dict(name='John', age=30, city='New York')
    print(dict2)  # {'name': 'John', 'age': 30, 'city': 'New York'}

    # Passing an existing dictionary as an argument to create a new dictionary
    existing_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    dict3 = dict(existing_dict)
    print(dict3)  # {'name': 'John', 'age': 30, 'city': 'New York'}
    ```

- Using `zip()` function to create a dictionary requires the keys and values to be saved in a tuple or a list.

    ```py
    keys = ['name', 'age', 'city']
    values = ['John', 30, 'New York']
    dict4 = dict(zip(keys, values))
    print(dict4)  # {'name': 'John', 'age': 30, 'city': 'New York'}
    ```

### Dictionary Length

We can use `len()` to check the number of "key, value" pairs in a dictionary.

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
print(len(person)) # 7
```

### Accessing Dictionary Items

We can access a dictionary item by referring to its key name.

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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

Accessing an item by key name raises an error if the key does not exist. To avoid this error, first we have to check if a key exist or we can use the `get()` method. The `get()` method returns `None`, which is a NoneType object data type, if the key does not exist.

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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Adding Items to a Dictionary

We can add new key and value pairs to a dictionary with several ways like `[]`, `update()`, `setdefault()`.

- Using `[]` square brackets: This allows user to add a key-value pair directly to a dictionary.

```py
my_dict = {'name': 'John', 'age': 30}

my_dict['city'] = 'New York'
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
```

- Using `update()` method: This allows user to add multiple key-value pairs via another dictionary or keyword arguments.

    ```py
    my_dict = {'name': 'John', 'age': 30}

    # Updating with another dictionary 
    my_dict.update({'city': 'New York', 'job': 'Developer'})
    print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Developer'}

    # Updating with keyword arguments
    my_dict.update(gender="male", status="single")
    print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Developer', 'gender': 'male', 'status': 'single'}
    ```

- Using `setdefault()` method: This allows user to add a key-value pair. If the pair is already existed, **it will return value of the key**. If the pair is not exist, it will **add the pair to the dictionary and return value of the key**. However if a user tries to use `setdefault()` to update an existed key-pair, it **will not be updated** and thus **return the original value of the key**.

```py
my_dict = {'name': 'John', 'age': 30}

# Add a non-exist key-value pair
return1 = my_dict.setdefault('city', 'New York')
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
print(return1)  # 'New York'

# Add an existed key-value pair
return2 = my_dict.setdefault('name', 'John')
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
print(return2)  # 'John'

# Add an existed key-value pair with different value
return3 = my_dict.setdefault('age', 18)
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
print(return3)  # 30
```

### Modify Items in a Dictionary

We can also use `[]` square brackets to modify (update) an existed item in a dictionary.

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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Checking keys in a dictionary

We use the `in` operator to check if a **key** exist in a dictionary. Remember the `in` operator it **only checks keys, values are not included**.

```py
my_dict = {'name': 'John', 'age': 30}

print("name" in my_dict)    # True
print("gender" in my_dict)  # False
print("John" in my_dict)    # False
```

### Removing Key and Value Pairs from a Dictionary

- `pop()`: removes the item with specified **key** name. It will return **value of the popped key**.

    ```py
    person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_married':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }

    person.pop('first_name')        # Removes the firstname item
    ```

- `popitem()`: removes the last item. It will return **value of the popped key**.

    ```py
    person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_married':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }

    person.popitem()                # Removes the address item
    ```

- `del`: removes (destroys) an item with specified key name.

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

del person['is_married']        # Removes the is_married item
```

### Changing Dictionary to a List of items

The `items()` method changes key-value pair of dictionary to a **list of tuples** as a **view object**. A view object in Python provides a dynamic view of dictionary keys, values, or items, reflecting real-time changes to the dictionary.

```py
my_dict = {'name': 'John', 'age': 30}
my_tuple = my_dict.items()
print(my_tuple) # dict_items([('name', 'John'), ('age', 30)])

# Since it's a view object, you have to convert to a list or use a for loop to iterate
for t in my_tuple:
    print(t)
```

### Clearing a Dictionary

If we don't want the items in a dictionary we can clear them using `clear()` method.

```py
my_dict = {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict) # my_dict
```

### Deleting a Dictionary

If we do not use the dictionary we can use `del` delete it completely.

```py
my_dict = {'name': 'John', 'age': 30}
del my_dict
```

### Copying a Dictionary

Just like a list, when you reassign a dictionary to another variable, it will referencing the original dictionary. Any modification between these two variable will affect one another. We can copy a dictionary using a `copy()` method to avoid the problem mentioned earlier. Using `copy()` we can avoid mutation of the original dictionary.

```py
my_dict = {'name': 'John', 'age': 30}
copied_dict = my_dict.copy()

copied_dict["gender"] = "male"
print(copied_dict)  # {'name': 'John', 'age': 30, 'gender': 'male'}
```

### Getting Dictionary Keys

The `keys()` method gives us all the keys of a dictionary as a **view object**. It will reflect the change of keys in the dictionary dynamically. Since a view object is iterable, you can use `for` loop to get item individually or covert it to a list.

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

person_keys = person.keys()
print(person_keys)  # dict_keys(['first_name', 'last_name', 'age', 'country', 'is_married', 'skills', 'address'])

person["gender"] = "male"
print(person_keys)  # dict_keys(['first_name', 'last_name', 'age', 'country', 'is_married', 'skills', 'address', 'gender'])
```

### Getting Dictionary Values as a List

The `values()` method gives us all the values of a dictionary as a **view object**. It will reflect the change of values in the dictionary dynamically. Since a view object is iterable, you can use `for` loop to get item individually or covert it to a list.

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

person_values = person.values()
print(person_values)  # dict_values(['Asabeneh', 'Yetayeh', 250, 'Finland', True, ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], {'street': 'Space street', 'zipcode': '02210'}])

person["gender"] = "male"
print(person_values)  # dict_values(['Asabeneh', 'Yetayeh', 250, 'Finland', True, ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], {'street': 'Space street', 'zipcode': '02210'}, 'male'])
```

## 練習題

1. Create an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using _items()_ method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries
