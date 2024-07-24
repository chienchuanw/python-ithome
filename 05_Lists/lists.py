# 1. Declare an empty list

empty_list = list()

# 2. Declare a list with more than 5 items

five_items = ["a", "b", "c", "d", "e"]
print(five_items)

# 3. Find the length of your list

list_three = ["a", "b", "c", "d", "e"]
print(len(list_three))

# 4. Get the first item, the middle item and the last item of the list

list_four = ["a", "b", "c", "d", "e"]
print(list_four[0], list_four[int(len(list_four) / 2)], list_four[-1])


# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Wang", 30, 174.5, {"Single": True}, "New Taipei City"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 8. Print the number of companies in the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(len(it_companies))

# 9. Print the first, middle and last company

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[0], it_companies[int(len(it_companies) / 2)], it_companies[-1])

# 10. Print the list after modifying one of the companies

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[4] = "MSI"
print(it_companies)

# 11. Add an IT company to it_companies

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("ASUS")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(int(len(it_companies) / 2), "Acer")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("#;  ".join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("MSI" in it_companies)

# 16. Sort the list using sort() method

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse=True)
print(it_companies)

# 18. Slice out the first 3 companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[int(len(it_companies) / 2) : int(len(it_companies) / 2) + 1])

# 21. Remove the first IT company from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove(it_companies[0])
print(it_companies)

# alternative answer
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove(it_companies[int(len(it_companies) / 2)])
print(it_companies)

# 23. Remove the last IT company from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove(it_companies[-1])
print(it_companies)

# 24. Remove all IT companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies

# 26. Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

new_list = front_end + back_end

print(new_list)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = new_list.copy()
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

# 28. The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age

min_age = sorted(ages)[0]
max_age = sorted(ages)[-1]

print(min_age, max_age)

# - Add the min age and the max age again to the list

ages.append(min_age)
ages.append(max_age)
print(ages)

# - Find the median age (one middle item or two middle items divided by two)


def find_median_age(age_list):
    if len(age_list) % 2 == 0:
        return (
            sorted(age_list)[int(len(age_list) / 2)]
            + sorted(age_list)[(int(len(age_list) / 2)) - 1]
        ) / 2

    else:
        return sorted(age_list)[int(len(age_list) / 2)]


median_age = find_median_age(ages)
print(median_age)

# - Find the average age (sum of all items divided by their number )

average_age = sum(ages) / len(ages)
print(average_age)

# - Find the range of the ages (max minus min)

print(max_age - min_age)

# - Compare the value of (min - average) and (max - average), use _abs()_ method

if abs(min_age - average_age) > abs(max_age - average_age):
    print("min_age wins!")

elif abs(min_age - average_age) == abs(max_age - average_age):
    print("it's a tie!")

else:
    print("max_age wins!")

# 29. Find the middle country(ies) in the countries list
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombi",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor Timur)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia, The",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia and Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

print(countries[int(len(countries) / 2)])
# 30. Divide the countries list into two equal lists if it is even if not one more country for the first half.

first_half, second_half = (
    countries[: int(len(countries) / 2)],
    countries[int(len(countries) / 2) :],
)
print(first_half)
print(second_half)

# 31. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

first, second, third, *scandic = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark",
]
print(first, second, third, scandic)
