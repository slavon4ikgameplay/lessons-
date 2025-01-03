import string
def is_palindrome(text):
    new_text = ""
    for symbol in range(len(text)):
        if text[symbol] not in string.punctuation and text[symbol] != " ":
            new_text += text[symbol]
    return new_text.lower() == new_text.lower()[::-1]




assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")



