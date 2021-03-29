import pygame
import GameVariable

size=GameVariable.tile_size

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/cowgirl.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_dir = 1
        self.move_count = 0

    def update(self):
        self.rect.x += self.move_dir
        self.move_count += 1
        if abs(self.move_count) > 50:
            self.move_dir *= -1
            self.move_count *= -1


blob_group = pygame.sprite.Group()