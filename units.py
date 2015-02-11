import pygame, sys, random, platforms
from pygame import *

class Unit(sprite.Sprite):
    def __init__(self, x, y,  WEIGH, HIGH, image, health, vector, speed):
        self.surf = Surface((WEIGH, HIGH))
        self.start_coordinate = (x,y)
        self.rect = Rect(x, y, WEIGH, HIGH)
        self.img = image
        self.health = health
        self.onplat = False
        self.speed = speed
        self.vec = vector

    def display(self, screen):
         screen.blit(self.img, (self.rect.left, self.rect.top))


    #def die(self):
   #     pass


class Player(Unit):
    def move(self, PLATS_ARRAY):
        self.rect.top += self.vec[1]
        for plat in PLATS_ARRAY:
            if pygame.sprite.collide_rect(plat, self):
                    if self.vec[1] < 0:
                        self.rect.top = plat.rect.bottom
                        self.onplat = False
                        self.vec[1] = 0

                    elif self.vec[1] >= 0:
                            self.rect.bottom = plat.rect.top
                            self.onplat = True
                            self.vec[1] = 0


        self.rect.left += self.vec[0]*self.speed
        for plat in PLATS_ARRAY:
            if pygame.sprite.collide_rect(plat, self):


                    if self.vec[0] > 0:
                        self.rect.right = plat.rect.left

                    elif self.vec[0] < 0:
                        self.rect.left = plat.rect.right
                    if plat.direction == "left":
                        self.rect.left -= plat.speed*2
                    if plat.direction == "right":
                        self.rect.left += plat.speed*2

        self.vec[1] += 0.3

    def die(self):
        self.rect.top = self.start_coordinate[1]
        self.rect.left = self.start_coordinate[0]
        self.onplat = False

class Monster(Unit):
    def move(self, PLATS_ARRAY, player):
        self.rect.top += self.vec[1]
        if pygame.sprite.collide_rect(player, self):
            if player.vec[1] > 0:
                self.die()
            else:
                player.die()
        for plat in PLATS_ARRAY:
            if pygame.sprite.collide_rect(plat, self):
                    if self.vec[1] < 0:
                        self.rect.top = plat.rect.bottom
                        self.onplat = False
                        self.vec[1] = 0

                    elif self.vec[1] >= 0:
                            self.rect.bottom = plat.rect.top
                            self.onplat = True
                            self.vec[1] = 0


        self.rect.left += self.vec[0]*self.speed
        if pygame.sprite.collide_rect( self, player):
             if player.vec[1] > 2 and player.rect.bottom > self.rect.top:
                self.die()

             else:
                player.die()
        for plat in PLATS_ARRAY:
            if pygame.sprite.collide_rect(plat, self):


                    if self.vec[0] > 0.1:
                        self.rect.right = plat.rect.left

                    elif self.vec[0] < 0:
                        self.rect.left = plat.rect.right

                    self.vec[0] = -self.vec[0]

        self.vec[1] += 0.3

    def die(self):
        self.surf = None
        self.start_coordinate = None
        self.rect = Rect(-200,0,0,0)
        self.health = 0
        self.onplat = None
        self.speed = 0
        self.vec = [0,0]
