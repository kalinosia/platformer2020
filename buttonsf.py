import pygame

#  < a href = 'https://www.freepik.com/vectors/icons' > Icons vector created by rawpixel.com - www.freepik.com < / a >
import screenf

restart_img = pygame.transform.scale(pygame.image.load('buttons/1425569252372.png'), (217, 60))

class Buttons():
    def __init__(self, x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            print("mouse")
            '''if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            
            
     if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
   '''
        screenf.screen.blit(self.image, self.rect)