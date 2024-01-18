def count_words(sentence):
    words = sentence.split()
    return len(words)

user_input = input("Enter a sentence: ")
result = count_words(user_input)
print("Number of words:", result)
