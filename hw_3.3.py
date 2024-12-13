lst = [1 , 2 , 3 , 4 , 5 , 6]
new_lst = []

if len(lst) == 0: # якщо список порожній
    part1 = []
    part2 = []
    new_lst.append(part1)
    new_lst.append(part2)
    print(new_lst)

elif len(lst) % 2 == 0: # якщо список має парну кількість елементів
    part1 = lst[0 : len(lst) // 2]
    part2 = lst[len(lst) // 2 : len(lst)]
    new_lst.append(part1)
    new_lst.append(part2)
    print(new_lst)

elif len(lst) % 2 != 0: # якщо список має непарну кількість елементів
    part1 = lst[0 : len(lst) // 2 + 1] # тут беремо len(lst)// 2 + 1 щоб в першому списку було більше елементів ніж в другому
    part2 = lst[len(lst) // 2 + 1 : len(lst)]
    new_lst.append(part1)
    new_lst.append(part2)
    print(new_lst)

