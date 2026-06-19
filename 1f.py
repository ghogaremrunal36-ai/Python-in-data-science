sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
char_count = len(sentence)

print("Number of words:", word_count)
print("Number of characters:", char_count)

print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())

print("With underscores:", sentence.replace(" ", "_"))
