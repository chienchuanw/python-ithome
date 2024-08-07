# Day 19 - File Handling

## File Handling

So far, we have seen different Python data types. We usually store our data in various file formats. In addition to handling files, we will also explore different file formats such as .txt, .json, .xml, .csv, .tsv, and .excel in this section. First, let us get familiar with handling files in the common .txt format.

File handling is an important part of programming that allows us to create, read, update, and delete files. In Python, to handle files, we use the built-in `open()` function.

```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t, b) could be to read, append, write, create, text, binary
```

- `"r"` as Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- `"a"` as Append - Opens a file for appending, creates the file if it does not exist
- `"w"` as Write - Opens a file for writing, creates the file if it does not exist
- `"x"` as Create - Creates the specified file, returns an error if the file exists
- `"t"` as Text - Default value. Text mode
- `"b"` as Binary - Binary mode (e.g. images)

### Opening Files for Reading

The default mode of open is reading, so we do not have to specify `r` or `rt`. I have created and saved a file named reading_file_example.txt in the files directory. Let us see how it is done:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

As you can see in the example above, I printed the opened file and it gave some information about it. Opened file has different reading methods: `read()`, `readline`, `readlines`. An opened file **has to be closed** with `close()` method.

- `read()`: read the whole text as **strings**. If we want to limit the number of characters we want to read, we can limit it by passing int value to the `read(number)` method.

    ```py
    f = open('./files/reading_file_example.txt')
    txt = f.read()
    print(type(txt)) # <class 'str'>
    print(txt)

    # Output
    '''
    This is an example to show how to open a file and read.
    This is the second line of the text.I love python
    '''

    f.close()
    ```

    Instead of printing all the text, let us print the first 10 characters of the text file.

    ```py
    f = open('./files/reading_file_example.txt')
    txt = f.read(10)
    print(type(txt)) # <class 'str'>
    print(txt)  # This is an

    f.close()
    ```

    If you try to apply `read()` method on a file which has been closed by `close()`, it will raise `ValueError: I/O operation on closed file.` on console. So remember to `open()` the file first before `read()`, and `close()` it when you are done.

- `readline()`: read only the first line

    ```py
    f = open('./files/reading_file_example.txt')
    line = f.readline()
    print(type(line)) # <class 'str'>
    print(line) # This is an example to show how to open a file and read.
    f.close()
    ```

- `readlines()`: read all the text line by line and returns a **list** of lines

    ```py
    f = open('./files/reading_file_example.txt')
    lines = f.readlines()
    print(type(lines))  # <class 'list'>
    print(lines)  # ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.I love python']
    f.close()
    ```

Another way to get all the lines as a **list** is using `splitlines()`:

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
lines = txt.splitlines()
print(type(lines))  # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.', 'This is the second line of the text.I love python']
f.close()
```

### Opening Files for Writing and Updating

To write to an existing file, we must add a mode as parameter to the `open()` function:

- `"a"` as append: will append to the end of the file. If the file does not exist, it creates a new file.
- `"w"` as write: will overwrite any existing content. If the file does not exist, it creates a new file.

Let us append some text to the file we have been reading:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

The method below creates a new file, if the file does not exist:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Deleting Files

We have seen how to make and remove a directory using `os` module before. Again now, if we want to remove a file we use `os` module.

```py
import os
os.remove('./files/writing_file_example.txt')
```

If the file does not exist, the remove method will raise a `FileNotFoundError`, so it is good to use a condition like this:

```py
import os
if os.path.exists('./files/writing_file_example.txt'):
    os.remove('./files/writing_file_example.txt')
else:
    print('The file does not exist')
```

## File Types

### File with `txt` Extension

File with `txt` extension is a very common form of data and we have covered it in the previous section. Let us move to the `json` file.

### File with `json` Extension

JSON stands for **JavaScript Object Notation**. Actually, it is a **stringified JavaScript object** or **Python dictionary**.

Example:

```py
# dictionary
person_dict = {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React", "Python"]
}'''
```

#### Changing JSON to Dictionary

To change a JSON to a Python dictionary, first we import the `json` module and then we use `loads` method.

```py
import json

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

# let's change JSON to dictionary
person_dict = json.loads(person_json)
print(person_dict) # {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
print(type(person_dict)) # <class 'dict'>
print(person_dict['name']) # Asabeneh
```

#### Changing Dictionary to JSON

To change a Python dictionary to a JSON, we use `dumps` method from the `json` module.

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

# let's convert it to json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(person_json)
print(type(person_json))
```

Output:

```console
# output
# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.

{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
<class 'str'>
```

#### Saving as JSON File

We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the `json.dump()` method, it can take arguments like `dictionary`, `output file`, `ensure_ascii` and `indent`.

```py
import json

# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


# Alternative Solution
import json

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Open file
f = open('./files/json_example.json', 'w', encoding='utf-8')

# Write json
json.dump(person, f, ensure_ascii=False, indent=4)

# Close file
f.close()
```

In the code above, we use encoding and indentation. Indentation makes the json file easy to read.

### File with `csv` Extension

CSV stands for **Comma Separated Values**. CSV is a simple file format used to store tabular data, such as a **spreadsheet** or **database**. CSV is a very common data format in data science.

Example:

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

Example:

```py
import csv

# Create or overwrite csv_example.csv
with open("./files/csv_example.csv", "w") as f:
    f.write(
        '''"name","country","city","skills"
            "Asabeneh","Finland","Helsinki","JavaScrip"'''
    )

# Read and output texts
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines: {line_count}')
```

```console
Column names are :name, country, city, skills
                    "Asabeneh" is a teachers. He lives in Finland, Helsinki.
Number of lines: 2
```

### File with `xlsx` Extension

To read excel files we need to install `xlrd` package. We will cover this after we cover package installing using `pip`. Notice that `xlrd` no longer supports Excel 2007 or later. You have to use `openpyxl` package instead of `xlrd`

```py
# This will NOT work for xlsx extension
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

# Use openpyxl instead
import openpyxl
excel_book = openpyxl.load_workbook('./files/excel_example.xlsx')
print(excel_book.sheetnames)
print(len(excel_book.sheetnames))
```

### File with `xml` Extension

XML is another structured data format which looks like HTML. In XML, the tags are not predefined. The first line is an XML declaration. The person tag is **the root of the XML**. The person has a gender attribute.

Example:

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

For more information on how to read an XML file check the [documentation](https://docs.python.org/2/library/xml.etree.elementtree.html)

```py
import xml.etree.ElementTree as ET

tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```

Output:

```console
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```
