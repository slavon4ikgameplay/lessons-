lst = [12, 3, 4, 10, 8]

if lst:
    last_elem = lst.pop(-1)
    lst.insert(0,last_elem)

print(lst)
