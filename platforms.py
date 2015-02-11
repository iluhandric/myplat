import pygame, sys, random, platforms
from pygame import *
pygame.init()

class plat(sprite.Sprite):
    def __init__(self, x, y,  WEIGH, HIGH, COLOR, bool, direction_str, speed):
        self.filled = Surface((WEIGH, HIGH))
        self.rect = Rect(x, y, WEIGH, HIGH)
        self.filled.fill((COLOR))
        self.death = bool
        self.direction = direction_str
        self.speed = speed
    def display(self, screen):
         screen.blit(self.filled, (self.rect.left, self.rect.top))
    def move(self):
        if self.direction == "up":
            self.rect.top += self.speed
        elif self.direction == "down":
                self.rect.top -= self.speed
        elif self.direction == "left":
            self.rect.right += self.speed
        elif self.direction == "right":
            self.rect.right += self.speed
