#Set-up Game

#import libraries
import pygame
from pygame import *
from random import randint

#initialize pygame
pygame.init()

#set up clock
clock = time.Clock() 

#-----------------------------
#Define constant variables

#Define the parameters of the game window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Define the parameters of each tile
WIDTH = 100
HEIGHT = 100

# Define some colors
WHITE = (255, 255, 255)

#Set up rates
SPAWNRATE = 360
FRAMERATE = 60

#--------------------------------------------------------------
#Load Assets 


#create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Vampire Pizza')

#set up enemy imgage
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))

#set up background image
background_img = image.load('restaurant.jpg')
background_surf = Surface.convert(background_img)
BACKGROUND = transform.scale(background_surf, (WINDOW_RES))


#---------------------------------------------
#Set up classes

#Create an enemy class
class VampireSprite(sprite.Sprite):

    #This function creates an instance of the enemy
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.lane = randint(0, 4)
        all_vampires.add(self)
        self.image = VAMPIRE_PIZZA.copy()
        y = 50 + self.lane * 100
        self.rect = self.image.get_rect(center=(1100, y))

    #This function moves the enemies from right to left and destroys them after they've left the screen
    def update(self, game_window):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed
        game_window.blit(self.image, (self.rect.x, self.rect.y))



#-------------------------------------------------------------
#Create class instances

#create a sprite group for all the VampireSprite instances
all_vampires = sprite.Group()


#--------------------------------------------------------------
# Initialize and draw Background Grid

# Populate the grid
tile_color = WHITE
for row in range(6):
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)

GAME_WINDOW.blit(BACKGROUND, (0,0))



#--------------------------------------------------------------------------------------------------------------------------------------
#Start Main Game Loop

#Game Loop
running = True
while running: 

#------------------------------------------
#Check for events

    #checking for and handling events
    for event in pygame.event.get():

        #exit loop on quit
        if event.type == QUIT: 
            running = False


#-------------------------------------------------
#Create VampireSprite instances

    if randint(1, SPAWNRATE) == 1:
        VampireSprite()


#-------------------------------------------------
#Update displays
    for vampire in all_vampires:
        vampire.update(GAME_WINDOW)

    display.update()

    #set the framerate
    clock.tick(FRAMERATE)

#Close Main Game Loop
#------------------------------------------------------------------------------------------------------------------------
#End of game loop

#Clean-up Game
pygame.quit()