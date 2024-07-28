# Day 8 - Dictionaries 字典

## Dictionaries

A dictionary is a collection of **unordered, modifiable(mutable) paired (key: value)** data type.

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


