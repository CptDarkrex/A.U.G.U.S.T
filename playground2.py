def extract_second_string(sentence):
    # Split the sentence into words using the split() method
    words = sentence.split()
    # Get the second word in the list of words', '
    second_word = words[1]
    return second_word


word = extract_second_string("hello there")
print(word)
