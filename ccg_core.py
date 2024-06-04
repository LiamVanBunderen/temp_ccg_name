import pygame
import sys

# cspell: ignore Windowresized, blit, keydown, fullscreen, colorkey

pygame.init()

window = pygame.display
screen = window.set_mode(
    (
        min(1000, min(i[0] for i in window.get_desktop_sizes())),
        min(800, min(i[1] for i in window.get_desktop_sizes())),
    ),
    pygame.RESIZABLE,
)
window.set_caption("temp_ccg")
clock = pygame.time.Clock()

run = True

BACKGROUND = pygame.Color(29, 117, 62)
GUI_BASE = pygame.Color(25, 25, 25)
HEALTH_BAR = pygame.Color(200, 50, 25)
ENERGY_BAR = pygame.Color(10, 100, 255)
COLOUR_KEY = pygame.Color(255, 0, 255)


def drawBase():

    base = pygame.Surface(window.get_window_size())
    meat = pygame.Surface(window.get_window_size())
    outline = pygame.Surface(window.get_window_size())

    base.fill(COLOUR_KEY)
    base.set_colorkey(COLOUR_KEY)
    base.set_alpha(100)
    pygame.draw.rect(
        base,
        GUI_BASE,
        pygame.Rect(
            5,
            5,
            window.get_window_size()[0] - 10,
            max((window.get_window_size()[1] - 10) / 13, 5),
        ),
        0,
    )
    pygame.draw.rect(
        base,
        GUI_BASE,
        pygame.Rect(
            5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 26 - 2.5, 5),
        ),
        0,
    )
    pygame.draw.rect(
        base,
        GUI_BASE,
        pygame.Rect(
            5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            )
            + max((window.get_window_size()[1] - 10) / 26 + 2.5, 5),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 26 - 2.5, 5),
        ),
        0,
    )
    pygame.draw.rect(
        base,
        GUI_BASE,
        pygame.Rect(
            (window.get_window_size()[0] - 10) / 7 * 6 + 5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 13, 5),
        ),
        0,
    )
    pygame.draw.rect(
        base,
        GUI_BASE,
        pygame.Rect(
            (window.get_window_size()[0] - 10) / 7 + 10,
            min(
                (window.get_window_size()[1] - 5) / 13 * 9,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7 * 5 - 10,
            max((window.get_window_size()[1] - 10) / 13 * 4, 5),
        ),
        0,
    )

    meat.fill(COLOUR_KEY)
    meat.set_colorkey(COLOUR_KEY)
    pygame.draw.rect(
        meat,
        HEALTH_BAR,
        pygame.Rect(
            5,
            5,
            window.get_window_size()[0] - 10,
            max((window.get_window_size()[1] - 10) / 13, 5),
        ),
        0,
    )
    pygame.draw.rect(
        meat,
        HEALTH_BAR,
        pygame.Rect(
            5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 26 - 2.5, 5),
        ),
        0,
    )
    pygame.draw.rect(
        meat,
        ENERGY_BAR,
        pygame.Rect(
            5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            )
            + max((window.get_window_size()[1] - 10) / 26 + 2.5, 5),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 26 - 2.5, 5),
        ),
        0,
    )

    outlineWidth = max(
        min(
            5,
            min(
                (window.get_window_size()[0] - 10) // 26,
                (window.get_window_size()[1] - 10),
            )
            // 2
            - 2,
        ),
        1,
    )
    outline.fill(COLOUR_KEY)
    outline.set_colorkey(COLOUR_KEY)
    pygame.draw.rect(
        outline,
        GUI_BASE,
        pygame.Rect(
            5,
            5,
            window.get_window_size()[0] - 10,
            max((window.get_window_size()[1] - 10) / 13, 5),
        ),
        outlineWidth,
    )
    pygame.draw.rect(
        outline,
        GUI_BASE,
        pygame.Rect(
            5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 26 - 2.5, 5),
        ),
        max(min(outlineWidth * 2, 10) // 2, 1),
    )
    pygame.draw.rect(
        outline,
        GUI_BASE,
        pygame.Rect(
            5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            )
            + max((window.get_window_size()[1] - 10) / 26 + 2.5, 5),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 26 - 2.5, 5),
        ),
        max(min(outlineWidth * 2, 10) // 2, 1),
    )
    pygame.draw.rect(
        outline,
        GUI_BASE,
        pygame.Rect(
            (window.get_window_size()[0] - 10) / 7 * 6 + 5,
            min(
                (window.get_window_size()[1] - 5) / 13 * 12,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7,
            max((window.get_window_size()[1] - 10) / 13, 5),
        ),
        outlineWidth,
    )
    pygame.draw.rect(
        outline,
        GUI_BASE,
        pygame.Rect(
            (window.get_window_size()[0] - 10) / 7 + 10,
            min(
                (window.get_window_size()[1] - 5) / 13 * 9,
                (window.get_window_size()[1] - 10),
            ),
            (window.get_window_size()[0] - 10) / 7 * 5 - 10,
            max((window.get_window_size()[1] - 10) / 13 * 4, 5),
        ),
        outlineWidth,
    )

    screen.fill(BACKGROUND)
    screen.blit(base, (0, 0))
    screen.blit(meat, (0, 0))
    screen.blit(outline, (0, 0))


drawBase()

while run:

    for event in pygame.event.get():
        match (event.type):
            case pygame.QUIT:
                run = False
            case pygame.WINDOWRESIZED:
                screen = window.set_mode(window.get_window_size(), pygame.RESIZABLE)
            case pygame.KEYDOWN:
                match (event.key):
                    case _:
                        pass

    drawBase()

    window.flip()
    clock.tick(60)

sys.exit()
