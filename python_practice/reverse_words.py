def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
input_sentence = input("Enter a sentence: ")
result = reverse_words_in_sentence(input_sentence)
print(f"Sentence after reversing words: '{result}'")
