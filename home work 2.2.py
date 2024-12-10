your_number = int(input("Enter your number: "))

first_numb = your_number // 10000
second_numb = your_number // 1000 % 10
third_numb = your_number // 100 % 10
fourth_numb = your_number // 10 % 10
fifth_numb =  your_number % 10

revert_number = fifth_numb * 10000 + fourth_numb * 1000 + third_numb * 100 + second_numb * 10 + first_numb
print(revert_number)