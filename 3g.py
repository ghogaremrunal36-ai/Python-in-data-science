
file = open("sample.txt", "r")


text = file.read()
file.close()


word = input("Enter the word to search: ")


if word.lower() in text.lower():
    print("Word found.")
else:
    print("Word not found.")
