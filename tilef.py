import pygame
import screenf
import levelsf

class World():
    def __init__(self):
        self.tile_size = 40
        self.tile_top_left=pygame.transform.scale(pygame.image.load('img/tiles/tile/1.png'), (self.tile_size, self.tile_size))
        self.tile_top_middle = pygame.transform.scale(pygame.image.load('img/tiles/tile/2.png'), (self.tile_size, self.tile_size))
        self.tile_top_right = pygame.transform.scale(pygame.image.load('img/tiles/tile/3.png'), (self.tile_size, self.tile_size))
        self.tile_right = pygame.transform.scale(pygame.image.load('img/tiles/tile/4.png'), (self.tile_size, self.tile_size))
        self.tile_middle = pygame.transform.scale(pygame.image.load('img/tiles/tile/5.png'), (self.tile_size, self.tile_size))
        self.tile_left = pygame.transform.scale(pygame.image.load('img/tiles/tile/6.png'), (self.tile_size, self.tile_size))
        self.tile_down_top_right = pygame.transform.scale(pygame.image.load('img/tiles/tile/7.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_down_right = pygame.transform.scale(pygame.image.load('img/tiles/tile/8.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_up_middle = pygame.transform.scale(pygame.image.load('img/tiles/tile/9.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_down_left = pygame.transform.scale(pygame.image.load('img/tiles/tile/10.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_down_top_left = pygame.transform.scale(pygame.image.load('img/tiles/tile/11.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_up_left = pygame.transform.scale(pygame.image.load('img/tiles/tile/12.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_up_right = pygame.transform.scale(pygame.image.load('img/tiles/tile/13.png'),
                                                (self.tile_size, self.tile_size))

        self.tile_float_left = pygame.transform.scale(pygame.image.load('img/tiles/tile/14.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_float_middle = pygame.transform.scale(pygame.image.load('img/tiles/tile/15.png'),
                                                (self.tile_size, self.tile_size))
        self.tile_float_right = pygame.transform.scale(pygame.image.load('img/tiles/tile/16.png'),
                                                (self.tile_size, self.tile_size))

        #img = pygame.transform.scale(img, (tile_size, tile_size))

    def update_tile(self, level):

        if level==1:
            build_tiles = levelsf.basic_tiles

        row_count = 0
        for row in build_tiles: ###
            col_count=0
            for tile in row:
                if tile == 1:
                    screenf.screen.blit(self.tile_top_left, (self.tile_size*col_count, self.tile_size*row_count))
                elif tile == 2:
                    screenf.screen.blit(self.tile_top_middle, (self.tile_size * col_count, self.tile_size * row_count))
                #elif tile == 22:    #2.png upside down
                #    screenf.screen.blit(pygame.transform.flip(self.tile_up_left, False, True), (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 3:
                    screenf.screen.blit(self.tile_top_right , (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 4:
                    screenf.screen.blit(self.tile_right, (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 5:
                    screenf.screen.blit(self.tile_middle , (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 6:
                    screenf.screen.blit(self.tile_left , (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 7:
                    screenf.screen.blit(self.tile_down_top_right, (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 8:
                    screenf.screen.blit(self.tile_down_right, (self.tile_size * col_count, self.tile_size * row_count))
                #elif tile == 88:    #8.png upside down
                #    screenf.screen.blit(pygame.transform.flip(self.tile_down_right, False, True), (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 9:
                    screenf.screen.blit(self.tile_up_middle , (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 10:
                    screenf.screen.blit(self.tile_down_left, (self.tile_size * col_count, self.tile_size * row_count))
                #elif tile == 101:  # 10.png upside down
                #    screenf.screen.blit(pygame.transform.flip(self.tile_down_left, False, True),
                #                        (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 11:
                    screenf.screen.blit(self.tile_down_top_left, (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 12:
                    screenf.screen.blit(self.tile_up_left , (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 13:
                    screenf.screen.blit(self.tile_up_right, (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 14:
                    screenf.screen.blit(self.tile_float_left , (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 15:
                    screenf.screen.blit(self.tile_float_middle, (self.tile_size * col_count, self.tile_size * row_count))
                elif tile == 16:
                    screenf.screen.blit(self.tile_float_right, (self.tile_size * col_count, self.tile_size * row_count))
                col_count += 1
            row_count += 1