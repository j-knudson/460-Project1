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
        randomDistance = random.randint(1,2) #create a reandom value to choose a distance 1 square or 2 squares

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
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(0, -100)
            distance_moved +=1
        if (self.rect.top < 0):  # check if top of board is reached
            self.rect.top = 0  # if so set position to top of board

    def MoveDown(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(0, 100)
            distance_moved +=1
        if (self.rect.bottom > SCREEN_HEIGHT):  # check if bottom reached
            self.rect.bottom = SCREEN_HEIGHT  # if so set position to bottom

    def MoveLeft(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(-100, 0)
            distance_moved +=1
        if (self.rect.left < 0):
            self.rect.left = 0

    def MoveRight(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(100, 0)
            distance_moved +=1
        if (self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH
    def Spawn(self):
        self.rect.center = (random.randint(0, (SCREEN_WIDTH / 100) - 1) * 100 + 50, random.randint(0, (SCREEN_HEIGHT / 100) - 1) * 100 + 50)
        if pygame.sprite.spritecollideany(self, all_sprites):
            print("Bad spawn")
            self.Spawn
        # if pygame.sprite.spritecollide(players, all_sprites)
        #     self.Spawn



class BugsBunny(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/bugs2.png")
        self.rect = self.image.get_rect()

        # randomly spawn bugs Creates a random int between 0-4 and then centers it to the midpoint of the 100 pixel sized square
        self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Taz(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/taz.png")
        self.rect = self.image.get_rect()

        self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Tweety(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/tweety.png")
        self.rect = self.image.get_rect()

        self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Marvin(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/marvin.png")
        self.rect = self.image.get_rect()

        self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Mountain(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/mountain.png")
        self.rect = self.image.get_rect()

        self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Carrot(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/777.png")
        self.rect = self.image.get_rect()

        self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


all_sprites = pygame.sprite.Group()


#creating sprites
bugsbunny1 = BugsBunny()
taz1 = Taz()
tweety1 = Tweety()
marvin1 = Marvin()
carrot1 = Carrot()
mountain1 = Mountain()

#creating sprite groups

#players: toons that have turns
players = pygame.sprite.Group()
players.add(bugsbunny1)
players.add(taz1)
players.add(tweety1)
players.add(marvin1)

#all sprites: all created toons
all_sprites.add(bugsbunny1)
all_sprites.add(taz1)
all_sprites.add(tweety1)
all_sprites.add(marvin1)
all_sprites.add(carrot1)
all_sprites.add(mountain1)

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    bugsbunny1.Move()
    taz1.Move()
    DISPLAYSURF.fill(BGColor)
    board_draw(WIDTH, HEIGHT, SCREEN_WIDTH)
    # bugsbunny1.draw(DISPLAYSURF)
    # taz1.draw(DISPLAYSURF)
    # tweety1.draw(DISPLAYSURF)
    # marvin1.draw(DISPLAYSURF)
    # carrot1.draw(DISPLAYSURF)
    # mountain1.draw(DISPLAYSURF)
    for sprite in all_sprites:
        sprite.draw(DISPLAYSURF)

    pygame.display.update()
    pygame.time.delay(500)
    FramePerSec.tick(FPS)