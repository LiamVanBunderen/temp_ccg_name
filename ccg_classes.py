from dataclasses import dataclass
from enum import Enum
import pygame


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
        self.art: pygame.Surface = self.generate_art()

    def generate_art(self) -> pygame.Surface:
        card: pygame.Surface = pygame.Surface((250, 350))
        key: pygame.Color
