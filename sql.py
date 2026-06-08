import sqlite3
from book import Book

def createTable():
    db = sqlite3.connect("books.db")
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        upc TEXT PRIMARY KEY,
        title TEXT,
        description TEXT,
        prod_type TEXT,
        rating INTEGER,
        price REAL,
        tax REAL
    )                        
    """)

    db.commit()
    db.close()

def massInsert(books: list[Book]):
    for book in books:
        insertBook(book)


def insertBook(book: Book):
    db = sqlite3.connect("books.db")
    cur = db.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO books 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        book.UPC,
        book.title,
        book.description,
        book.prodType,
        book.rating,
        book.price,
        book.tax,
    ))
    
    db.commit()
    db.close()


