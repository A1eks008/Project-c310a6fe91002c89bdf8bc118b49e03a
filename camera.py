import pygame

class Camera():
    SPEED_CAM = 0.1
    def __init__(self, width, height) -> None:
        self.dx = 0
        self.dy = 0
        self.x = width // 2
        self.y = height // 2
        self.observers = []

    def add(self, observers):
        self.observers.append(observers)

    def add_group(self, group):
        for sprite in group:
            self.add(sprite)

    def _apply(self):
        for observer in self.observers:
            observer.rect.x += int(self.dx * self.SPEED_CAM)
            observer.rect.y += int(self.dy * self.SPEED_CAM)

    def update_xy(self,target):
        self.dx = - (self.x // 2 - self.x)
        self.dy = - (self.y // 2 - self.y)