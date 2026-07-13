from bs4 import BeautifulSoup


with open("example.html", "r") as file:
    html = file.read()


soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()


word = input("Enter the word to search: ")


if word.lower() in text.lower():
    print("Word found.")
else:
    print("Word not found.")
