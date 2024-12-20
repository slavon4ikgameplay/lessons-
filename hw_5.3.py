import string
input_string = input("Enter string: ")


clean_string = ""

for char in input_string:
    if char not in string.punctuation:
        clean_string += char

words = clean_string.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.title())

hashtag_string = "#" + "".join(capitalized_words)

if len(hashtag_string) > 140:
    hashtag_string = hashtag_string[:140]

print(hashtag_string)
