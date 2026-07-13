from bs4 import BeautifulSoup


with open("sample.html", "r") as file:
    content = file.read()


soup = BeautifulSoup(content, "html.parser")


print(soup.get_text())
