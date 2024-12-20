while True:
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
#Змінна яка відповідає за вибір користувачем математичної операції
    operation_choice = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nSelect your choice:")) # 1 - додавання 2 - віднімання 3 - множення 4 - ділення

    match operation_choice:
        case 1:
            print(first_number+second_number)
        case 2:
            choice_1 = int(input("1.Subtract the first number from the second\n2.Subtract the second number from the first\nSelect your choice:")) # вибираємо віднімати перше число від другого, чи друге від першого
            if choice_1 == 1:
                print(second_number - first_number)
            else:
                print(first_number - second_number)
        case 3:
            print(first_number*second_number)
        case 4:
            choice_2 = int(input("1.Divide the first number by the second\n2.Divide the second number by the first\nSelect your choice:")) # вибираємо ділити перше число на друге , чи друге на перше
            if choice_2 == 1:
                if second_number != 0 :
                    print(first_number/second_number)
                else:
                    print("You can't divide by zero.")# якщо друге число == 0, то при діленні першого на друге буде повідомлення
            elif choice_2 == 2:
                if first_number != 0:
                    print(second_number / first_number)
                else:
                    print("You can't divide by zero.")# якщо перше число == 0, то при діленні другого на перше буде повідомлення

    want_next = input("Enter 'y' if you want to continue or anything to end: ")
    if want_next == 'y':
        print("Continue...")
    else:
        print("End...")
        break