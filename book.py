from dataclasses import dataclass

@dataclass
class Book:
    title: str
    description: str
    prodType: str
    rating: int
    UPC: str
    price: float
    tax: float
