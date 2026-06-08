import sqlite3
from book import Book

if __name__ == "__main__":
    db = sqlite3.connect("books.db")
    cur = db.cursor()

    UPC = input("What is the UPC of the book you're looking for?")
    cur.execute("SELECT * FROM books WHERE upc = ?", (UPC,))
    book = cur.fetchone()

    print(f"Title: {book[1]}, Price: {book[4]} Euro, Rating: {book[3]};")
    print(f"Description: {book[2]}")
