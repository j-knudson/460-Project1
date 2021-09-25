import pygame, sys
from pygame.locals import *

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
DisplayWidth = 500   #set width; could refactor to just one pixel size
DisplayHeight = 500  #set height

DISPLAYSURF = pygame.display.set_mode((DisplayWidth, DisplayHeight))
DISPLAYSURF.fill(BGColor)
pygame.display.set_caption("Toon Board")

# Creating Lines and Shapes
#Draw board lines
WIDTH = 0
HEIGHT = 0
while WIDTH < DisplayWidth:
    pygame.draw.line(DISPLAYSURF, BLACK, (WIDTH, 0), (WIDTH, 500))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, HEIGHT), (500, HEIGHT))
    WIDTH += 100
    HEIGHT += 100

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)