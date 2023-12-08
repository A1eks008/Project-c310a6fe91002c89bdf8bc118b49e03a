import math
import pygame

import config
from init_screen import init_screen
from main_menu import main_menu
from utils import events_handler
import rooms
import Units.entite

pygame.init()

init_screen()

main_menu()
while True:
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    background_image = pygame.image.load('Image/main_задний_фон.jpg')
    background_image = pygame.transform.smoothscale(background_image, screen.get_size())
    running = True

    group_rooms = pygame.sprite.Group() 
    group_rooms.add(rooms.MainRooms(695, 396, 250, 175))
    group_rooms.add(rooms.Corridoor(342, 477, 323, 81))
    group_rooms.add(rooms.Corridoor(983, 477, 323, 81))
    group_rooms.add(rooms.AnomalyRoom(327, 390, 170, 70))
    group_rooms.add(rooms.AnomalyRoominv(517, 390, 170, 70))
    group_rooms.add(rooms.AnomalyRoom(953, 390, 170, 70))
    group_rooms.add(rooms.AnomalyRoominv(1217, 390, 170, 70))

    group_entite = pygame.sprite.Group() 
    group_entite.add(Units.entite.Igor(737, 529))
    
    while running: 
        events = pygame.event.get()

        #Не двигается
        Units.entite.randmows()


        for event in events:
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.blit(background_image, (0, 0))
        group_rooms.draw(screen)
        group_entite.draw(screen)
        pygame.display.flip()
    main_menu()
pygame.quit()
