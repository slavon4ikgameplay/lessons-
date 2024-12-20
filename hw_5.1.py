import string
import keyword

input_string = input("Enter string: ")

is_valid = True

#перевірка на пробіли
if " " in input_string:
    is_valid = False

#перевірка чи змінна є  ключовим словом
if input_string in keyword.kwlist:
    is_valid = False

#перевірка чи змінна починатися з цифри
if input_string[0].isdigit():
    is_valid = False

#перевіряє чи є великі літери
for char in input_string:
    if char.isupper():
        is_valid = False
        break

#перевіряє чи є знаки пунктуації окрім '_'
for char in input_string:
    if char in string.punctuation and char != "_":
        is_valid = False
        break

#перевіряє чи '_' стоїть більше ніж один раз підряд
if "__" in input_string:
    is_valid = False

print(is_valid)
