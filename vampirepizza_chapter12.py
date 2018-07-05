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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Set up rates
FRAMERATE = 60
SPAWNRATE = 360

#Set up counters
STARTING_BUCKS = 15
BUCK_RATE = 120
BUCK_BOOSTER = 1

#Define speeds
REG_SPEED = 2
SLOW_SPEED = 1

#--------------------------------------------------------------
#Load Assets 


#create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Vampire Pizza')

#set up background image
background_img = image.load('restaurant.jpg')
background_surf = Surface.convert(background_img)
BACKGROUND = transform.scale(background_surf, (WINDOW_RES))

#set up enemy imgage
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))

# tile trap images
garlic_img = image.load('garlic.jpg')
garlic_surf = Surface.convert(garlic_img)
GARLIC = transform.scale(garlic_surf, (WIDTH, HEIGHT))
GARLIC.set_alpha(127)
cutter_img = image.load('pizzacutter.png')
cutter_surf = Surface.convert(cutter_img)
CUTTER = transform.scale(cutter_surf, (WIDTH, HEIGHT))
CUTTER.set_alpha(127)
pepperoni_img = image.load('pepperoni.jpg')
pepperoni_surf = Surface.convert(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (WIDTH, HEIGHT))
PEPPERONI.set_alpha(127)

#---------------------------------------------
#Set up classes

#Create an enemy class
class VampireSprite(sprite.Sprite):

    #This function creates an instance of the enemy
    def __init__(self):
        super(VampireSprite, self).__init__()
        self.speed = REG_SPEED
        self.lane = randint(0, 4)
        all_vampires.add(self)
        self.image = VAMPIRE_PIZZA.copy()
        y = 50 + self.lane * 100
        self.rect = self.image.get_rect(center=(950, y))
        self.health = 150

    #This function moves the enemies from right to left and destroys them after they've left the screen
    def update(self, game_window, counters):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed
        if self.health <= 0 or self.rect.x <= 100:
            self.kill()

        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

    def attacked_by(self, tile):
        if tile.trap == SLOW:
            self.speed = SLOW_SPEED
        if tile.trap == DAMAGE:
            self.health -= 1

class Counters:

    def __init__(self, pizza_bucks, buck_rate, buck_booster):
        self.loop_count = 0
        self.display_font = pygame.font.Font('pizza-font.ttf', 25)
        self.pizza_bucks = pizza_bucks
        self.buck_rate = buck_rate
        self.buck_booster = buck_booster
        self.bucks_rect = None

    def increment_bucks(self):
        if self.loop_count % self.buck_rate == 0:
            self.pizza_bucks += self.buck_booster

    def draw_bucks(self, game_window):
        if bool(self.bucks_rect):
            game_window.blit(BACKGROUND, (self.bucks_rect.x, self.bucks_rect.y), self.bucks_rect)
        bucks_surf = self.display_font.render(str(self.pizza_bucks), True, WHITE)
        self.bucks_rect = bucks_surf.get_rect()
        self.bucks_rect.x = WINDOW_WIDTH - 50
        self.bucks_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(bucks_surf, self.bucks_rect)

    def update(self, game_window):
        self.loop_count += 1
        self.increment_bucks()
        self.draw_bucks(game_window)


#Set up the different kinds of traps
class Trap(object):

    def __init__(self, trap_kind, cost, trap_img):
        self.trap_kind = trap_kind
        self.cost = cost
        self.trap_img = trap_img


class TrapApplicator(object):

    def __init__(self):
        self.selected = None

    def select_trap(self, trap):
        if trap.cost <= counters.pizza_bucks:
            self.selected = trap

    def select_tile(self, tile, counters):
        self.selected = tile.set_trap(self.selected, counters)


#Create a class of sprites. Each tile has an invisible interactive field attached to it which is a sprite in this class. 
class BackgroundTile(sprite.Sprite):

    def __init__(self):
        super(BackgroundTile, self).__init__()
        self.trap = None

