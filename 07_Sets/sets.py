it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies

print(len(it_companies))

# 2. Add 'Twitter' to it_companies

it_companies.add("Twitter")

# 3. Insert multiple IT companies at once to the set it_companies

new_it_companies = {"MSI", "ASUS", "Acer"}
it_companies.update(new_it_companies)

# 4. Remove one of the companies from the set it_companies

it_companies.remove("MSI")

# 5. What is the difference between remove and discard

print(
    "The difference between remove and discard is remove will raise an error if there no delete item found in the set. On the other hand, discard will just be silent."
)

# 6. Join A and B

join_set = A.union(B)
print(join_set)

# 7. Find A intersection B

intersect_join = A.intersection(B)
print(intersect_join)

# 8. Is A subset of B

print(A.issubset(B))

# 9. Are A and B disjoint sets

print(A.isdisjoint(B))

# 10. Join A with B and B with A

A.update(B)
print(A)
B.update(A)
print(B)

# 11. What is the symmetric difference between A and B

sym_diff = A.symmetric_difference(B)
print(sym_diff)

# 12. Delete the sets completely

del A, B

# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)

if len(age_set) > len(age):
    print("age_set is bigger.")
elif len(age_set) == len(age):
    print("two length are the same")
else:
    print("age is bigger")


# 14. Explain the difference between the following data types: string, list, tuple and set

print("A string is ordered and immutable.")
print("A list is ordered and mutable.")
print("A tuple is ordered and immutable.")
print("A set is unordered and mutable.")

# 15. `I am a teacher and I love to inspire and teach people`. How many unique words have been used in the sentence? Use the `split` methods and set to get the unique words.

words = "I am a teacher and I love to inspire and teach people"
print(len(set(words.split())))
