from models import Book


def parse_book(title: str) -> Book:
    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    return Book(title=title)
