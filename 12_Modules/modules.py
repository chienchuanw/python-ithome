# 初階題
# 1. Writ a function which generates a six digit/character `random_user_id`.

#    ```py
#      print(random_user_id())
#      '1ee33d'
#    ```

from string import digits, ascii_lowercase, ascii_letters
from random import choices


def random_user_id() -> str:
    option = []
    for digit in digits:
        option.append(digit)

    for letter in ascii_lowercase:
        option.append(letter)

    result = choices(option, k=6)

    return "".join(result)


# better solution
def random_user_id() -> str:
    option = digits + ascii_lowercase
    return "".join(choices(option, k=6))


# 2. Modify the previous task. Declare a function named `user_id_gen_by_user`. It doesn’t take any parameters but it takes two inputs using `input()`. One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

#     ```py
#     print(user_id_gen_by_user()) # user input: 5 5
#     #output:
#     #kcsy2
#     #SMFYb
#     #bWmeq
#     #ZXOYh
#     #2Rgxf

#     print(user_id_gen_by_user()) # 16 5
#     #1GCSgPLMaBAVQZ26
#     #YD7eFwNQKNs7qXaT
#     #ycArC5yrRupyG00S
#     #UbGxOFI7UXSWAyKN
#     #dIV0SSUTgAdKwStr
#     ```


def user_id_gen_by_user() -> str:
    char_length = int(input("The number of characters: "))
    id_nums = int(input("The number of IDs: "))

    option = []
    for digit in digits:
        option.append(digit)

    for letter in ascii_letters:
        option.append(letter)

    result = []

    for _ in range(id_nums):
        id = "".join(choices(option, k=char_length))
        result.append(id)

    return "\n".join(result)


# better solution
from string import digits, ascii_letters
from random import choices


def user_id_gen_by_user() -> str:
    char_length = int(input("The number of characters: "))
    id_nums = int(input("The number of IDs: "))

    option = digits + ascii_letters
    result = ["".join(choices(option, k=char_length)) for _ in range(id_nums)]

    return "\n".join(result)


# 3. Write a function named `rgb_color_gen`. It will generate rgb colors (3 values ranging from 0 to 255 each).

# ```py
# print(rgb_color_gen())
# # rgb(125, 244, 255) - the output should be in this form
# ```

from random import randint


def rgb_color_gen() -> str:
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return f"rgb({red}, {green}, {blue})"


# 進階題
# 1. Write a function `list_of_hex_colors` which returns any number of hexadecimal colors in a list (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

from string import hexdigits
from random import randint, choices


def list_of_hex_colors(num) -> list:
    hex_numbers = hexdigits[:-6]

    hex_colors = list()

    for _ in range(num):
        hex_color = "#" + "".join(choices(hex_numbers, k=6))
        hex_colors.append(hex_color)

    return hex_colors


# better solution
from random import choices
from string import hexdigits


def list_of_hex_colors(num) -> list:
    hex_numbers = hexdigits[:-6]
    hex_colors = ["#" + "".join(choices(hex_numbers, k=6)) for _ in range(num)]

    return hex_colors


# 2. Write a function `list_of_rgb_colors` which returns any number of RGB colors in a list.


def list_of_rgb_colors(num) -> list:

    rgb_colors = []

    for _ in range(num):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        rgb_colors.append(f"rgb({red}, {green}, {blue})")

    return rgb_colors


# 3. Write a function `generate_colors` which can generate any number of hex or rgb colors.

#     ```py
#     generate_colors('hex', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#     generate_colors('hex', 1) # ['#b334ef']
#     generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#     generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
#     ```


def generate_colors(option: str, num: int) -> list:
    match option:
        case "hex":
            return list_of_hex_colors(num)
        case "rgb":
            return list_of_rgb_colors(num)


# 高階題
# 1. Call your function `shuffle_list`, it takes a list as a parameter and it returns a shuffled list.

from random import choice


def shuffle_list(input_list: list) -> list:

    output_list = []
    counter = len(input_list)
    while counter > 0:
        item = choice(input_list)
        output_list.append(item)
        input_list.remove(item)
        counter -= 1

    return output_list


# better solution
from random import shuffle


def shuffle_list(input_list: list) -> list:
    shuffle(input_list)
    return input_list


# 2. Write a function which returns a list of seven random numbers in a range of 0-9. All the numbers must be unique.

from random import randrange


def seven_random_numbers() -> list:

    output_list = list(range(10))

    while len(output_list) > 7:
        output_list.pop(randrange(0, len(output_list)))

    return shuffle_list(output_list)


# better solution

from random import sample


def seven_random_numbers() -> list:
    return sample(range(10), 7)
