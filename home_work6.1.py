import string
from string import ascii_letters

your_range = input("Enter the range in which to display the letters in format 'a-b': ")

first_letter = your_range[0]
second_letter = your_range[2]

first_letter_index = string.ascii_letters.index(first_letter)
second_letter_index = string.ascii_letters.index(second_letter)


print("".join(string.ascii_letters[first_letter_index:second_letter_index+1]))
