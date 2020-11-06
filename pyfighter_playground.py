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
from classes.player import Player

from classes.map import Map

def pyfighter_playground():
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
    screen_dims = (config['screen_dims'])

    ### Setting up Screen and clock
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    game_display = pygame.Surface((screen_width / 1, screen_height / 1))
    pygame.display.set_caption(game_name)
    clock = pygame.time.Clock()

    ### Setting up game loop
    run_me = True

    ############################TEMP PLAYER##############################################
    # Testing Player
    player = pygame.image.load('graphics/char_idle/idler1.png')
    move_R = False
    move_L = False
    player_loc = [50, 50]
    player_gravity = 0

    tile_1 = pygame.image.load('graphics/map_tiles/tile1.png')
    tile_2 = pygame.image.load('graphics/map_tiles/tile2.png')

    game_map = Map(tile_1, tile_2, game_display)
    ##########################################################################

    while run_me:
        # Limit frame rate
        clock.tick(max_fps)

        # Get/action events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                run_me = False

           #####################TEMP PLAYER##########################################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_R = True
                if event.key == pygame.K_LEFT:
                    move_L = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_R = False
                if event.key == pygame.K_LEFT:
                    move_L = False
            ##############################################################
        # Refresh screen
        game_display.fill(colour['black'])

        ### Code to re-display items on screen will go here ###

        ############################TEMP PLAYER##################################################
        game_map.generateMap()
        game_display.blit(player, player_loc)

        if move_R == True:
            player_loc[0] += 4
        if move_L == True:
            player_loc[0] -= 4
        else:
            player_gravity += 0.2
        player_loc[1] += player_gravity

        #################################################################################

        scaled_surf = pygame.transform.scale(game_display, screen_dims)
        game_screen.blit(scaled_surf, (0, 0))
        # Flip to display
        pygame.display.flip()


pyfighter_playground()
