import pygame

def timer() -> None:
    countM = 0
    countH = 0
    time = pygame.time.Clock() 
    MINUTS = pygame.USEREVENT + 1
    HOUR = pygame.USEREVENT + 2