import requests, time
from bs4 import BeautifulSoup
from website import webSearch
from sql import insertBook, createTable
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-"

headers = {
    'User-Agent' : 'Mozilla/5.0'
}
createTable()

for i in range(1, 2):
    soup = BeautifulSoup(requests.get(url + str(i) + ".html", headers = headers).text, "html.parser")
    for book in soup.find_all("article", class_ = "product_pod"):
        path = book.h3.a['href']
        result = webSearch(path)
        print(result)
        insertBook(result)
        time.sleep(1)
        

