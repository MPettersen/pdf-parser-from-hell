from uuid import UUID, uuid4

from tests.test_values import (
    t1,
    t2
)
from parsers import (
    parse_paragraphs
)
from models import (
    Book,
    Chapter,
    Paragraphs,
    List,
    Table,
    Heading,
    InfoBox
)


def test_book_title():
    title = "Test Book"
    test_book = Book(title=title)
    assert test_book.title == title
    assert isinstance(test_book.id, UUID)


def test_chapter():
    title = "Test Chapter"
    uuid = uuid4()
    kwargs = {
        "parent_id": uuid,
        "book_id": uuid,
    }
    test_chapter = Chapter(
        title=title,
        page=1,
        **kwargs
    )
    assert test_chapter.title == title
    assert test_chapter.page == 1
    assert isinstance(test_chapter.id, UUID)
    assert (
        isinstance(test_chapter.parent_id, UUID)
        and test_chapter.parent_id == uuid
    )
    assert (
        isinstance(test_chapter.book_id, UUID)
        and test_chapter.book_id == uuid
    )


def test_parse_paragraphs():
    p1 = parse_paragraphs(t1)
    p2 = parse_paragraphs(t2)
    a1 = ["Testing is this works it should work"]
    a2 = [
        "This is another test it should also work.",
        "So let us see",
    ]
    assert p1 == a1
    assert p2 == a2


def test_paragraphs():
    p1 = parse_paragraphs(t1)
    p2 = parse_paragraphs(t2)

    uuid = uuid4()
    kwargs = {
        "parent_id": uuid,
        "book_id": uuid,
        "chapter_id": uuid,
        "page": 1
    }
    test_paragraphs_1 = Paragraphs(
        content=p1,
        **kwargs
    )
    test_paragraphs_2 = Paragraphs(
        content=p2,
        **kwargs
    )

    assert test_paragraphs_1.content == p1
    assert test_paragraphs_2.content == p2
    assert test_paragraphs_1.page == 1
    assert test_paragraphs_2.page == 1
    assert isinstance(test_paragraphs_1.id, UUID)
    assert isinstance(test_paragraphs_2.id, UUID)
    assert (
        isinstance(test_paragraphs_1.book_id, UUID)
        and test_paragraphs_1.book_id == uuid
    )
    assert (
        isinstance(test_paragraphs_1.chapter_id, UUID)
        and test_paragraphs_1.chapter_id == uuid
    )
    assert (
        isinstance(test_paragraphs_2.book_id, UUID)
        and test_paragraphs_2.book_id == uuid
    )
    assert (
        isinstance(test_paragraphs_2.chapter_id, UUID)
        and test_paragraphs_2.chapter_id == uuid
    )


def test_heading():
    title = "Test Heading"
    uuid = uuid4()
    kwargs = {
        "parent_id": uuid,
        "book_id": uuid,
        "chapter_id": uuid,
    }
    test_chapter = Heading(
        title=title,
        page=1,
        **kwargs
    )
    assert test_chapter.title == title
    assert test_chapter.page == 1
    assert isinstance(test_chapter.id, UUID)
    assert (
        isinstance(test_chapter.parent_id, UUID)
        and test_chapter.parent_id == uuid
    )
    assert (
        isinstance(test_chapter.book_id, UUID)
        and test_chapter.book_id == uuid
    )


def test_infobox():
    title = "Test Info Box"
    uuid = uuid4()
    kwargs = {
        "parent_id": uuid,
        "book_id": uuid,
        "chapter_id": uuid,
    }
    test_chapter = InfoBox(
        title=title,
        page=1,
        **kwargs
    )
    assert test_chapter.title == title
    assert test_chapter.page == 1
    assert isinstance(test_chapter.id, UUID)
    assert (
        isinstance(test_chapter.parent_id, UUID)
        and test_chapter.parent_id == uuid
    )
    assert (
        isinstance(test_chapter.book_id, UUID)
        and test_chapter.book_id == uuid
    )
