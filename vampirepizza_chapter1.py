#Set-up Game

#import libraries
import pygame
from pygame import *

#initialize pygame
pygame.init()

#-----------------------------
#Define constant variables

#Define the parameters of the game window
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)


#--------------------------------------------------------------
#Load Assets 


#create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')


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

    display.update()

#Close Main Game Loop
#------------------------------------------------------------------------------------------------------------------------
#End of game loop

#Clean-up Game
pygame.quit()