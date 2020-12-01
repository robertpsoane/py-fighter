''' Pyfighter (working title)

A Steampunk 2D streetfighting game built with PyGame.

[ More details to go here before release :), big it up and that! ]

Produced as an MSc Computer Science project by R. Soane, 
S. Mistrey and R. Danevicius

########################################################################

This file forms a start menu for the game.  When selected, the game 
function is loaded as a new instance of pygame within the same window.  
Implemented in this way so that whenever the player quits the game, it 
goes back to the menu.

'''

### Library Imports
import pygame
import json
from game import pyfighterGame
from classes.menu import StartMenu
from classes.menu import Button
from classes.text import Text

### Important Game Variables from JSON
with open('json/config.JSON') as config_file:
    config = json.load(config_file)

# Colour tuples and font sizes
colour = config['colour']
font_size = config['font_size']

# Important screen variables
screen_width = config['screen_dims'][0]
screen_height = config['screen_dims'][1]
max_fps = config['max_fps']
game_name = config['game_name']

### Setting up Screen and clock
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)
clock = pygame.time.Clock()

### Setting Icon
logo_image = pygame.image.load(config['logo_location'])
pygame.display.set_icon(logo_image)

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
title_obj = Text(menu_screen, (midpoint, height_unit),
                        font_size['title'], menu_title, 'purple')
play_obj = Text(menu_screen, (midpoint, 3*height_unit,),
                        font_size['subtitle'], option_1, colour['white'])
help_obj = Text(menu_screen, (midpoint, 5*height_unit),
                        font_size['subtitle'], option_2, colour['white'])
# quit_obj = Text(menu_screen, (midpoint, 7*height_unit),
#                        font_size['subtitle'], option_3, colour['white'])

quit_obj = Button(menu_screen, 'test', (midpoint, 7*height_unit), print)

# Initialising StartMenu class
start_menu = StartMenu(menu_screen, title_obj, play_obj, help_obj,
                                            quit_obj, pyfighterGame)

### Main Game Loop
while start_menu.playing:
    # Limit frame rate
    clock.tick(max_fps)

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
    menu_screen.fill(colour['black'])

    ### Code to re-display items on screen will go here
    start_menu.display()

    # Display everything on screen
    pygame.display.flip()

