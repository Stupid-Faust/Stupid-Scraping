import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

headers = {
    'User-Agent' : 'Mozilla/5.0'
}

response = requests.get(url, headers = headers)

print(response.text)
