import pandas as pd

from uuid import UUID, uuid4
from pydantic import BaseModel, Field

from models.base import ChapterItem


class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    children: list[UUID] = Field(default_factory=list)


class Chapter(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    parent_id: UUID
    book_id: UUID
    page: int
    title: str
    children: list[UUID]


class Paragraphs(ChapterItem):
    content: list[str]


class List(ChapterItem):
    title: str = None
    type: str = None
    content: list[str | dict[str, str]]


class Table(ChapterItem):
    title: str = None
    type: str = None
    metadata: dict[str, str]
    content: pd.DataFrame


class InfoBox(ChapterItem):
    title: str
    children: list[UUID]


class Headings(ChapterItem):
    title: str
    children: list[UUID]
