import requests
from bs4 import BeautifulSoup


url = "https://www.facebook.com/"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)


soup = BeautifulSoup(response.text, "html.parser")


print("Page Title:", soup.title.get_text(strip=True))


for link in soup.find_all("a", href=True)[:5]:

    link_text = link.get_text(strip=True)
    link_url = link["href"]

   
    if link_url == "#":
        link_url = "https://www.facebook.com/"


    elif link_url.startswith("/"):
        link_url = "https://www.facebook.com" + link_url

    print("Link Text:", link_text, "| URL:", link_url)
print("Mrunal ghogare, S084")
