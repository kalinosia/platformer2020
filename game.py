import pygame
from pygame.locals import *
import time
import GameVariable

import screenf
import playerf
import tilef
import levelsf
import enemyf
import worldf

pygame.init()
clock = pygame.time.Clock()

tiles = tilef.Tiles()
player = playerf.Player(tilef.tile_size, screenf.screenHeight-tilef.tile_size)
tiles.update_tile(1)
#blob_group = pygame.sprite.Group()

win = False

run = True
start_level=True
while run:
    clock.tick(60) #fps
    screenf.screen.blit(screenf.background, (0,0))
    if start_level:
        tiles.update_tile(1)
        start_level = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            #sys.exit()

    #screenf.draw_grid()

    tiles.draw()

    enemyf.blob_group.draw(screenf.screen)
    if GameVariable.game_over==0:
        enemyf.blob_group.update()
    worldf.cactus_group.draw(screenf.screen)
    worldf.world.draw(screenf.screen)
    player.update()

    pygame.display.update()