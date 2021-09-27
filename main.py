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
        randomDistance = random.randint(1,2) #create a reandom value to choose a distance 1; square or 2 squares


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
        contact =  pygame.sprite.spritecollideany(self, players)
        if contact:
            print(self.name, " hit ", contact.name)
            if contact.hascarrot:
                print(contact.name, "had the carrot and it is stolen!")
                self.hascarrot = True
            pygame.sprite.Sprite.kill(contact)
        if pygame.sprite.spritecollideany(self, carrot):
            print(self.name, "got the carrot!")
            self.hascarrot = True
            pygame.sprite.Sprite.kill(carrot1)
        if pygame.sprite.spritecollideany(self, mountain):
            if self.hascarrot:
                print(self.name, "brought the carrot to the mountain and won!")
                pygame.quit()
                sys.exit()


        players.add(self) #return self to players group


    # These four functions control cardinal direction movement
    def MoveUp(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(0, -100)
            distance_moved +=1
            test = pygame.sprite.spritecollideany(self, players)
            if test and self.avoid:         #create a check to avoid other players if not marvin
                self.rect.move_ip(0, 100)
                break
            if pygame.sprite.spritecollideany(self, mountain) and not self.hascarrot: #check if contact with mountain and avoid if no carrot
                self.rect.move_ip(0,100)
                break
        if (self.rect.top < 0):  # check if top of board is reached
            self.rect.top = 0  # if so set position to top of board

    def MoveDown(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(0, 100)
            distance_moved +=1
            if pygame.sprite.spritecollideany(self, players) and self.avoid :
                self.rect.move_ip(0, -100)
                break
            if pygame.sprite.spritecollideany(self, mountain) and not self.hascarrot: #check if contact with mountain and avoid if no carrot
                self.rect.move_ip(0,-100)
                break
        if (self.rect.bottom > SCREEN_HEIGHT):  # check if bottom reached
            self.rect.bottom = SCREEN_HEIGHT  # if so set position to bottom

    def MoveLeft(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(-100, 0)
            distance_moved +=1
            if pygame.sprite.spritecollideany(self, players) and self.avoid:
                self.rect.move_ip(100, 0)
                break
            if pygame.sprite.spritecollideany(self, mountain) and not self.hascarrot: #check if contact with mountain and avoid if no carrot
                self.rect.move_ip(100, 0)
                break
        if (self.rect.left < 0):
            self.rect.left = 0

    def MoveRight(self, distance):
        distance_moved = 0
        while distance_moved < distance:
            self.rect.move_ip(100, 0)
            distance_moved +=1
            if pygame.sprite.spritecollideany(self, players) and self.avoid:
                self.rect.move_ip(-100, 0)
                break
            if pygame.sprite.spritecollideany(self, mountain) and not self.hascarrot: #check if contact with mountain and avoid if no carrot
                self.rect.move_ip(-100, 0)
                break
        if (self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH
    def Spawn(self):
        self.rect.center = (random.randint(0, (SCREEN_WIDTH / 100) - 1) * 100 + 50, random.randint(0, (SCREEN_HEIGHT / 100) - 1) * 100 + 50)
        if pygame.sprite.spritecollideany(self, all_sprites):
            print("Bad spawn")
            self.Spawn()

    # def setCarrot(self, gotcarrot):
    #     self.hascarrot = gotcarrot


class BugsBunny(Toon):
    def __init__(self):
        super().__init__()
        self.name = "Bugs"
        self.hascarrot = False
        if self.hascarrot:
            self.image = pygame.image.load("Assets/bugs2.png")
        else:
            self.image = pygame.image.load("Assets/bugs2.png")
        self.rect = self.image.get_rect()
        self.avoid = True  #does the toon avoid other toons



        # randomly spawn bugs Creates a random int between 0-4 and then centers it to the midpoint of the 100 pixel sized square
        # self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Taz(Toon):
    def __init__(self):
        super().__init__()
        self.name ="Taz"
        self.hascarrot = False
        if self.hascarrot == True:
            self.image = pygame.image.load("Assets/tazcarrot.png")
        else:
            self.image = pygame.image.load("Assets/taz.png")
        self.rect = self.image.get_rect()
        self.avoid = True


    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Tweety(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/tweety.png")
        self.rect = self.image.get_rect()
        self.name = "Tweety"
        self.hascarrot = False
        self.avoid = True

        # self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Marvin(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/marvin.png")
        self.rect = self.image.get_rect()
        self.name = "Marvin"
        self.hascarrot = False
        self.avoid = False
        # self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Mountain(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/mountain.png")
        self.rect = self.image.get_rect()

        # self.Spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Carrot(Toon):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/777.png")
        self.rect = self.image.get_rect()

        # self.Spawn()

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

#carrot group:                      #single sprite group for the carrot
carrot = pygame.sprite.Group()
carrot.add(carrot1)

#mountain group:                    #single sprite group for the mountain
mountain = pygame.sprite.Group()
mountain.add(mountain1)

#spawning sprites


# Beginning Game Loop
turn_counter = 0                    #used to keep track of the number of turns
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BGColor)
    board_draw(WIDTH, HEIGHT, SCREEN_WIDTH)
    if turn_counter == 0:
        for sprite in all_sprites:  # cycle through all the sprites
            all_sprites.remove(sprite)  # remove the current sprite to prevent it from triggering contact with itself
            sprite.Spawn()  # spawn sprite
            all_sprites.add(sprite)  # return sprite to the app_sprites group
    # for sprite in all_sprites:
    #     sprite.draw(DISPLAYSURF)
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
    for player in players:
        #print("It is now ", player.name, "'s turn")
        # if player.hascarrot:
        #     print(player.name, " has the carrot")
        #else:
            #print(player.name, " is looking for the carrot")
        if player.name == "Marvin" and turn_counter%3 ==0 and turn_counter > 0:  #check to activate marvin's time-travel machine
            print("Activating Marvin's multi-dimensional time-travel machine")
            all_sprites.remove(mountain1)
            mountain1.Spawn()
            all_sprites.add(mountain1)
        players.remove(player)
        player.Move()
        players.add(player)
        pygame.time.delay(1000)
    turn_counter += 1
    print("It is turn: ", turn_counter)
    pygame.display.update()
    FramePerSec.tick(FPS)