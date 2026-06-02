import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

headers = {
    'User-Agent' : 'Mozilla/5.0'
}

soup = BeautifulSoup(requests.get(url, headers = headers).text, "html.parser")
books = soup.find_all("article", class_ = "product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_ = "price_color").get_text(strip = True)

    print(title, price)


