''' Pyfighter (working title)

A Steampunk 2D streetfighting game built with PyGame.

[ More details to go here before release :), big it up and that! ]

Produced as an MSc Computer Science project by R. Soane, 
S. Mistrey and R. Danevicius
'''

### Library Imports
import pygame
import json


### Important Game Variables
# Colours
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255


# Setting up screen variables
screen_height, screen_width = 500, 700
game_name = 'PyFighter (working title)'
fps = 60

'''
Note - The above variables could eventually be dumped in a JSON and loaded
on loading of the program.  Could make the code look neater :)
'''


### Setting up Screen and clock
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)
clock = pygame.time.Clock()


### Setting up game loop
run_me = True

while run_me:
    # Limit frame rate
    clock.tick(fps)

    # Get/action events
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            # Detecting user pressing quit button, if X pressed,
            # break loop and quit screen.
            run_me = False
        
        

    # Refresh screen
    game_screen.fill(black)

    ### Code to re-display items on screen will go here

