import pygame
from random import randint

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ALICEBLUE = (240, 248, 255)
WIDTH = 1260
HEIGHT = 640
COLOR = ALICEBLUE
SECERT_COLOR = WHITE

FPS = 40
flak = 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
running = True
xFIO = 400
yFIO = 150
xVAR = 450
yVAR = 360
xHW = 400
yHW = 400

xFIO1 = xFIO
yFIO1 = yFIO
xVAR1 = xVAR
yVAR1 = yVAR
xHW1 = xHW
yHW1 = yHW
pygame.init()

deffont = pygame.font.SysFont(None, 50)
bigfont = pygame.font.SysFont(None, 170)
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                xFIO = xFIO1
                yFIO = yFIO1
                xVAR = xVAR1
                yVAR = yVAR1
                xHW = xHW1
                yHW = yHW1
                screen.fill(WHITE) 
            pygame.display.update()
        if event.type == pygame.MOUSEWHEEL:
            x1 = randint(0,255)
            x2 = randint(0,255)
            x3 = randint(0,255)
            COLOR = (x1, x2, x3)
            screen.fill(WHITE) 
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                y1 = randint(0,255)
                y2 = randint(0,255)
                y3 = randint(0,255)
                print(event)
                SECERT_COLOR = (y1, y2, y3)
                screen.fill(WHITE) 
            pygame.display.update()

    FIO = deffont.render("ROZHKOV ALEKSANDER SERGEEVIS", False, (COLOR))
    VAR = deffont.render("1 вариант", False, (COLOR))
    HW = bigfont.render("Text", False, (COLOR))
    Secret = deffont.render("Чего надо?", False, (SECERT_COLOR))

    screen.blit(FIO, (xFIO, yFIO))
    screen.blit(VAR, (xVAR, yVAR))
    screen.blit(HW, (xHW, yHW))
    screen.blit(Secret, (300, 200))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)



    if event.type == pygame.MOUSEBUTTONDOWN and flak == 0:
        flak = 1
    elif event.type == pygame.MOUSEBUTTONDOWN and flak == 1:
        flak = 0


    if flak == 1:
        yFIO += 1
        xVAR -= 1
        xHW -= 1
        screen.fill(WHITE) 
    pygame.display.update()





        

    
pygame.quit()
