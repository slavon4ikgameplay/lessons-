import random
lst = []
for i in range(random.randint(3 , 11)): # генерує кількість елементів списку у діапазоні від 3 до 10 включно
     lst.append(random.randint(0 , 10)) # заповнює список числами від 0 до 10
print(lst)
new_lst = [lst[0] , lst[2] , lst[-2]]
print(new_lst)



