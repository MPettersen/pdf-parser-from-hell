from uuid import UUID

from models import Book
from parser.book_parser import parse_book


def test_book_parser():
    title = "Test Book"
    test_book = parse_book(title=title)
    assert test_book.title == title
    assert isinstance(test_book.id, UUID)
