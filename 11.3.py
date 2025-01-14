def is_even(number):
    numb_to_str = str(number)
    for i in range(0 , 10 , 2):
        if numb_to_str[-1] == str(i):
            return True
    return False


print(is_even(1056897**2))
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
