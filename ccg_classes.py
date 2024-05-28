from dataclasses import dataclass
from enum import Enum
from error_management import printError
import json
import pygame
import sys

# cspell: ignore colorkey, blit, blits


class Family(Enum):
    TEMP = "temp"
    KNIGHT = "knight"


@dataclass
class Card:
    ID: str = "null"

    def __post_init__(self):
        try:
            f = open("cards.json")
            foundation: dict[str, int | str] = json.load(f)[self.ID]
            f.close()
        except:
            printError("failed to load cards (json)")
            sys.exit()
        finally:
            del f

        self.health: int = foundation["health"]
        self.damage: int = foundation["damage"]
        self.energy: int = foundation["energy"]
        self.movement: int = foundation["movement"]

        self.NAME: str = foundation["name"]
        self.FAMILY: Family = Family(foundation["family"])

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
        num_font: pygame.font.Font

        for asset in assets:
            extension: str = f"/{self.ID}" if asset == "character_art" else ""
            try:
                assets[asset] = pygame.image.load(
                    f"assets/{self.FAMILY.value}/{asset}{extension}.png"
                )
            except FileNotFoundError:
                try:
                    extension = f"/null" if asset == "character_art" else ""
                    assets[asset] = pygame.image.load(
                        f"assets/temp/{asset}{extension}.png"
                    )
                except FileNotFoundError:
                    printError(
                        f"A Critical File is Missing: assets/temp/{asset}{extension}.png"
                    )

        try:
            font = pygame.font.Font(f"assets/{self.FAMILY.value}/font.ttf", 18)
        except:
            try:
                font = pygame.font.Font(f"assets/temp/font/taxon.ttf", 24)
            except FileNotFoundError:
                printError("A Critical File is Missing: assets/temp/font/taxon.ttf")

        try:
            num_font = pygame.font.Font(f"assets/{self.FAMILY.value}/font.ttf", 18)
        except:
            try:
                num_font = pygame.font.Font(f"assets/temp/font/ccg-temp-numbers.ttf", 3)
            except FileNotFoundError:
                printError(
                    "A Critical File is Missing: assets/temp/font/ccg-temp-numbers.ttf"
                )

        key: pygame.Color = assets["base"].get_at((0, 0))
        text_colour: pygame.Color = assets["base"].get_at((1, 0))
        num_colour: pygame.Color = assets["base"].get_at((2, 0))
        if num_colour.a == 0:
            num_colour = text_colour

        assets["base"].set_at((1, 0), key)

        card.fill(key)
        card.set_colorkey(key)

        temp: int = 9

        card.blits(
            (
                (assets["base"], (0, 0)),
                (assets["description_box"], (25, 245)),
                (assets["character_art"], (45, 35)),
                (assets["health"], (50, 205)),
                (assets["damage"], (135, 205)),
            ),
            False,
        )

        card.blits(
            (
                (
                    (
                        assets["energy_full"]
                        if (slot < self.energy)
                        else assets["energy_empty"]
                    ),
                    (15, (14 * slot) + 45),
                )
                for slot in range(10)
            ),
            False,
        )

        card.blits(
            (
                (assets["movement"], (215, (20 * slot) + 45))
                for slot in range(self.movement)
            ),
            False,
        )

        card.blits(
            (
                (
                    num_font.render(f"{self.health:02}", False, num_colour),
                    (87, 221 - (num_font.size(f"{self.health:02}")[1] / 2)),
                ),
                (
                    num_font.render(f"{self.damage:02}", False, num_colour),
                    (172, 221 - (num_font.size(f"{self.damage:02}")[1] / 2)),
                ),
            ),
            False,
        )

        font.bold = True
        card.blit(
            font.render(self.NAME, False, text_colour),
            (
                30 + (190 - font.size(self.NAME)[0]) / 2,
                250 + (70 - font.size(self.NAME)[1]) / 2,
            ),
        )
        font.bold = False

        card.blit(assets["borders"], (0, 0))
        return card


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((350, 450))
    pygame.display.set_caption("Testing_Card")
    screen.fill(pygame.Color(0, 0, 0))

    testCard = Card("archer")

    screen.blit(testCard.art, (50, 50))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
