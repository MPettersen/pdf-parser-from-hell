import pandas as pd


class BookContainer:
    """
    A container for all the book's chapters, paragraphs, lists and tables.

    Note that this class is not a model, but rather a container for the models.

    PS: This entire class was made by GitHub Copilot, including the docstring (above
    and below this remark). The only thing I did was add the docstring, part of it at least.
    It really annoys me how good Copilot is at this. I'm not sure if I should be happy or sad.

    :param book: The book object.
    """
    def __init__(self, book):
        self.book = book
        self.chapters = {}
        self.paragraphs = {}
        self.lists = {}
        self.tables = {}

    def add_chapter(self, chapter):
        self.chapters[chapter.id] = chapter

    def add_paragraph(self, paragraph):
        self.paragraphs[paragraph.id] = paragraph

    def add_list(self, list_):
        self.lists[list_.id] = list_

    def add_table(self, table):
        self.tables[table.id] = table

    def get_chapter(self, chapter_id):
        return self.chapters[chapter_id]

    def get_paragraph(self, paragraph_id):
        return self.paragraphs[paragraph_id]

    def get_list(self, list_id):
        return self.lists[list_id]

    def get_table(self, table_id):
        return self.tables[table_id]

    def get_chapter_children(self, chapter_id):
        chapter = self.get_chapter(chapter_id)
        children = []
        for child_id in chapter.children:
            if child_id in self.paragraphs:
                children.append(self.get_paragraph(child_id))
            elif child_id in self.lists:
                children.append(self.get_list(child_id))
            elif child_id in self.tables:
                children.append(self.get_table(child_id))
        return children

    def get_book_children(self):
        children = []
        for child_id in self.book.children:
            if child_id in self.chapters:
                children.append(self.get_chapter(child_id))
        return children

    def get_chapter_children_recursive(self, chapter_id):
        chapter = self.get_chapter(chapter_id)
        children = []
        for child_id in chapter.children:
            if child_id in self.paragraphs:
                children.append(self.get_paragraph(child_id))
            elif child_id in self.lists:
                children.append(self.get_list(child_id))
            elif child_id in self.tables:
                children.append(self.get_table(child_id))
            elif child_id in self.chapters:
                children.extend(self.get_chapter_children_recursive(child_id))
        return children

    def get_book_children_recursive(self):
        children = []
        for child_id in self.book.children:
            if child_id in self.chapters:
                children.extend(self.get_chapter_children_recursive(child_id))
        return children

    def get_book(self):
        return self.book

    def get_book_dict(self):
        book = self.get_book()
        book_dict = book.dict()
        book_dict["children"] = []
        for child_id in book.children:
            if child_id in self.chapters:
                book_dict["children"].append(self.get_chapter(child_id).dict())
        return book_dict
    
    def get_book_dict_recursive(self):
        book = self.get_book()
        book_dict = book.dict()
        book_dict["children"] = []
        for child_id in book.children:
            if child_id in self.chapters:
                book_dict["children"].append(self.get_chapter_dict_recursive(child_id))
        return book_dict
    
    def get_chapter_dict(self, chapter_id):
        chapter = self.get_chapter(chapter_id)
        chapter_dict = chapter.dict()
        chapter_dict["children"] = []
        for child_id in chapter.children:
            if child_id in self.paragraphs:
                chapter_dict["children"].append(self.get_paragraph(child_id).dict())
            elif child_id in self.lists:
                chapter_dict["children"].append(self.get_list(child_id).dict())
            elif child_id in self.tables:
                chapter_dict["children"].append(self.get_table(child_id).dict())
        return chapter_dict
    
    def get_chapter_dict_recursive(self, chapter_id):
        chapter = self.get_chapter(chapter_id)
        chapter_dict = chapter.dict()
        chapter_dict["children"] = []
        for child_id in chapter.children:
            if child_id in self.paragraphs:
                chapter_dict["children"].append(self.get_paragraph(child_id).dict())
            elif child_id in self.lists:
                chapter_dict["children"].append(self.get_list(child_id).dict())
            elif child_id in self.tables:
                chapter_dict["children"].append(self.get_table(child_id).dict())
            elif child_id in self.chapters:
                chapter_dict["children"].append(self.get_chapter_dict_recursive(child_id))
        return chapter_dict
    
    def get_paragraph_dict(self, paragraph_id):
        paragraph = self.get_paragraph(paragraph_id)
        return paragraph.dict()
    
    def get_list_dict(self, list_id):
        list_ = self.get_list(list_id)
        return list_.dict()
    
    def get_table_dict(self, table_id):
        table = self.get_table(table_id)
        return table.dict()
