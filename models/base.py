from __future__ import annotations

from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class ChapterItem(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    parent_id: UUID
    book_id: UUID
    chapter_id: UUID
    page: int

    class Config:
        arbitrary_types_allowed = True


class TitleChildrenItem(ChapterItem):
    title: str
    children: list[UUID] = Field(default_factory=list)


class TitleChildrenCostItem(TitleChildrenItem):
    cost: str | dict[str, str] | list[str]


class TitleChildrenTypesItem(TitleChildrenItem):
    types: list[str]


class TitleChildrenCostTypesItem(TitleChildrenItem):
    cost: str | dict[str, str] | list[str]
    types: list[str]
