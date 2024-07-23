# Q1
age = 30

# Q2
height = 174.2

# Q3
complex_num = 5 + 7j

# Q4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print(f"The are of the triangle is {base * height / 2}")

# Q5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
print(f"The perimeter of the triangle is {side_a + side_b + side_c}")


# Q6
def rectangle_area(length, width) -> float:
    return length * width


def rectangle_perimeter(length, width) -> float:
    return (length + width) * 2


# Q7
def circle_area(radius) -> float:
    pi = 3.14
    return (radius**2) * pi


def circle_circumference(radius) -> float:
    pi = 3.14
    return (radius * 2) * pi


# Q8
x1 = 0
y1 = 2(x1) - 2

x2 = 10
y2 = 2(x2) - 2

slope_Q8 = (y2 - y1) / (x2 - x1)
print(slope_Q8)


# Q9
def slope_formula(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    try:
        slope = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError as e:
        raise e

    return slope


slope_Q9 = slope_formula((2, 2), (6, 10))
print(slope_Q9)


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    import math

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


print(euclidean_distance((2, 2), (6, 10)))


# Q10
def compare_slope(slope1, slope2):
    if slope1 > slope2:
        print("slope 1 is greater than slope 2")

    elif slope1 == slope2:
        print("slope 1 is equal to slope 2")

    else:
        print("slope 1 is less than slope 2")


compare_slope(slope_Q8, slope_Q9)

# Q11


def Q11(y):
    import math

    x = math.sqrt(y) - 3

    return x


print(Q11(y=0))

# Q12


def Q12(word1, word2):
    return not len(word1) == len(word2)


print(Q12("python", "dragon"))

# Q13


def Q13(word1, word2):
    return "on" in word1 and "on" in word2


print(Q13("python", "dragon"))

# Q14
print("jargon" in "I hope this course is not full of jargon.")

# Q15
print("on" not in "dragon" and "on" not in "python")


# Q16

text = "python"

text_to_float = float(len(text))
float_to_string = str(text_to_float)

print(text_to_float, float_to_string)

# Q17


def check_even_number(num):
    return num % 2 == 0


# Q18
print((7 // 3) == int(2.7))

# Q19
print(type(10) == type("10"))

# Q20
print(int("9.8") == 10)

# Q21
hours = int(input("hours: "))
rate_per_hour = int(input("rate per hour: "))
print(f"Your weekly earning is {hours * rate_per_hour}")

# Q22
years = int(input("number of years have lived: "))
print(f"You have lived for {years * 365 * 24 * 60 * 60} seconds.")

# Q23


def Q23(num):
    i = 1
    for _ in range(num):
        print(f"{i} {int(i / i)} {i} {i ** 2} {i ** 3}")
        i += 1


Q23(5)
