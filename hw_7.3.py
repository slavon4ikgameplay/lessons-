def second_index(text: str, some_str: str) -> int or None:
    first_index = text.find(some_str)
    if first_index == -1:
        return None

    sec_index = text.find(some_str, first_index + 1)
    if sec_index == -1:
        return None

    return sec_index


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
