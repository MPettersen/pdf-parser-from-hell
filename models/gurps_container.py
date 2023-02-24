from uuid import UUID
from pydantic import Field

from app.models.book_container import BookContainer
from app.models.gurps_custom import (
    Skill,
    Technique,
    Spell
)
from app.models.gurps_general import (
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
    PsionicPower
)

class GurpsContainer(BookContainer):
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

    def _get_gurps(self, obj_id):
        if obj_id in self.advantages:
            return self.advantages[obj_id]
        elif obj_id in self.sub_advantages:
            return self.sub_advantages[obj_id]
        elif obj_id in self.disadvantages:
            return self.disadvantages[obj_id]
        elif obj_id in self.sub_disadvantages:
            return self.sub_disadvantages[obj_id]
        elif obj_id in self.special_limitations:
            return self.special_limitations[obj_id]
        elif obj_id in self.special_enhancements:
            return self.special_enhancements[obj_id]
        elif obj_id in self.enhancements:
            return self.enhancements[obj_id]
        elif obj_id in self.limitations:
            return self.limitations[obj_id]
        elif obj_id in self.gadget_enhancements:
            return self.gadget_enhancements[obj_id]
        elif obj_id in self.gadget_limitations:
            return self.gadget_limitations[obj_id]
        elif obj_id in self.perks:
            return self.perks[obj_id]
        elif obj_id in self.psionic_powers:
            return self.psionic_powers[obj_id]
        elif obj_id in self.skills:
            return self.skills[obj_id]
        elif obj_id in self.techniques:
            return self.techniques[obj_id]
        elif obj_id in self.spells:
            return self.spells[obj_id]
        else:
            raise ValueError("Object ID not found in any of the containers.")

    def _add_gurps(self, obj):
        if isinstance(obj, Advantage):
            self.advantages[obj.id] = obj
        elif isinstance(obj, SubAdvantage):
            self.sub_advantages[obj.id] = obj
        elif isinstance(obj, Disadvantage):
            self.disadvantages[obj.id] = obj
        elif isinstance(obj, SubDisadvantage):
            self.sub_disadvantages[obj.id] = obj
        elif isinstance(obj, SpecialLimitation):
            self.special_limitations[obj.id] = obj
        elif isinstance(obj, SpecialEnhancement):
            self.special_enhancements[obj.id] = obj
        elif isinstance(obj, Enhancement):
            self.enhancements[obj.id] = obj
        elif isinstance(obj, Limitation):
            self.limitations[obj.id] = obj
        elif isinstance(obj, GadgetEnhancement):
            self.gadget_enhancements[obj.id] = obj
        elif isinstance(obj, GadgetLimitation):
            self.gadget_limitations[obj.id] = obj
        elif isinstance(obj, Perk):
            self.perks[obj.id] = obj
        elif isinstance(obj, PsionicPower):
            self.psionic_powers[obj.id] = obj
        elif isinstance(obj, Skill):
            self.skills[obj.id] = obj
        elif isinstance(obj, Technique):
            self.techniques[obj.id] = obj
        elif isinstance(obj, Spell):
            self.spells[obj.id] = obj
        else:
            raise ValueError("Object not recognized.")
        
    def get(self, obj_id):
        try:
            return self._get(obj_id)
        except ValueError:
            return self._get_gurps(obj_id)
    
    def add(self, obj):
        try:
            self._add(obj)
        except ValueError:
            self._add_gurps(obj)
        self._add_to_parent(obj)
        return obj
