from dataclasses import dataclass
from enum import Enum
import pygame

# cspell: ignore colorkey, blit


class Family(Enum):
    TEMP = 0
    KNIGHT = 1


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
        key: pygame.Color = pygame.Color(255, 100, 0)
        base: pygame.Color = pygame.Color(255, 255, 245)

        card.fill(key)
        card.set_colorkey(key)

        pygame.draw.rect(card, base, pygame.Rect(0, 0, 250, 350), 0, 15)

        return card


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((350, 450))
    pygame.display.set_caption("Testing_Card")

    testCard = Card()

    screen.blit(testCard.art, (50, 50))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
