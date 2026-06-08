import requests, re
from bs4 import BeautifulSoup
from book import Book



def webSearch(path:str) -> list:
    url = "https://books.toscrape.com/catalogue/" + path
    headers = {
        'User-Agent' : 'Mozilla/5.0'
    }
    NumMap = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5,
    }

    response = requests.get(url = url, headers = headers)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    product = soup.find("article", class_ = "product_page")

    title = product.find("div", class_ = "product_main").h1.get_text(strip = True)

    descHeader = product.find("div", id = "product_description")
    if descHeader:
        description = descHeader.find_next_sibling("p").get_text(strip=True)
    else:
        description = ""
    
    rating_loc = product.find("p", class_ = "star-rating")
    rating = NumMap[rating_loc['class'][1]]

    table = product.find("table", class_ = "table")
    # for con in ['UPC', 'Product Type', 'Price (excl. tax)', 'Tax', 'Availability', 'Number of reviews']:
    
    UPC = table.find('th', string = 'UPC').find_next_sibling("td").get_text(strip=True)
    prodType = table.find('th', string = 'Product Type').find_next_sibling("td").get_text(strip=True)
    priceText = table.find('th', string = 'Price (excl. tax)').find_next_sibling("td").get_text(strip=True)
    price = float(priceText.replace("£", ""))

    taxText = table.find('th', string = 'Tax').find_next_sibling("td").get_text(strip=True)
    tax = float(taxText.replace("£", ""))

    return Book(title=title, description=description, prodType=prodType, rating=rating, UPC=UPC, price=price, tax=tax)

if __name__ == "__main__":
    print(webSearch("a-light-in-the-attic_1000/index.html"))


    