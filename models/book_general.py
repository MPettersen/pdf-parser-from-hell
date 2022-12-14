from models.base import TitleChildrenItem as Chapter
from models.base import TitleChildrenItem as InfoBox
from models.base import TitleChildrenItem as Heading


Chapter.__doc__ = """
A chapter object.

Args:
    id (UUID): The ID of the chapter. Defaults to an autogenerated UUID.
    parent_id (UUID): The ID of the parent chapter.
    page (int): The page number of the chapter.
    title (str): The title of the chapter.
    children (list[UUID]): The list of children IDs. Defaults to [].

Examples:
    >>> from uuid import uuid4
    >>> chapter = Chapter(
    >>>     parent_id=uuid4(),
    >>>     title="Chapter 1",
    >>>     page=1,
    >>> )
    >>> chapter
    Chapter(
        id=UUID('c0a8b2b0-8b1a-4b1a-9b1a-8b1a8b1a8b1a'),
        parent_id=UUID('c0a8b2b0-8b1a-4b1a-9b1a-8b1a8b1a8b1a'),
        page=1,
        title='Chapter 1',
        children=[]
    )
"""


InfoBox.__doc__ = """
An info box object.

Args:
    id (UUID): The ID of the info box. Defaults to an autogenerated UUID.
    parent_id (UUID): The ID of the parent chapter.
    page (int): The page number of the chapter.
    title (str): The title of the info box.
    children (list[UUID]): The list of children IDs. Defaults to [].

Examples:
    >>> from uuid import uuid4
    >>> info_box = InfoBox(
    >>>     parent_id=uuid4(),
    >>>     title="Info Box",
    >>>     page=1,
    >>> )
    >>> info_box
    InfoBox(
        id=UUID('c0a8b2b0-8b1a-4b1a-9b1a-8b1a8b1a8b1a'),
        parent_id=UUID('c0a8b2b0-8b1a-4b1a-9b1a-8b1a8b1a8b1a'),
        page=1,
        title='Info Box',
        children=[]
    )
"""


Heading.__doc__ = """
A heading object.

Args:
    id (UUID): The ID of the heading. Defaults to an autogenerated UUID.
    parent_id (UUID): The ID of the parent chapter.
    page (int): The page number of the chapter.
    title (str): The title of the heading.
    children (list[UUID]): The list of children IDs. Defaults to [].

Examples:
    >>> from uuid import uuid4
    >>> heading = Heading(
    >>>     parent_id=uuid4(),
    >>>     title="Heading",
    >>>     page=1,
    >>> )
    >>> heading
    Heading(
        id=UUID('c0a8b2b0-8b1a-4b1a-9b1a-8b1a8b1a8b1a'),
        parent_id=UUID('c0a8b2b0-8b1a-4b1a-9b1a-8b1a8b1a8b1a'),
        page=1,
        title='Heading',
        children=[]
    )
"""
