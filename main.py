import pygame, sys
from pygame.locals import *
import random

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Yellow = (255,255,102)

BGColor = Yellow #set background color to yellow

# Setup a 500x500 pixel display with caption
SCREEN_WIDTH = 500   #set width; could refactor to just one pixel size
SCREEN_HEIGHT = 500  #set height

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BGColor)
pygame.display.set_caption("Toon Board")

# Creating Lines and Shapes
#Draw board lines
WIDTH = 0
HEIGHT = 0
def board_draw(Width, Height, Screen_Width):
    while Width < Screen_Width:
        pygame.draw.line(DISPLAYSURF, BLACK, (Width, 0), (Width, 500))
        pygame.draw.line(DISPLAYSURF, BLACK, (0, Height), (500, Height))
        Width += 100
        Height += 100

class Toon(pygame.sprite.Sprite):

    def Move(self):

        randomDirection = random.randint(0,8) #create a random value to choose a direction
        randomDistance = random.randint(1,2) #create a reandom value to choose a distance

        #create a series of if statements to determine 1 or more directions for the toon to move
        if randomDirection == 1:
            self.MoveUp(randomDistance)
        if randomDirection == 2:
            self.MoveDown(randomDistance)
        if randomDirection == 3:
            self.MoveRight(randomDistance)
        if randomDirection == 4:
            self.MoveLeft(randomDistance)
        if randomDirection == 5:
            self.MoveUp(randomDistance)
            randomDistance = random.randint(1, 2)
            self.MoveRight(randomDistance)
        if randomDirection == 6:
            self.MoveUp(randomDistance)
            randomDistance = random.randint(1, 2)
            self.MoveLeft(randomDistance)
        if randomDirection == 7:
            self.MoveDown(randomDistance)
            randomDistance = random.randint(1, 2)
            self.MoveRight(randomDistance)
        if randomDirection == 8:
            self.MoveDown(randomDistance)
            randomDistance = random.randint(1, 2)
            self.MoveLeft(randomDistance)

    # These four functions control cardinal direction movement
    def MoveUp(self, distance):
        self.rect.move_ip(0, -100 * distance)
        if (self.rect.top < 0):  # check if top of board is reached
            self.rect.top = 0  # if so set position to top of board

    def MoveDown(self, distance):
        self.rect.move_ip(0, 100 * distance)
        if (self.rect.bottom > SCREEN_HEIGHT):  # check if bottom reached
            self.rect.bottom = SCREEN_HEIGHT  # if so set position to bottom

    def MoveLeft(self, distance):
        self.rect.move_ip(-100 * distance, 0)
        if (self.rect.left < 0):
            self.rect.left = 25

    def MoveRight(self, distance):
        self.rect.move_ip(100 * distance, 0)
        if (self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH - 25

class BugsBunny(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/bugs2.png")
        self.rect = self.image.get_rect()

        # randomly spawn bugs Creates a random int between 0-4 and then centers it to the midpoint of the 100 pixel sized square
        self.rect.center = (random.randint(0, (SCREEN_WIDTH/100)-1)*100+50, random.randint(0, (SCREEN_HEIGHT/100)-1)*100+50)
    # def move(self):
    #     self.rect.move_ip(0, 10)
    #     if (self.rect.bottom > 600):
    #         self.rect.top = 0
    #         self.rect.center = (random.randint(0, 4)*100+50, random.randint(0, 4)*100+50)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#creating sprites
bugsbunny1 = BugsBunny()

#creating sprite groups
# players = pygame.sprite.group()
# players.add(bugsbunny1)


# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    bugsbunny1.Move()
    DISPLAYSURF.fill(BGColor)
    board_draw(WIDTH, HEIGHT, SCREEN_WIDTH)
    bugsbunny1.draw(DISPLAYSURF)
    pygame.display.update()
    pygame.time.delay(500)
    FramePerSec.tick(FPS)