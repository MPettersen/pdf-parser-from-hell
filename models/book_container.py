import pandas as pd

from uuid import UUID
from pydantic import BaseModel, Field

from models import (
    Book,
    Chapter,
    Paragraphs,
    List,
    Table,
    InfoBox,
    Headings,
    Advantage,
    SubAdvantage,
    Disadvantage,
    SubDisadvantage,
    SpecialLimitation,
    SpecialEnhancement,
    Enhancement,
    Limitation,
    GadgetEnhancement,
    GadgetLimitation,
    Perk,
    PsionicPower,
    Skill,
    Technique,
    Spell
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
    headings: dict[UUID, Headings] = Field(default_factory=dict)
    advantages: dict[UUID, Advantage] = Field(default_factory=dict)
    sub_advantages: dict[UUID, SubAdvantage] = Field(default_factory=dict)
    disadvantages: dict[UUID, Disadvantage] = Field(default_factory=dict)
    sub_disadvantages: dict[UUID, SubDisadvantage] = Field(default_factory=dict)
    special_limitations: dict[UUID, SpecialLimitation] = Field(default_factory=dict)
    special_enhancements: dict[UUID, SpecialEnhancement] = Field(default_factory=dict)
    enhancements: dict[UUID, Enhancement] = Field(default_factory=dict)
    limitations: dict[UUID, Limitation] = Field(default_factory=dict)
    gadget_enhancements: dict[UUID, GadgetEnhancement] = Field(default_factory=dict)
    gadget_limitations: dict[UUID, GadgetLimitation] = Field(default_factory=dict)
    perks: dict[UUID, Perk] = Field(default_factory=dict)
    psionic_powers: dict[UUID, PsionicPower] = Field(default_factory=dict)
    skills: dict[UUID, Skill] = Field(default_factory=dict)
    techniques: dict[UUID, Technique] = Field(default_factory=dict)
    spells: dict[UUID, Spell] = Field(default_factory=dict)

    def add_chapter(self, chapter):
        self.chapters[chapter.id] = chapter

    def add_paragraph(self, paragraph):
        self.paragraphs[paragraph.id] = paragraph

    def add_list(self, list_):
        self.lists[list_.id] = list_

    def add_table(self, table):
        self.tables[table.id] = table
    
    def add_info_box(self, info_box):
        self.info_boxes[info_box.id] = info_box
    
    def add_headings(self, headings):
        self.headings[headings.id] = headings
    
    def add_advantage(self, advantage):
        self.advantages[advantage.id] = advantage
    
    def add_sub_advantage(self, sub_advantage):
        self.sub_advantages[sub_advantage.id] = sub_advantage
    
    def add_disadvantage(self, disadvantage):
        self.disadvantages[disadvantage.id] = disadvantage
    
    def add_sub_disadvantage(self, sub_disadvantage):
        self.sub_disadvantages[sub_disadvantage.id] = sub_disadvantage

    def add_special_limitation(self, special_limitation):
        self.special_limitations[special_limitation.id] = special_limitation
    
    def add_special_enhancement(self, special_enhancement):
        self.special_enhancements[special_enhancement.id] = special_enhancement
    
    def add_enhancement(self, enhancement):
        self.enhancements[enhancement.id] = enhancement
    
    def add_limitation(self, limitation):
        self.limitations[limitation.id] = limitation
    
    def add_gadget_enhancement(self, gadget_enhancement):
        self.gadget_enhancements[gadget_enhancement.id] = gadget_enhancement
    
    def add_gadget_limitation(self, gadget_limitation):
        self.gadget_limitations[gadget_limitation.id] = gadget_limitation
    
    def add_perk(self, perk):
        self.perks[perk.id] = perk

    def add_psionic_power(self, psionic_power):
        self.psionic_powers[psionic_power.id] = psionic_power
    
    def add_skill(self, skill):
        self.skills[skill.id] = skill
    
    def add_technique(self, technique):
        self.techniques[technique.id] = technique
    
    def add_spell(self, spell):
        self.spells[spell.id] = spell

    def get(self, obj_id):
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
        elif obj_id in self.advantages:
            return self.advantages[obj_id]
        elif obj_id in self.sub_advantages:
            return self.sub_advantages[obj_id]
        else:
            raise ValueError("Object ID not found in any of the containers.")
    
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
    
    def get_children(self, id, _dict=False):
        parent = self.get(id)
        children = []
        for child_id in parent.children:
            child = self._get_child(child_id, _dict)
            if hasattr(child, "children"):
                children.append([child, self.get_children(child, _dict)])
            else:
                children.append(child)
        return children

    def get_book_recursive(self):
        return self.get_children(self.book.id, recursive=True)

    def get_book(self):
        return self.book

    def get_book_dict(self):
        return self._get_dict(self.get_book(), children=True)
    
    def get_book_dict_recursive(self):
        return self._get_dict(self.get_book(), children=True, recursive=True)
