import pygame
import screenf
import levelsf
import enemyf
import worldf

import GameVariable
tile_size = GameVariable.tile_size

class Tiles():
    def __init__(self):
        self.tile_size = tile_size
        self.images = []
        for num in range(1, 17):
            image=pygame.image.load(f'img/tiles/tile/{num}.png')
            image=pygame.transform.scale(image, (self.tile_size, self.tile_size))
            self.images.append(image)

        self.tile_list = []

    def update_tile(self, level):

        build_tiles = []
        if level == 1:
            build_tiles = levelsf.basic_tiles

        row_count = 0
        for row in build_tiles: ###
            col_count=0
            for tile in row:
                if 0 < tile < 20:
                    #screenf.screen.blit(self.images[tile-1], (self.tile_size*col_count, self.tile_size*row_count))
                    img=self.images[tile-1]
                    img_rect=img.get_rect()
                    img_rect.x=self.tile_size * col_count
                    img_rect.y=self.tile_size*row_count
                    tile=(img, img_rect)
                    self.tile_list.append(tile)
                #elif tile == 16:
                #    screenf.screen.blit(self.tile_float_right, (self.tile_size * col_count, self.tile_size * row_count))
                # NOT WORKING!!!
                elif 41 <= tile <= 46:
                    worldf.world.add(worldf.World(col_count * tile_size, row_count * tile_size, tile-41))
                elif tile == 20:
                    blob = enemyf.Enemy(col_count*tile_size, row_count*tile_size) #+15 pix for exapm
                    #from game import blob_group
                    enemyf.blob_group.add(blob)
                elif 31<=tile<= 33:
                    cactus = worldf.WorldEnemys(col_count*tile_size, row_count*tile_size, tile-31)
                    worldf.cactus_group.add(cactus)
                col_count += 1
            row_count += 1

            ## 1 - 16 is tiles      ## \platformer2020\img\tiles\Tile
            ## 20 - 30 is enemy who walk
            ## 30 - 40 is enemy who stay - cactus       ## platformer2020\img\tiles\Objects 31 32 33
            ## 40 - 50 is world tiles

    def draw(self):
        for tile in self.tile_list:
            screenf.screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screenf.screen, (255, 255, 0), tile[1], 1)