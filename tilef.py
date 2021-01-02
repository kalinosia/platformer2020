import pygame
import screenf
import levelsf

class World():
    def __init__(self):
        self.tile_size = 40
        self.images = []
        for num in range(1, 17):
            image=pygame.image.load(f'img/tiles/tile/{num}.png')
            image=pygame.transform.scale(image, (self.tile_size, self.tile_size))
            self.images.append(image)

    def update_tile(self, level):

        build_tiles = []
        if level == 1:
            build_tiles = levelsf.basic_tiles

        row_count = 0
        for row in build_tiles: ###
            col_count=0
            for tile in row:
                if tile>0:
                    screenf.screen.blit(self.images[tile-1], (self.tile_size*col_count, self.tile_size*row_count))
                #elif tile == 16:
                #    screenf.screen.blit(self.tile_float_right, (self.tile_size * col_count, self.tile_size * row_count))
                col_count += 1
            row_count += 1