lst = [5 , 2 , 3 , 4 , 5 , 1 , 2 , 3 , 2]

suma = 0

if lst:  # перевірка чи список пустий
    ''' цикл проходить по всіх індексах і якщо вони 
    діляться на 2 націло то додаємо його до загальної суми'''
    for index in range(len(lst)):
        if index % 2 == 0 :
            suma += lst[index]
    res = suma * lst[-1]
else:
    res = 0

print(res)
