def count_words(sentence):
    words = sentence.split()
    return len(words)
input_sentence = input("Enter a sentence: ")
word_count = count_words(input_sentence)
print(f"The number of words in the sentence is: {word_count}")
