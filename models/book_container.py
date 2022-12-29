import pandas as pd

from uuid import UUID
from pydantic import BaseModel, Field

from models.book_custom import (
    Book,
    Paragraphs,
    List,
    Table
)
from models.book_general import (
    Chapter,
    InfoBox,
    Heading
)


class BookContainer(BaseModel):
    """
    A container for all the book's chapters, paragraphs, lists and tables.
    Note that this class is not a model, but rather a container for the models.

    :param book: The book object.
    """
    book: Book
    chapters: dict[UUID, Chapter] = Field(default_factory=dict)
    paragraphs: dict[UUID, Paragraphs] = Field(default_factory=dict)
    lists: dict[UUID, List] = Field(default_factory=dict)
    tables: dict[UUID, Table] = Field(default_factory=dict)
    info_boxes: dict[UUID, InfoBox] = Field(default_factory=dict)
    headings: dict[UUID, Heading] = Field(default_factory=dict)

    def _get(self, obj_id):
        if obj_id in self.paragraphs:
            return self.paragraphs[obj_id]
        elif obj_id in self.lists:
            return self.lists[obj_id]
        elif obj_id in self.tables:
            return self.tables[obj_id]
        elif obj_id in self.chapters:
            return self.chapters[obj_id]
        elif obj_id in self.headings:
            return self.headings[obj_id]
        elif obj_id in self.info_boxes:
            return self.info_boxes[obj_id]
        else:
            raise ValueError("Object ID not found in any of the containers.")

    def _add(self, obj):
        if isinstance(obj, Chapter):
            self.chapters[obj.id] = obj
        elif isinstance(obj, Paragraphs):
            self.paragraphs[obj.id] = obj
        elif isinstance(obj, List):
            self.lists[obj.id] = obj
        elif isinstance(obj, Table):
            self.tables[obj.id] = obj
        elif isinstance(obj, InfoBox):
            self.info_boxes[obj.id] = obj
        elif isinstance(obj, Heading):
            self.headings[obj.id] = obj
        else:
            raise ValueError("Object not recognized.")
    
    def get(self, obj_id):
        return self._get(obj_id)
    
    def _add_to_parent(self, obj):
        if hasattr(obj, "parent_id") and obj.parent_id:
            if obj.parent_id == self.book.id:
                self.book.children.append(obj.id)
            else:
                self.get(obj.parent_id).children.append(obj.id)

    def add(self, obj):
        self._add(obj)
        self._add_to_parent(obj)
        return obj
    
    def _append(self, parent, child):
        parent.children.append(child.id)
        self.get(child.parent_id).children.append(child.id)
    
    def _get_dict(self, obj, children=True):
        obj_dict = obj.dict()
        if children:
            obj_dict["children"] = self.get_children(obj, _dict=True)
        return obj_dict
    
    def _get_child(self, child_id, _dict=False):
        return (
            self.get(child_id)
            if not _dict
            else self.get(child_id).dict()
        )
    
    def get_children(self, parent, _dict=False):
        children = []
        for child_id in parent.children:
            child = self._get_child(child_id, _dict)
            if hasattr(child, "children"):
                children.extend([child, self.get_children(child, _dict)])
            else:
                children.append(child)
        return children

    def get_book_recursive(self):
        return [self.book, self.get_children(self.book)]

    def get_book(self):
        return self.book

    def get_book_dict(self):
        return self._get_dict(self.get_book(), children=True)
    
    def get_book_dict_recursive(self):
        return self._get_dict(self.get_book(), children=True, recursive=True)
