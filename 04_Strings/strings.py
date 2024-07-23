# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print(" ".join(["Thirty", "Days", "Of", "Python"]))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print("%s %s %s" % ("Coding", "For", "All"))

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

company.upper()

# Change all the characters to lowercase letters using lower() method.

company.lower()

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

company.capitalize()
company.title()
company.swapcase()

# Cut(slice) out the first word of Coding For All string.

company.split(" ")[0]

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

company.find("Coding")

# Replace the word coding in the string 'Coding For All' to Python.

company.replace("Coding", "Python")

# Change Python for Everyone to Python for All using the replace method or other methods.

"Python for Everyone".replace("Everyone", "All")

# Split the string 'Coding For All' using space as the separator (split()) .

"Coding For All".split(" ")

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")

# What is the character at index 0 in the string Coding For All.

print("Coding For All"[0] == "C")

# What is the last index of the string Coding For All.

last_index = len("Coding For All") - 1

# What character is at index 10 in "Coding For All" string.

print("Coding For All"[10] == " ")

# Create an acronym or an abbreviation for the name 'Python For Everyone'.


def abbr(name: str):
    print("".join([word[0] for word in name.split(" ")]))


abbr("Python For Everyone")

# Create an acronym or an abbreviation for the name 'Coding For All'.

abbr("Coding For All")

# Use index to determine the position of the first occurrence of C in Coding For All.

first_occurrence_C = 0
print("Coding For All"[first_occurrence_C] == "C")

# Use index to determine the position of the first occurrence of F in Coding For All.

first_occurrence_F = 7
print("Coding For All"[first_occurrence_F] == "F")

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

last_occurrence_l = "Coding For All People".rfind("l")
print(last_occurrence_l)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
first_occurrence_because = sentence.index(sub_string)
print(first_occurrence_because)

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
last_occurrence_because = sentence.rindex(sub_string)
print(last_occurrence_because)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
first_occurrence_because = sentence.index(sub_string)
last_occurrence_because = sentence.rindex(sub_string)
print(sentence[first_occurrence_because : (last_occurrence_because + len(sub_string))])

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
first_occurrence_because = sentence.find(sub_string)
print(first_occurrence_because)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
first_occurrence_because = sentence.index(sub_string)
last_occurrence_because = sentence.rindex(sub_string)
print(sentence[first_occurrence_because : (last_occurrence_because + len(sub_string))])

# Does 'Coding For All' start with a substring Coding?

sentence = "Coding For All"
sub_string = "Coding"

print(sentence.startswith(sub_string))  # True


# Does 'Coding For All' end with a substring coding?

sentence = "Coding For All"
sub_string = "coding"

print(sentence.endswith(sub_string))  # False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

sentence = "   Coding For All      "
sentence.strip(" ")

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

"30DaysOfPython".isidentifier()  # False
"thirty_days_of_python".isidentifier()  # True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]

print("# ".join(python_libraries))

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")


# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
pi = 3.14
area = pi * radius**2

print("radius = {}".format(radius))
print("area = {} * radius ** 2".format(pi))
print(
    "The area of a circle with radius {} is {:.0f} meters square.".format(radius, area)
)

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a**b))
