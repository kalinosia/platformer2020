import pygame
import math
import screenf

import GameVariable

tile_size = GameVariable.tile_size

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
            sizeXmg, sizeYimg = tile_size, tile_size

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
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.vel_y = 0
        self.state = "stay"  # "stay" "run" "slide" "dead" "jump"
        self.side = 1  # prawa w prawo idze -1 lewa
        self.index_jump=0
        self.countframe=0
        self.on_ground = False

    def update(self):
        dx = 0
        dy = 0
        if self.state != "over":

            if GameVariable.game_over == 0:

                key = pygame.key.get_pressed()
                #if key[pygame.K_SPACE]:
                    #self.state = "slide"
                #    self.index = 0
                # if key[pygame.K_SPACE] and self.jumped == False and self.jumping and colision:
                #    you can jump

                if key[pygame.K_UP] and not self.state == "jump" and self.on_ground:
                    self.vel_y = -14
                    self.state = "jump"
                    self.index = 0
                    self.on_ground = False

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
                if key[pygame.K_DOWN] and (self.state == "run" or self.state == "stay") and self.side == 1:
                    self.side = 1
                    self.index = 0
                    self.state = "slide"
                if key[pygame.K_DOWN] and (self.state == "run" or self.state == "stay") and self.side == -1:
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
            self.countframe += 1
            ##################dok
            if self.countframe > 15: #here we change how many frames have that same img
                self.index += 1
                self.countframe=0
                if self.state=="dead": dx+=1


            if GameVariable.game_over == 0:
                if self.state == "jump":
                    self.index_jump+=1
                    self.index=math.floor(self.index_jump/3)
                    if self.index >= len(self.img_jump):
                        self.index = 0
                        self.state = "stay"
                        self.index_jump = 0
                    if self.on_ground:
                        self.state = "stay"

                if self.state == "slide":
                    if self.side == 1:
                        dx += 1
                    elif self.side == -1:
                        dx -= 1
                    if self.index == len(self.img_slide):
                        self.state = "stay"

            if self.index >= len(self.img_stay):#####can change to couple
                self.index = 0
            # slide?

            if self.state == "stay" and self.side == 1:
                self.image = self.img_stay[self.index]
            elif self.state == "stay" and self.side == -1:
                self.image = pygame.transform.flip(self.img_stay[self.index], True, False)
            elif self.state == "run" and self.side == 1:
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

            if GameVariable.game_over==-1 and self.state=="dead": ################## DEAD #############
                if self.index == len(self.img_dead)-1:
                    self.state="over"
                from game import tiles
                for tile in tiles.tile_list:
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        # check if above the ground i.e. falling
                        if self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.on_ground = True
                    #if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height): #??
                    #    dx = 0

            #if GameVariable.game_over == 0:
            ## add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            if GameVariable.game_over == 0:
                #colision so he must stay on ground
                '''
                on_ground=False
                row_count = 0
                for row in levelsf.basic_tiles:  ###
                    col_count = 0
                    for tile in row:
                        if 0<tile<17:
                            if self.rect.bottom >= tile_size*row_count + 30 and self.rect.bottom <= tile_size*row_count:
                                self.rect.bottom = tile_size*row_count
                                on_ground = True
                                dy=0
                                print("brak")
                                break
                        if on_ground:
                            break
                    col_count += 1
                row_count += 1
                print(self.rect.bottom, self.rect, self.rect.top, self.rect.left)
        '''
                #####################CHANGE TILES
                #check for collision in x direction
                from game import tiles
                for tile in tiles.tile_list:
                    if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                        dx = 0
                        #self.state = "stay"
                # check for collision in y direction
                for tile in tiles.tile_list:
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        #check if below the ground i.e. jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                            #self.state = "stay"
                        # check if above the ground i.e. falling
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.state = "stay"
                            self.on_ground=True

                #check for collision with enemies (and world)##############################


                import enemyf
                if pygame.sprite.spritecollide(self, enemyf.blob_group, False):
                    GameVariable.game_over = -1
                    self.state = "dead"
                    self.index = 0
                import worldf
                if pygame.sprite.spritecollide(self, worldf.cactus_group, False):
                    GameVariable.game_over = -1
                    self.state = "dead"
                    self.index = 0
                    #print(game_over)

                # update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            #print(self.rect.y)
            # if self.rect.y>=screenf.screenHeight: game.win=True;
            # grawity so he must stay on ground
            '''
            if self.rect.bottom > screenf.screenHeight - (0.01 * screenf.screenHeight):
                self.rect.bottom = screenf.screenHeight - (0.01 * screenf.screenHeight)
                dy = 0
            '''



        screenf.screen.blit(self.image, self.rect)
        #pygame.draw.rect(screenf.screen, (255,255,255), self.rect, 2)