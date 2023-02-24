import pandas as pd

from uuid import uuid4, UUID
from joblib import dump, load
from models import (
    Item,
    Book,
    Chapter,
    Paragraphs,
    Heading,
    List,
    InfoBox,
    Table,
    Attribute,
    SpecialLimitation,
    Advantage,
    Perk,
    Enhancement,
    Limitation
)
from parsers import (
    parse_paragraphs,
    parse_list,
    parse_table
)


def save_df(df: pd.DataFrame, title: str):
    dump(df, f"books/{title}.joblib")


def load_items(title: str) -> pd.DataFrame:
    df = load(f"books/{title}.joblib")
    return df.apply(lambda x: Item(**x), axis=1).to_list()


def elevate_parent(items: list[Item], parent_id: UUID) -> Item:
    for item in items:
        if item.id == parent_id:
            return item.parent_id


def get_parent_type(items: list[Item], parent_id: UUID) -> str:
    for item in items:
        if item.id == parent_id:
            return item.type


def add_item(
    items: list[Item],
    parent_id: UUID,
    type_: str,
    metadata: dict
) -> Item:
    item = Item(
        parent_id=parent_id,
        type=type_,
        metadata=metadata
    )
    items.append(item)
    return item


def new_book(title: str, items: list[Item]) -> tuple[Item, UUID, UUID]:
    meta = Book(title=title)
    id_ = uuid4()
    item = Item(
        id=id_,
        parent_id=id_,
        type="book",
        metadata=meta.dict()
    )
    items.append(item)
    return item, item.id, item.id


def add_chapter(
    title: str,
    page: int,
    items: list[Item],
    parent_id: UUID
) -> tuple[Item, UUID]:
    meta = Chapter(title=title, page=page)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="chapter",
        metadata=meta.dict()
    )


def add_paragraphs(
    text: list[str],
    items: list[Item],
    parent_id: UUID
) -> Item:
    content = parse_paragraphs(text)
    meta = Paragraphs(content=content, page=-1)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="paragraphs",
        metadata=meta.dict()
    )


def add_heading(
    title: str,
    items: list[Item],
    parent_id: UUID,
    page: int = -1
) -> Item:
    meta = Heading(title=title, page=page)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="heading",
        metadata=meta.dict()
    )


def add_list(
    text: list[str],
    items: list[Item],
    parent_id: UUID,
    title: str = None,
    page: int = -1
) -> Item:
    content = parse_list(text)
    meta = List(title=title, content=content, page=page)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="list",
        metadata=meta.dict()
    )


def add_infobox(
    title: str,
    items: list[Item],
    parent_id: UUID,
    page: int = -1
) -> Item:
    meta = InfoBox(title=title, page=page)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="infobox",
        metadata=meta.dict()
    )


def add_table(
    text: dict,
    items: list[Item],
    parent_id: UUID,
    title: str = None,
    metadata: list[list[str]] = None,
    page: int = -1,
    **kwargs
) -> Item:
    content = parse_table(text, **kwargs).to_dict()
    meta = Table(
        title=title,
        page=page,
        content=content,
        metadata=metadata)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="table",
        metadata=meta.dict()
    )


def add_attribute(
    text: str,
    cost: str,
    items: list[Item],
    parent_id: UUID,
    page: int = -1
) -> Item:
    meta = Attribute(title=text, cost=cost, page=page)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="attribute",
        metadata=meta.dict()
    )


def add_special_limitation(
    text: str,
    items: list[Item],
    parent_id: UUID,
    cost: str = '',
    page: int = -1
) -> Item:
    meta = SpecialLimitation(title=text, page=page, cost=cost)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="special_limitation",
        metadata=meta.dict()
    )


def add_advantage(
    text: str,
    items: list[Item],
    parent_id: UUID,
    cost: str = '',
    types: list[str] = None,
    page: int = -1
) -> Item:
    meta = Advantage(title=text, page=page, cost=cost, types=types)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="advantage",
        metadata=meta.dict()
    )

def add_perk(
    text: str,
    items: list[Item],
    parent_id: UUID,
    types: list[str] = None,
    page: int = -1
) -> Item:
    meta = Perk(title=text, page=page, types=types)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="perk",
        metadata=meta.dict()
    )


def add_enhancement(
    text: str,
    items: list[Item],
    parent_id: UUID,
    cost: str = '',
    types: list[str] = None,
    page: int = -1
) -> Item:
    meta = Enhancement(title=text, page=page, cost=cost, types=types)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="enhancement",
        metadata=meta.dict()
    )


def add_limitation(
    text: str,
    items: list[Item],
    parent_id: UUID,
    cost: str = '',
    types: list[str] = None,
    page: int = -1
) -> Item:
    meta = Limitation(title=text, page=page, cost=cost, types=types)
    return add_item(
        items=items,
        parent_id=parent_id,
        type_="limitation",
        metadata=meta.dict()
    )
