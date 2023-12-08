from sys import exit
import pygame
import pygame_widgets
from pygame_widgets.button import Button

import config
from seting import seting_menu
from utils import hide_widgets, show_widgets

FPS = 20
LIGHT_BLUE = (64, 224, 208)

class CustomButton(Button):
    def draw(self):
        """ Display to surface """
        if not self._hidden:
            if self.borderThickness:
                pygame.draw.rect(
                    self.win, self.borderColour, (self._x, self._y, self._width, self._height),
                    border_radius=self.radius, width=self.borderThickness
                )

            if self.image:
                self.imageRect = self.image.get_rect()
                self.alignImageRect()
                self.win.blit(self.image, self.imageRect)

            self.textRect = self.text.get_rect()
            self.alignTextRect()
            self.win.blit(self.text, self.textRect)


def main_menu() -> None:
    def btn_start_click():
        nonlocal running
        running = False

    def seting() -> None:
        hide_widgets(widgets)
        seting_menu()
        show_widgets(widgets)
        screen.blit(background_image, (0, 0))

    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    background_image = pygame.image.load('Image/i.png')
    background_image = pygame.transform.smoothscale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))

    btn_start = CustomButton(screen, 1370, 270, 145, 50, onClick=btn_start_click, text='Play', borderThickness=2)
    btn_exit = CustomButton(screen, 1370, 430, 145, 50, onClick=exit, text='Exit', borderThickness=2)
    btn_seting = CustomButton(screen, 1370, 350, 145, 50, onClick=seting, text='Seting', borderThickness=2)

    widgets = [btn_start, btn_exit, btn_seting]

    pygame.display.update()
    running = True
    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(FPS)
    hide_widgets(widgets)



