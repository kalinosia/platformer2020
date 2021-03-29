import pygame
import GameVariable

size=GameVariable.tile_size


class WorldEnemys(pygame.sprite.Sprite):
    def __init__(self, x, y, index):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]

        self.images.append(pygame.image.load('img/tiles/objects/Cactus (1).png'))
        self.images.append(pygame.image.load('img/tiles/objects/Cactus (2).png'))
        self.images.append(pygame.image.load('img/tiles/objects/Cactus (3).png'))

        self.index=index
        self.image=self.images[self.index]

        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_dir = 1
        self.move_count = 0

cactus_group=pygame.sprite.Group()


class World(pygame.sprite.Sprite):
    def __init__(self, x, y, index):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/Bush (1).png'), (size, size)))
        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/Bush (2).png'), (size, size)))
        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/Grass (1).png'), (size, size)))
        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/Grass (2).png'), (size, size)))
        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/SignArrow.png'), (size, size)))
        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/Tree.png'), (3*size, 3*size)))

        self.index = index
        self.image = self.images[self.index]

        #self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_dir = 1
        self.move_count = 0


world = pygame.sprite.Group()

'''
self.images = []

        self.images.append(pygame.transform.scale(pygame.image.load('img/tiles/objects/Bush (1).png'), (size, size)))
        self.images.append(pygame.image.load('img/tiles/objects/Bush (2).png'))
        self.images.append(pygame.image.load('img/tiles/objects/Grass (1).png'))
        self.images.append(pygame.image.load('img/tiles/objects/Grass (2).png'))
        self.images.append(pygame.image.load('img/tiles/objects/SignArrow.png'))
        self.images.append(pygame.image.load('img/tiles/objects/Tree.png'))

    #def update(self):
    #    screenf.screen.blit(self.images[tile - 41], (tile_size * col_count, tile_size * row_count))
    #    print("Done")

    #index = 0
    #image = images[index]

    #image = pygame.transform.scale(self.image, (size, size))

    

'''