''' Pyfighter (working title)

A Steampunk 2D streetfighting game built with PyGame.

[ More details to go here before release :), big it up and that! ]

Produced as an MSc Computer Science project by R. Soane, S. Mistrey and
R. Danevicius

@author: R. Soane, S. Mistrey, R. Danevicius
'''

### Library Imports
import pygame
import json
from classes.text import Text

### THESE IMPORTS ARE NEEDED IN CONTROLLER
from classes.background import Background
from classes.player import Player
from classes.npc import NPC
from classes.controller import Controller


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
    # If screen_dims halved image get scaled up by half
    screen_dims = (config['screen_dims'])

    ### Setting up Screen and clock
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    # surface on which we blit images
    game_display = pygame.Surface((screen_width // 2, screen_height // 2))  
    pygame.display.set_caption(game_name)
    clock = pygame.time.Clock()

    ### Setting up game music
    # - Music code inspired by code here:
    #   https://riptutorial.com/pygame/example/24563/example-to-add-music-in-pygame
    game_background_path = 'audio/prototype.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(game_background_path)
    #pygame.mixer.music.play(-1)

    # Setup game controller
    game_controller = Controller(game_display, game_screen, screen_dims,
                                                                    colour)
    game_controller.play()

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
                pygame.mixer.music.stop()
                run_me = False

            # Pass event to game_controller
            game_controller.keyboardInput(event)

            
        # Update elements data
        game_controller.update()
        
        # Display elements on screen
        game_controller.display()

        # Flip to display
        pygame.display.flip()


# Used for testing - can run game direct from this file, bypassing the 
# start menu
if __name__ == '__main__':
    pyfighterGame()
