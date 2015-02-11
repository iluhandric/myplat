import pygame
import sys
from pygame import *
from platforms import *
from units import *
pygame.init()

# SET DISPLAY PARAMETERS

FPS = 70
game_display = pygame.display.set_mode((800, 500))
timer = pygame.time.Clock()
pygame.display.set_caption('PICA')

# SET COLOURS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PL_COLOUR = (190, 100, 0, 70)
GREY = (90, 90, 90)
RED = (255,0,0)

# PERS PARAMETERS

### coordinate
startX = 30
startY = 30
###
speed = 3
jump_high = 7

# GRAVITY PARAMETERS
onPlat = False
left = right = jump = False
gravitation = 0.9
time_fly = 0



class VectorSpeed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

dino_vec = VectorSpeed(4,0)
pers_vec = VectorSpeed(0,0)

player = Player(startX, startY,  31, 39, pygame.image.load('C:/pica.jpg'), 3, [0, 0], 3)

dino = Monster(400, 400, 50, 43, pygame.image.load('C:/dino.gif'), 3, [4, 0], 1)

def motion( unit):

    if event.type == KEYDOWN:
                    if (event.key == K_LEFT or event.key == K_a):
                        unit.vec[0] = -1
                    elif (event.key == K_RIGHT or event.key == K_d):
                        unit.vec[0] = 1
                    elif (event.key == K_UP or event.key == K_w) and unit.onplat:
                        unit.onplat = False
                        unit.vec[1] = -jump_high
    if event.type == KEYUP:
                    if (event.key == K_LEFT or event.key == K_a) or (event.key == K_RIGHT or event.key == K_d):
                        unit.vec[0] = 0
#    #if unit.vec[0] != 0 and

# PLATFORMS:

PLATS_ARRAY = []

GROUND = platforms.plat( 0, 370, 800, 400, (50, 150, 50), False, "", 0)    #

pl3 = plat(100, 310, 80, 60, PL_COLOUR, False, "", 0)
pl4 = plat(400, 230, 80, 70, PL_COLOUR, False, "", 0)
pl5 = plat(400, 120, 80, 30, PL_COLOUR, False, "", 0)
pl2 = plat(310, 200, 80, 30, PL_COLOUR, False, "", 0)
pl1 = plat(250, 290, 80, 30, PL_COLOUR, False, "", 0)
pl6 = plat(630, 100, 10, 600, PL_COLOUR, False, "", 0)
pl7 = plat(470, 260, 10, 110, PL_COLOUR, False, "", 0)

leftWall = plat(0, 0, 10, 370, PL_COLOUR, False, "", 0)
rightWall = plat(790, 0, 10, 320, PL_COLOUR, False, "", 0)
roof = plat(0, 0, 800, 10, PL_COLOUR, False, "", 0)

moving1 = plat(550, 200, 80, 80, GREY, False, "up", -2)
moving11 = plat(550, 300, 80, 80, GREY, False, "up", -5)

teleport = plat(540, 0, 100, 10, RED, True, "", 0)
respawn = plat(0, 10, 10, 60, WHITE, False, "", 0)

PLATS_ARRAY.append(GROUND)
PLATS_ARRAY.append(pl1)
PLATS_ARRAY.append(pl2)
PLATS_ARRAY.append(pl3)
PLATS_ARRAY.append(pl4)
PLATS_ARRAY.append(pl5)
PLATS_ARRAY.append(rightWall)
PLATS_ARRAY.append(leftWall)
PLATS_ARRAY.append(roof)
PLATS_ARRAY.append(moving1)
#PLATS_ARRAY.append(moving11)
PLATS_ARRAY.append(teleport)
PLATS_ARRAY.append(respawn)
PLATS_ARRAY.append(pl6)
PLATS_ARRAY.append(pl7)
                               #


def move_plats(PLATS_ARRAY):
    for pl in PLATS_ARRAY:
        pl.move()





###
###### START UPDATING DISPLAY ########


while 99 != 63:
    timer.tick(FPS)   # CONTROL FPS

    for event in pygame.event.get():  # CHECK CLOSING
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_r:
                    player.die()
                
    game_display.fill(WHITE)  # FILLING BG                                           ### WHITE ###

    player.display(game_display)  # DISPLAYING PERS
    dino.display(game_display)
    for plat in PLATS_ARRAY: #  DISPLAY PLATFORMS
        plat.display(game_display)
    
    pygame.display.update()  # UPDATING

# MOVING PERS ACCORDING TO MOTION() FUNCTION
    motion(player)
    player.move(PLATS_ARRAY)
    if dino.surf != None:
        dino.move(PLATS_ARRAY, player)
# # #  MOVE PLATFORMS
    if PLATS_ARRAY[9].rect.top == -50:
        PLATS_ARRAY[9].rect.top = 550
    if PLATS_ARRAY[9].rect.left == 50 or PLATS_ARRAY[9].rect.left == 600:
        PLATS_ARRAY[9].speed = -PLATS_ARRAY[9].speed

# # DEATH

    if player.rect.left < 0 or player.rect.left > 800 or player.rect.top > 500 or player.rect.top < 0:
        player.die()
    for plat in PLATS_ARRAY:
        if pygame.sprite.collide_rect(plat, player):
                if plat.death:
                    player.die()

    move_plats(PLATS_ARRAY)
