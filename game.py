import pygame
from pygame.locals import *
import time


import screenf
import playerf
import tilef
import levelsf
import enemyf

pygame.init()
clock = pygame.time.Clock()

world=tilef.World()
player = playerf.Player(tilef.tile_size, screenf.screenHeight-tilef.tile_size)
world.update_tile(1)
#blob_group = pygame.sprite.Group()

run = True
start_level=True
while run:
    clock.tick(60) #fps
    screenf.screen.blit(screenf.background, (0,0))
    if start_level:
        world.update_tile(1)
        start_level=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            #sys.exit()

    #screenf.draw_grid()

    world.draw()
    enemyf.blob_group.draw(screenf.screen)
    player.update()

    pygame.display.update()