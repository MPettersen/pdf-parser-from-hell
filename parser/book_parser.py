from uuid import UUID

from models import (
    Book,
    Chapter,
    Paragraphs,
    List,
    Table
)


def parse_book(title: str) -> Book:
    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    return Book(title=title)


def parse_chapter(title: str, parent_id: UUID, book_id: UUID, page: int) -> Chapter:
    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    if not isinstance(parent_id, UUID):
        raise TypeError("Parent ID must be a UUID")
    if not isinstance(book_id, UUID):
        raise TypeError("Book ID must be a UUID")
    if not isinstance(page, int):
        raise TypeError("Page must be an integer")
    return Chapter(
        title=title,
        parent_id=parent_id,
        book_id=book_id,
        page=page
    )
