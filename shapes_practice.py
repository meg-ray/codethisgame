#Set-up Game

#import libraries
import pygame
from pygame import *

#initialize pygame
pygame.init()

#create window
window_resolution = 900, 600
game_window = display.set_mode(window_resolution)
display.set_caption('Vampire Pizza')

#load assets
pizza_size = 100, 100
pizza_img = pygame.image.load('vampire.png')
pizza_surface = Surface.convert(pizza_img)
my_pizza = transform.scale(pizza_surface, (pizza_size))
game_window.blit(my_pizza, (745,455))

# This is the circle that will be commented out.
draw.circle(game_window, (255, 0, 0, 0.5), (770, 480), 25, 0)
# This is the sample rectangle that readers will remix. 
#draw.rect(game_window, (0, 255, 0, 1.0), (25, 25, 50, 25), 0)
# This is the end result of the rectangle that will be commented out. 
draw.rect(game_window, (160, 82, 45, 0.0), (740, 450, 110, 110), 5)

#Game Loop
running = True
while running: 

    #checking for and handling events
    for event in pygame.event.get(): 

        #exit loop on quit
        if event.type == QUIT: 
            running = False

    # Update the screen with what we've drawn.
    #game_window.blit(my_pizza, (745,455))
        
    #update display 
    display.update()


#Clean-up Game
pygame.quit()