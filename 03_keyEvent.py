from random import random

import pygame
from pygame.locals import *
import sys

wHeight = 480
wWidth = 640
wStrings = "Window Title."
wFPS = 20

# initialize
pygame.init()
screen = pygame.display.set_mode((wWidth, wHeight))
pygame.display.set_caption(wStrings)
FPSClock = pygame.time.Clock()

# drawWords
dStrings = "Hello PyGame."
font = pygame.font.SysFont(None, 60)
Word = font.render(dStrings, True, (0, 80, 150))
Word_rect = Word.get_rect()
Word_rect.center = (wWidth/2, wHeight/2)


def main():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(Word, Word_rect)

        # WindowClose
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Word_rect.move_ip(10 * random(), 10 * random())
        pygame.display.update()
    FPSClock.tick(wFPS)


if __name__ == "__main__":
    main()