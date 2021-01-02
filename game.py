import pygame
from pygame.locals import *
import time


import screenf
import playerf
import tilef
import levelsf

pygame.init()
clock = pygame.time.Clock()

world=tilef.World()
player=playerf.Player(screenf.screenHeight-100, 100)

run = True
while run:
    clock.tick(30) #fps
    screenf.screen.blit(screenf.background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            #sys.exit()

    #screenf.draw_grid()
    world.update_tile(1)
    player.update()

    pygame.display.update()