class PlayTile(BackgroundTile):

    def set_trap(self, trap, counters):
        if bool(trap) and not bool(self.trap):
            counters.pizza_bucks -= trap.cost
            self.trap = trap
            if trap == EARN:
                counters.buck_booster += 1
        return None

    def draw_trap(self, game_window, trap_applicator):
        if bool(self.trap):
            game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))


class ButtonTile(BackgroundTile):

    def set_trap(self, trap, counters):
        if counters.pizza_bucks >= self.trap.cost:
            return self.trap
        return trap

    def draw_trap(self, game_window, trap_applicator):
        if bool(trap_applicator.selected) and trap_applicator.selected == self.trap:
            game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))

class InactiveTile(BackgroundTile):

    def set_trap(self, trap, counters):
        return trap

    def draw_trap(self, game_window, trap_applicator):
        pass


#-------------------------------------------------------------
#Create class instances

#create a sprite group for all the VampireSprite instances
all_vampires = sprite.Group()

counters = Counters(STARTING_BUCKS, BUCK_RATE, BUCK_BOOSTER)

SLOW = Trap('SLOW', 5, GARLIC)
DAMAGE = Trap('DAMAGE', 3, CUTTER)
EARN = Trap('EARN', 7, PEPPERONI)

trap_applicator = TrapApplicator()


#--------------------------------------------------------------
# Initialize and draw Background Grid

# Create an empty list to hold the tile grid
tile_grid = []
# Populate the grid
tile_color = WHITE
for row in range(6):
    row_of_tiles = []
    tile_grid.append(row_of_tiles)
    for column in range(11):
        if column <= 1:
            new_tile = InactiveTile()
        else:
            if row == 5:
                if 1 < column < 5:
                    new_tile = ButtonTile()
                    new_tile.trap = [SLOW, DAMAGE, EARN][column - 2]
                else:
                    new_tile = InactiveTile()
            else:
                new_tile = PlayTile()
        new_tile.rect = pygame.Rect(WIDTH * column, HEIGHT * row, WIDTH, HEIGHT)
        row_of_tiles.append(new_tile)
        if row == 5 and 1 < column < 5:
            BACKGROUND.blit(new_tile.trap.trap_img, (new_tile.rect.x, new_tile.rect.y))
        if column != 0 and row != 5:
            if column != 1: 
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

        #Set up the background tiles to respond to a mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            trap_applicator.select_tile(tile_grid[y // 100][x // 100], counters)


#-------------------------------------------------
#Create VampireSprite instances

    if randint(0, SPAWNRATE) == 1:
        VampireSprite()

#------------------------------------------------
#Set up collision detection

    #draw the background grid
    for tile_row in tile_grid:
        for tile in tile_row:
            if bool(tile.trap):
                GAME_WINDOW.blit(BACKGROUND, (tile.rect.x, tile.rect.y), tile.rect)

    #set up collision detection
    for vampire in all_vampires:
        tile_row = tile_grid[vampire.rect.y // 100]
        vampire_left_side_x = vampire.rect.x // 100
        vampire_right_side_x = (vampire.rect.x + vampire.rect.width) // 100
        if -1 < vampire_left_side_x < 10:
            left_tile = tile_row[vampire_left_side_x]
        else:
            left_tile = None
        if -1 < vampire_right_side_x < 10:
            right_tile_wall = tile_row[vampire_right_side_x]
        else:
            right_tile = None
        if bool(left_tile):
            vampire.attacked_by(left_tile)
        if bool(right_tile) and right_tile.x != left_tile.x:
            vampire.attacked_by(right_tile)


#-------------------------------------------------
#Update displays
    for vampire in all_vampires:
        vampire.update(GAME_WINDOW, counters)

    for tile_row in tile_grid:
        for tile in tile_row:
            tile.draw_trap(GAME_WINDOW, trap_applicator)

    counters.update(GAME_WINDOW)
    display.update()

    #set the framerate
    clock.tick(FRAMERATE)

#Close Main Game Loop
#------------------------------------------------------------------------------------------------------------------------
#End of game loop

#Clean-up Game
pygame.quit()