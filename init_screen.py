import time
import pygame

import config



FPS = 10
DURATION = 3


def init_screen() -> None:
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    background_image = pygame.image.load('Image/i.png')
    background_image = pygame.transform.smoothscale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    running = True
    clock = pygame.time.Clock()
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                running = False
        clock.tick(FPS)
        i += 1
        if i > FPS * DURATION:
            break
