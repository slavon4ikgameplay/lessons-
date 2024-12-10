your_number = int(input("Enter your number: "))
first_numb = your_number // 1000
second_numb = your_number // 100 % 10
third_numb = your_number // 10 % 10
fourth_numb = your_number % 10

print(first_numb , second_numb , third_numb , fourth_numb , sep = "\n")

