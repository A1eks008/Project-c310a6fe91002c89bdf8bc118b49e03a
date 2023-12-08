import pygame
from abc import ABC, abstractmethod
from typing import Optional
from random import randint


import pygame
from pygame.sprite import Group
from pygame.transform import smoothscale

load_image = pygame.image.load

randoms = randint

class Entite(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, hp = 100) -> None:
        super().__init__()
        self.hp: int = hp,
        x: int
        y: int
    
    @abstractmethod
    def get_image(self) -> pygame.Surface:
        pass


class Agent(Entite):
    image = load_image('Image/agent.png')
    #def __init__(self, syndicate, spec, char, tool = 00000, armor = 0000, hp = 100, mp = 100, umbra = 0, spec_ops = 0) -> None:
    def __init__(self, x, y, tool = 00000, armor = 0000, hp = 100, mp = 100, umbra = 0, spec_ops = 0) -> None:
        super().__init__(x, y)
        self.mp: int = mp
        self.armor: int = armor
        self.tool: int = tool
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        #self.speed = speed
        # self.char: int = char
        # self.spec: int = spec
        # self.spec_ops: str = spec_ops
        # self.umbra: str = umbra
        # self.syndicate: str = syndicate
# class umbra (Agent):
#     def __init__(self, spec, type, tool, hp = 100, mp = 100) -> None:
#         self.hp: int = hp
#         self.mp:int = mp
#         self.tool:int = tool
#         self.type:int = type
#         self.spec:int = spec
# class spec_ops(Agent):
#     def __init__(self,spec_ops_armor,spec_ops_tool,hp = 100,mp =100) -> None:
#         self.spec_ops_armor = spec_ops_armor
#         self.spec_ops_tool = spec_ops_tool
#         self.hp:int = hp
#         self.mp:int = mp
class Hp():
    def __init__(self,physical,mental) -> None:
        type_HP = "physical"
        self.physical = physical
class Mp():
    def __init__(self,mental) -> None:
        type_HP = "mental"
        self.mental = mental
        

    
    

    pass
# class Anomaly(Entite):
#     def __init__(self,alfa,beta,lamda,omega,digamma,) -> None:
#         class alfa
    

speed = 5
class Igor(Agent):
    def get_image(self) -> pygame.surface.Surface:
        return pygame.image.load('Image/agent.png')
    def randmove(x) ->None:
        s = randoms(1,2)
        r = randoms(50,250)
        d = r
        speed = 5
        if s==1:
            while r == d:
                x += speed
                d += speed
        elif s==2:
            while r == d:
                x -= speed
                d += speed