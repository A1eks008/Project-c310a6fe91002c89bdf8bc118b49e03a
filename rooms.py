from abc import ABC, abstractmethod
from typing import Optional
#from random import randint

import pygame
from pygame.sprite import Group
from pygame.transform import smoothscale

pg = pygame

class Rooms(ABC, pygame.sprite.Sprite):
    def __init__(self, 
            x: int,
            y: int,
            w: Optional[int] = None,
            h: Optional[int] = None,
            *groups: Group
        ) -> None:
        super().__init__(*groups)
        self.image = self.get_image()
        if w is not None and w is not None:
            self.image = smoothscale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
    
    @abstractmethod
    def get_image(self) -> pygame.surface.Surface:
        pass

    def get_floor_y(self) -> int:
        return self.rect.top + int(round(0.915 * self.rect.height))


class MainRooms(Rooms):
    def get_image(self) -> pygame.surface.Surface:
        return pygame.image.load('Image/mainroom1.png')

class Corridoor(Rooms):
    def get_image(self) -> pygame.surface.Surface:
        return pygame.image.load('Image/corridoor.png')

class AnomalyRoom(Rooms):
    def get_image(self) -> pygame.surface.Surface:
        return pygame.image.load('Image/anomalyRoom.png')

class AnomalyRoominv(Rooms):
    def get_image(self) -> pygame.surface.Surface:
        return pygame.image.load('Image/anomalyRoominv.png')

class OparatorRoom():
    def get_image(self) -> pygame.surface.Surface:
        return pygame.image.load('Image/operatorroom.png')

