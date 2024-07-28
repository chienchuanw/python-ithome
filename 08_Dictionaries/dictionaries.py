# 1. Create an empty dictionary called dog

dog = dict()
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary

dog.update({"name": "Coco", "color": "brown", "breed": "Husky", "legs": 4, "age": 5})
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    "first_name": "John",
    "last_name": "Kelly",
    "gender": "male",
    "age": 20,
    "marital status": "single",
    "skills": ["boxing", "drawing", "cooking"],
    "country": "Taiwan",
    "city": "New Taipei City",
    "address": {"floor": 5, "number": 16, "road": "Rd. Xinyi"},
}

print(student)

# 4. Get the length of the student dictionary

print(len(student))

# 5. Get the value of skills and check the data type, it should be a list

print(type(student["skills"]))

# 6. Modify the skills values by adding one or two skills

student["skills"].extend(["dancing", "hiking"])
print(student["skills"])

# 7. Get the dictionary keys as a list

student_keys = list(student.keys())
print(student_keys)

# 8. Get the dictionary values as a list

student_values = list(student.values())
print(student_values)

# 9. Change the dictionary to a list of tuples using _items()_ method

student_tuples = list(student.items())
print(student_tuples)

# 10. Delete one of the items in the dictionary

del student["age"]
del student["address"]
print(student)

# 11. Delete one of the dictionaries

del student
