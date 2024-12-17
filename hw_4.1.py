lst = [0, 1, 0, 12, 3]
print(lst)

new_lst = []
count_of_zeros = 0
'''Переміщуємо всі не нульові елементи в окремий список
    і окремо рахуємо кількість нулів в початкову списку
    потім просто додаємо ті нулі в кінець списку'''
for elem in range(len(lst)):
    if lst[elem] != 0 :
        new_lst.append(lst[elem])
    else:
        count_of_zeros += 1
print(f"Count of zeros in list: {count_of_zeros}")
print(new_lst + [0] * count_of_zeros)