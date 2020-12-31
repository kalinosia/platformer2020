import pygame

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Platformer")

background = pygame.image.load('img/tiles/BG.png').convert() #conxert to faster work?
background = pygame.transform.scale(background, (screenWidth, screenHeight))

'''
tile_size=40
def draw_grid():
    for line in range(0, 24):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screenWidth, line * tile_size))
    for line in range(0, 32):
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screenHeight))
'''