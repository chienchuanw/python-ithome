# # 1. Read this url and find the 10 most frequent words. `romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'`
# import requests
# from collections import Counter

# # API
# romeo_and_juliet = "https://www.gutenberg.org/files/1112/1112-0.txt"

# # Get text and convert string to a list
# response = requests.get(romeo_and_juliet)
# text = response.text
# text_list = text.split()

# # Use counter to count the frequency of words and filter top 10
# word_count = Counter(text_list)
# top_10_words = [word for word, _ in word_count.most_common(10)]
# print(top_10_words)


# 2. Read the cats API and `cats_api = 'https://api.thecatapi.com/v1/breeds'` and find :
#     - the min, max, mean, median, standard deviation of cats' weight in metric units.
#     - the min, max, mean, median, standard deviation of cats' lifespan in years.
#     - Create a frequency table of country and breed of cats

import requests

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
cats = response.json()

for cat in cats:
    print(cat["weight"])
