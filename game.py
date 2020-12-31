import pygame
from pygame.locals import *

import screenf
import playerf
import tilef
import levelsf

pygame.init()

world=tilef.World()

run = True
while run:
    screenf.screen.blit(screenf.background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit()
            run=False
            pygame.quit()
            #sys.exit()

    #screenf.draw_grid()
    world.update_tile(1)

    pygame.display.update()