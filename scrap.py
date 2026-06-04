import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-"

headers = {
    'User-Agent' : 'Mozilla/5.0'
}
ratingMap = {
    'One' : 1,
    'Two' : 2,
    'Three' : 3,
    'Four' : 4,
    'Five' : 5
}

contents = []
titles = []
prices = []
ratings = []

for i in range(1, 21):
    soup = BeautifulSoup(requests.get(url + str(i) + ".html", headers = headers).text, "html.parser")
    books = soup.find_all("article", class_ = "product_pod")
    

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_ = "price_color").get_text(strip = True)
        classes = book.find("p", class_ = "star-rating")
        rating = classes['class'][1]
        ratingNum = ratingMap[rating]

        contents.append({'title' : title, 'price' : price, 'rating' : ratingNum})
        titles.append(title)
        prices.append(price)
        ratings.append(rating)

    
print(*contents, sep="\n")
