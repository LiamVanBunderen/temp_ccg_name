from dataclasses import dataclass
from enum import Enum
import pygame

# cspell: ignore colorkey, blit


class Family(Enum):
    TEMP = "temp"
    KNIGHT = "knight"


@dataclass
class Card:
    health: int = 20
    damage: int = 5
    energy: int = 1
    movement: int = 1

    ID: str = "null"
    NAME: str = "Null"
    FAMILY: Family = Family.TEMP

    def __post_init__(self):
        self.font: str = "taxon"
        self.art: pygame.Surface = self.generate_art()

    def generate_art(self) -> pygame.Surface:
        card: pygame.Surface = pygame.Surface((250, 350))
        try:
            test: pygame.font.Font = pygame.font.Font(
                f"assets/{self.FAMILY.value}/font/{self.font}.ttf"
            )
            base: pygame.Surface = pygame.image.load(f"assets/{self.FAMILY.value}/base.png")
            character: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/{self.ID}/character_art.png"
            )
            desc: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/description_box.png"
            )
            empty: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/energy_empty.png"
            )
            full: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/energy_full.png"
            )
            moves: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/movement.png"
            )
            health_stat: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/health.png"
            )
            damage_stat: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/damage.png"
            )
            border: pygame.Surface = pygame.image.load(
                f"assets/{self.FAMILY.value}/borders.png"
            )
        except:
            

        key: pygame.Color = base.get_at((0, 0))

        card.fill(key)
        card.set_colorkey(key)

        card.blit(base, (0, 0))
        card.blit(desc, (25, 245))
        card.blit(character, (45, 35))
        card.blit(health_stat, (41, 205))
        card.blit(damage_stat, (126, 205))

        for slot in range(10):
            card.blit(full if (slot < self.energy) else empty, (15, (14 * slot) + 45))

        for slot in range(self.movement):
            card.blit(moves, (215, (20 * slot) + 45))

        card.blit(border, (0, 0))
        return card


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((350, 450))
    pygame.display.set_caption("Testing_Card")
    screen.fill(pygame.Color(120, 120, 120))

    testCard = Card()

    screen.blit(testCard.art, (50, 50))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()

def printError(error: str = "") -> None:
    print(f"\u001b[31m{error}\u001b[0m")
