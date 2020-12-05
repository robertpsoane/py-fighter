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
import os
import webbrowser
import json
import pygame
from screens.game import pyfighterGame
from classes.menu import Menu
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

menu_background = config['start_menu_background']
menu_background_path = config['menu_music']

### Setting up Menu
# Menu Functions - These functions are passed into each menu button
def playGame():
    pyfighterGame()
    playMusic(menu_background_path)

def playMusic(music_path):
    ### Setting up game music
    # - Music code inspired by code here:
    #   https://riptutorial.com/pygame/example/24563/example-to-add-music-in-pygame
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)

def getHelp():
    webbrowser.open('https://sites.google.com/view/pyfighter/home',
                            new=2)

def quitGame():
    pygame.quit()
    os._exit(0)

# String names
menu_title = game_name
play_text = 'Play'
help_text = 'Help'
quit_text = 'Quit'

# Title position
title_x = screen_width // 2
title_y = screen_height // 9
# Calculating (x,y) coords of buttons
width_unit = screen_width // 6
height_unit = screen_height // 2

# Creating pygame string objects
title_obj = Text(menu_screen, (title_x, title_y),
                        font_size['title'], menu_title, 'purple')

play_button = Button(menu_screen, play_text, 
                    (1 * width_unit, height_unit,), playGame)

help_button = Button(menu_screen, help_text, 
                    (3 * width_unit, height_unit,), getHelp)

quit_button = Button(menu_screen, quit_text, 
                    (5 * width_unit, height_unit), quitGame)

# Initialising StartMenu class
start_menu = Menu(menu_screen, title_obj, menu_background, play_button, 
                                                help_button, quit_button)

# Start Music
playMusic(menu_background_path)


### Main Game Loop
while start_menu.playing:
    # Limit frame rate
    clock.tick(max_fps)

    # Get/action events
    for event in pygame.event.get():
        # Send each event to the start menu
        start_menu.do(event)
        
    # Refresh screen
    menu_screen.fill(colour['black'])

    ### Code to re-display items on screen will go here
    start_menu.display()

    # Display everything on screen
    pygame.display.flip()

quitGame()


