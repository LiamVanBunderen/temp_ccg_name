from dataclasses import dataclass
from enum import Enum
from pygame import Surface


class Family(Enum):
    KNIGHT = 0


@dataclass
class Card:
    health: int = 20
    damage: int = 5
    energy: int = 1

    NAME: str = "Null"
    FAMILY: Family = Family.KNIGHT

    def __post_init__(self):
        self.art: Surface = self.generate_art()

    def generate_art(self) -> Surface:
        pass
