import pygame
import sys

# cspell: ignore Windowresized, blit, keydown, fullscreen

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


def drawBase():
    screen.fill(BACKGROUND)


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
                    case pygame.K_F11:
                        window.toggle_fullscreen()
                    case _:
                        pass

    drawBase()

    window.flip()
    clock.tick(60)

sys.exit()
