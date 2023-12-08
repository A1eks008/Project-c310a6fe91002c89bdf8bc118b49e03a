import pygame
import pygame_widgets
from pygame_widgets.button import Button

import config
from utils import events_handler


FPS = 10

def seting_menu() -> None:
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    background_image = pygame.image.load('Image/seting.png')
    background_image = pygame.transform.smoothscale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    running = True


    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()
        events_handler(events)
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(FPS)


