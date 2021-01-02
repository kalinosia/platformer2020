import pygame
import math
import screenf


class Player():
    def __init__(self, x, y):  # jaka postać też?
        self.img_stay = []
        self.img_slide = []
        self.img_run = []
        self.img_jump = []
        self.img_dead = []

        # if girl Dead (2).png and girl worse because free space...
        for num in range(0, 10):
            # imahe size is 614 x 564 ,so 307,282 or ??
            # buy really this is size dead so toch is about ~250/300 [230 head] so it's 37,5% width is real width
            sizeXmg, sizeYimg = 122, 112

            img = pygame.image.load(f'img/boy/Dead__00{num}.png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))
            self.img_dead.append(img)

            img = pygame.image.load(f'img/boy/Idle__00{num}.png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))
            self.img_stay.append(img)

            img = pygame.image.load(f'img/boy/Jump__00{num}.png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))
            self.img_jump.append(img)

            img = pygame.image.load(f'img/boy/Run__00{num}.png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))
            self.img_run.append(img)

            img = pygame.image.load(f'img/boy/Slide__00{num}.png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))
            self.img_slide.append(img)
        self.index = 0
        self.image = self.img_stay[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.state = "stay"  # "stay" "run" "slide" "dead" "jump"
        self.side = 1  # prawa w prawo idze -1 lewa
        self.index_jump=0

    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.state = "slide"
            self.index = 0
        # if key[pygame.K_SPACE] and self.jumped == False and self.jumping and colision:
        #    you can jump

        if key[pygame.K_UP] and not self.state == "jump":
            self.vel_y = -15
            self.state = "jump"
            self.index = 0

        if key[pygame.K_LEFT] and not self.state == "jump":
            dx -= 5
            self.side = -1
            self.state = "run"
            if not self.state == "run":
                self.index = 0
        if key[pygame.K_LEFT] and self.state == "jump":
            self.side = -1
            dx -= 5

        if key[pygame.K_RIGHT] and not self.state == "jump":
            dx += 5
            self.side = 1
            self.state = "run"
            if not self.state== "run":
                self.index = 0
        if key[pygame.K_RIGHT] and self.state == "jump":
            self.side = 1
            dx += 5
        ##??????slide
        if key[pygame.K_DOWN] and self.state == "run" and self.side == 1:
            dx += 5
            self.side = 1
            self.index = 0
            self.state = "slide"
        if key[pygame.K_DOWN] and self.state == "run" and self.side == -1:
            dx -= 5
            self.side = -1
            self.index = 0
            self.state = "slide"

        if self.state == "run":
            if key[pygame.K_RIGHT] == False:
                if not key[pygame.K_LEFT]:
                    self.state="stay"
                    self.index=0
        '''
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and self.state == "jump":
                    self.state = "stay"
                    self.index = 0
                    
        '''

        # animation
        self.index += 1

        if self.state == "jump":
            self.index_jump+=1
            self.index=math.floor(self.index_jump/3)
            if self.index >= 10:
                self.index = 0
                self.state = "stay"
                self.index_jump=0

        if self.index >= 10:
            self.index = 0
        # slide?


        if self.state == "run" and self.side == 1:
            self.image = self.img_run[self.index]
        elif self.state == "run" and self.side == -1:
            self.image = pygame.transform.flip(self.img_run[self.index], True, False)
        elif self.state == "jump" and self.side == 1:
            self.image = self.img_jump[self.index]
        elif self.state == "jump" and self.side == -1:
            self.image = pygame.transform.flip(self.img_jump[self.index], True, False)
        elif self.state == "slide" and self.side == 1:
            self.image = self.img_slide[self.index]
        elif self.state == "slide" and self.side == -1:
            self.image = pygame.transform.flip(self.img_slide[self.index], True, False)
        elif self.state == "dead":
            self.image = self.img_dead[self.index]
        if self.state == "stay":
            self.image = self.img_stay[self.index]

        ## add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        # grawity so he must stay on ground
        if self.rect.bottom > screenf.screenHeight - (0.01 * screenf.screenHeight):
            self.rect.bottom = screenf.screenHeight - (0.01 * screenf.screenHeight)
            dy = 0

        screenf.screen.blit(self.image, self.rect)
