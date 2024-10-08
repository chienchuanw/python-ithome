# Day 21 - Classes and Objects 類別與物件

## Classes and Objects

Python is an **object oriented programming language**. **Everything in Python is an object**, with its **properties** and **methods**. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding **built-in class**. We create class to create an object. A class is like an **object constructor**, or a "blueprint" for creating objects. We **instantiate** a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

We have been working with classes and objects right from the beginning of this challenge unknowingly. Every element in a Python program is an object of a class. Let us check if everything in python is a class:

```py
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Creating a Class

To create a class we need the key word `class` followed by the name and colon. Class name should be **CamelCase** like `ThisIsClassName`.

```py
# Example 
class Person: 
    pass

print(Person) # <class '__main__.Person'>
```

### Creating an Object

We can create an object by calling the class. This step is also known as "instantiating a class".

```py
p = Person()
print(p)  # <__main__.Person object at 0x104e9c140>
```

### Class Constructor

In the examples above, we have created an object from the `Person` class. However, a class without a constructor is not really useful in real applications. Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in `init()` constructor function. The init constructor function has self parameter which is a reference to the current instance of the class.

```py
class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name

p = Person('Frank')

print(p.name) # Frank
print(p)  # <__main__.Person object at 0x100c694f0>
```

Let us add more parameters to the constructor function.

```py
class Person:
    def __init__(self, first_name, last_name, age, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city

p = Person("Frank", "Wang", 30, "Taiwan", "Taipei")
print(p.first_name) # Frank
print(p.last_name)  # Wang
print(p.age)  # 30
print(p.country)  # Taiwan
print(p.city) # Taipei
```

### Object Methods

Objects can have methods. The methods are functions which belong to the object.

Example:

```py
class Person:
    def __init__(self, first_name, last_name, age, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}."

p = Person("Frank", "Wang", 30, "Taiwan", "Taipei")
print(p.person_info()) # Frank Wang is 30 years old. He lives in Taipei, Taiwan.
```

### Object Default Methods

Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:

```py
class Person:
    def __init__(self, first_name='Asabeneh', last_name='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info()) # Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
p2 = Person('John', 'Doe', 30, 'New York', 'USA')
print(p2.person_info()) # John Doe is 30 years old. He lives in USA, New York.
```

### Method to Modify Class Default Values

In the example below, the person class, all the constructor parameters have default values. In addition to that, we have skills parameter, which we can access using a method. Let us create `add_skill` method to add skills to the skills list.

```py
class Person:
    def __init__(self, first_name='Asabeneh', last_name='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}.'
        
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info()) # Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'New York', 'USA')
print(p2.person_info()) # John Doe is 30 years old. He lives in USA, New York.

print(p1.skills)  # ['HTML', 'CSS', 'JavaScript']
print(p2.skills)  # []
```