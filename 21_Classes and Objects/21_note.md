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

To create a class we need the key word class followed by the name and colon. Class name should be **CamelCase**.

