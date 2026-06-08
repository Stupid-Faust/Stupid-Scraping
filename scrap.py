import requests, time
from bs4 import BeautifulSoup
from website import webSearch
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-"

headers = {
    'User-Agent' : 'Mozilla/5.0'
}

contents = []

for i in range(1, 4):
    soup = BeautifulSoup(requests.get(url + str(i) + ".html", headers = headers).text, "html.parser")
    for book in soup.find_all("article", class_ = "product_pod"):
        path = book.h3.a['href']
        result = webSearch(path)
        print(result)
        contents.append(result)
        time.sleep(1)
        
# pd.DataFrame(contents).to_csv("books.csv", index=False)
