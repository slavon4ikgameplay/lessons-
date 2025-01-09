def popular_words(text: str, words: list):
    word_list = text.lower().split()
    result = {word: word_list.count(word) for word in words}

    return result



print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''' , ['i', 'was', 'three', 'near']))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
