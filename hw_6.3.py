number = int(input("Enter number: "))

while number >9 :
    product= 1
    copy_of_number = number

    while copy_of_number != 0 :
        digit = copy_of_number % 10
        product *= digit
        copy_of_number //= 10


    number = product

print(number)

