def correct_sentence(text: str):
    sentences = text.split(". ")
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    result = ". ".join(capitalized_sentences)
    if result[-1] != ".":
        result = result + "."
    return(result)



assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
