''' Pyfighter (working title)

A Steampunk 2D streetfighting game built with PyGame.

[ More details to go here before release :), big it up and that! ]

Produced as an MSc Computer Science project by R. Soane, 
S. Mistrey and R. Danevicius

##############################################################################

This file forms a start menu for the game.  When selected, the game function 
is loaded as a new instance of pygame within the same window.  Implemented in
this way so that whenever the player quits the game, it goes back to the menu.

'''

### Library Imports
import pygame
import json
from game import pyfighterGame
from classes.menu import StartMenu
from classes.displaystring import DisplayString

### Important Game Variables
# Colours
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# Setting up screen variables
screen_height, screen_width = 700, 900
game_name = 'PyFighter'
fps = 60

# Font Size Data
title_size = 70
subtitle_size = 40
text_size = 15
'''
Note - The above variables could eventually be dumped in a JSON and loaded
on loading of the program.  Could make the code look neater :)
'''

### Setting up Screen and clock
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)
clock = pygame.time.Clock()


### Setting up Menu objects
# String names
menu_title = game_name
option_1 = '[1] Play Game'
option_2 = '[2] Help'
option_3 = '[3] Quit'

# Calculating (x,y) coords of strings
midpoint = screen_width // 2
height_unit = screen_height // 9

# Creating pygame string objects
title_obj = DisplayString(menu_screen, midpoint, height_unit, title_size,
                        menu_title, green)
play_obj = DisplayString(menu_screen, midpoint, 3*height_unit, subtitle_size, 
                        option_1, white)
help_obj = DisplayString(menu_screen, midpoint, 5*height_unit, subtitle_size, 
                        option_2, white)
quit_obj = DisplayString(menu_screen, midpoint, 7*height_unit, subtitle_size, 
                        option_3, white)

# Initialising StartMenu class
start_menu = StartMenu(menu_screen, title_obj, play_obj, help_obj, quit_obj,
                        pyfighterGame)


### Setting up game loop

while start_menu.playing:
    # Limit frame rate
    clock.tick(fps)

    # Get/action events
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            # Detecting user pressing quit button, if X pressed,
            # break loop and quit screen.
            start_menu.playing = False
        
        if event.type == pygame.KEYDOWN:
            # If key pressed, start menu to action chosen option.
            start_menu.do(event.unicode)
        
        
    # Refresh screen
    menu_screen.fill(black)


    ### Code to re-display items on screen will go here
    start_menu.display()

    # Display everything on screen
    pygame.display.flip()

