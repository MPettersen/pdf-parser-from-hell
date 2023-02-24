from models.base import (
    TitleChildrenItem,
    TitleChildrenTypesItem,
    TitleChildrenCostTypesItem
)


class Skill(TitleChildrenTypesItem):
    defaults: list[str]
    prerequisites: list[str]
    specialization: bool = False


class Technique(TitleChildrenItem):
    difficulty_level: str
    defaults: list[str]
    prerequisites: list[str]
    specialization: bool = False


class Spell(TitleChildrenCostTypesItem):
    spell_class: str = "IQ/Hard"
    duration: str
    time_to_cast: list[str]
    prerequisites: list[str]
