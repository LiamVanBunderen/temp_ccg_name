from dataclasses import dataclass
from enum import Enum
import json
import pygame

# cspell: ignore colorkey, blit


class Family(Enum):
    TEMP = "temp"
    KNIGHT = "knight"


@dataclass
class Card:
    ID: str = "null"

    def __post_init__(self):
        try:
            json.load(open("cards.json"))

        self.health: int = 20
        self.damage: int = 5
        self.energy: int = 1
        self.movement: int = 1

        self.NAME: str = "Null"
        self.FAMILY: Family = Family.TEMP

        self.art: pygame.Surface = self.generate_art()

    def generate_art(self) -> pygame.Surface:
        card: pygame.Surface = pygame.Surface((250, 350))
        assets: dict[str, pygame.Surface] = {
            "base": pygame.Surface((0, 0)),
            "character_art": pygame.Surface((0, 0)),
            "description_box": pygame.Surface((0, 0)),
            "energy_empty": pygame.Surface((0, 0)),
            "energy_full": pygame.Surface((0, 0)),
            "movement": pygame.Surface((0, 0)),
            "health": pygame.Surface((0, 0)),
            "damage": pygame.Surface((0, 0)),
            "borders": pygame.Surface((0, 0)),
        }
        font: pygame.font.Font

        for asset in assets:
            extension: str = f"/{self.ID}" if asset == "character_art" else ""
            try:
                assets[asset] = pygame.image.load(
                    f"assets/{self.FAMILY.value}/{asset}{extension}.png"
                )
            except FileNotFoundError:
                extension = f"/null" if asset == "character_art" else ""
                assets[asset] = pygame.image.load(f"assets/temp/{asset}{extension}.png")

        try:
            font = pygame.font.Font(f"assets/{self.FAMILY.value}/font.ttf")
        except:
            font = pygame.font.Font(f"assets/temp/font/taxon.ttf")

        key: pygame.Color = assets["base"].get_at((0, 0))

        card.fill(key)
        card.set_colorkey(key)

        card.blit(assets["base"], (0, 0))
        card.blit(assets["description_box"], (25, 245))
        card.blit(assets["character_art"], (45, 35))
        card.blit(assets["health"], (41, 205))
        card.blit(assets["damage"], (126, 205))

        for slot in range(10):
            card.blit(
                (
                    assets["energy_full"]
                    if (slot < self.energy)
                    else assets["energy_empty"]
                ),
                (15, (14 * slot) + 45),
            )

        for slot in range(self.movement):
            card.blit(assets["movement"], (215, (20 * slot) + 45))

        card.blit(assets["borders"], (0, 0))
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
