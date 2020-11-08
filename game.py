''' Pyfighter (working title)

A Steampunk 2D streetfighting game built with PyGame.

[ More details to go here before release :), big it up and that! ]

Produced as an MSc Computer Science project by R. Soane,
S. Mistrey and R. Danevicius
'''

### Library Imports
import pygame
import json
from classes.displaystring import DisplayString

### THESE IMPORTS ARE NEEDED IN CONTROLLER
from classes.background import Background
from classes.player import Player
from classes.npc import NPC


def pyfighterGame():
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
    screen_dims = (config['screen_dims'])  # If screen_dims halved image get scaled up by half

    ### Setting up Screen and clock
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    game_display = pygame.Surface((screen_width, screen_height))  # surface on which we blit images
    pygame.display.set_caption(game_name)
    clock = pygame.time.Clock()

    ######## Will go in controller init!

    game_background = Background(game_screen, screen_dims, 32)
    player = Player(game_screen, 600, 100)
    enemy = NPC(game_screen, 100, 100)
    enemy.addTarget(player)

    ########

    ### Setting up game loop
    run_me = True

    while run_me:
        # Limit frame rate
        clock.tick(max_fps)

        # Get/action events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                run_me = False

        # Refresh screen
        game_screen.fill(colour['blue'])

        ### Code to re-display items on screen will go here ###

        game_background.display()
        player.display()
        enemy.display()

        # Blits the scaled game_display to game_screen, move to controller when ready #
        #scaled_surf = pygame.transform.scale(game_display, screen_dims)
        #game_screen.blit(scaled_surf, (0, 0))
        ##############################################################################
        # Flip to display
        pygame.display.flip()

#### COMMENT BELOW OUT - only here for testing purposes now :)
pyfighterGame()