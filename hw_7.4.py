def common_elements():
    first_set = {number for number in range(100) if number % 3 == 0}
    second_set = {elem for elem in range(100) if elem % 5 == 0}
    my_set = first_set.intersection(second_set)
    return my_set



print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
