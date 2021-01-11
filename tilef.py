import pygame
import screenf
import levelsf
import enemyf

tile_size = 40 # <---------

class World():
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
                elif tile == 20:
                    blob = enemyf.Enemy(col_count*tile_size, row_count*tile_size)
                    #from game import blob_group
                    enemyf.blob_group.add(blob)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screenf.screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screenf.screen, (255, 255, 0), tile[1], 1)