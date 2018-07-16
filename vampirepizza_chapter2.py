#Set-up Game

#import libraries
import pygame
from pygame import *

#initialize pygame
pygame.init()

#-----------------------------
#Define constant variables

#Define the parameters of the game window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)


#--------------------------------------------------------------
#Load Assets 


#create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')


#set up enemy imgage
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))



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

    GAME_WINDOW.blit(VAMPIRE_PIZZA, (900,400))

    display.update()

#Close Main Game Loop
#------------------------------------------------------------------------------------------------------------------------
#End of game loop

#Clean-up Game
pygame.quit()