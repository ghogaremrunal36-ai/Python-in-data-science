import requests
from bs4 import BeautifulSoup


print(" Mrunal Ghogare, S084")

url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("\nPAGE TITLE:")

if soup.title:
    print(soup.title.get_text(strip=True))
else:
    print("Title not found")

print("\nFIRST 3 PARAGRAPHS:")

paragraphs = soup.find_all("p")

for i, paragraph in enumerate(paragraphs[:3], start=1):
    print(f"Paragraph {i}:")
    print(paragraph.get_text(" ", strip=True))

print("\nIMAGE SRC URLs:")

images = soup.find_all("img")

for i, image in enumerate(images, start=1):
    src = image.get("src")

    if src:
        print(f"Image {i}: {src}")

print("\nTOTAL NUMBER OF LINKS:")

links = soup.find_all("a")

print(len(links))

print("\nHEADINGS:")

headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.get_text(" ", strip=True))

print("\nLANGUAGE NAMES:")

language_boxes = soup.find_all("a", class_="link-box")

for language in language_boxes:
    name = language.find("strong")

    if name:
        print(name.get_text(" ", strip=True))
