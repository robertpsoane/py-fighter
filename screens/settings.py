import pygame
import os
import json

from classes.text import Text
from classes.menu import Button
from classes.menu import Menu

SETTINGS_LOCATION = 'json/settings.JSON'
DEFAULT_LOCATION = 'json/default_settings.JSON'

# Setup menu buttons
def refreshTexts(screen):
    with open(SETTINGS_LOCATION) as settings_data:
        settings_data = json.load(settings_data)

    height = screen.get_height()
    width = screen.get_width()
    height_unit = height // 9
    left = width // 4
    right = 3 * left
    mid = width // 2

    texts = {}
    used_keys = [
        settings_data["left"],
        settings_data["right"],
        settings_data["up"],
        settings_data["attack"],
        settings_data["next_level"]
    ]

    left_str = f'Move Left : {settings_data["left"]}'
    left_text = Text(screen, (left, 2 * height_unit), 35, left_str)
    texts['left'] = left_text

    right_str = f'Move Right : {settings_data["right"]}'
    right_text = Text(screen, (left, 3 * height_unit), 35, right_str)
    texts['right'] = right_text

    jump_str = f'Jump : {settings_data["up"]}'
    jump_text = Text(screen, (left, 4 * height_unit), 35, jump_str)
    texts['up'] = jump_text

    attack_str = f'Attack : {settings_data["attack"]}'
    attack_text = Text(screen, (left, 5 * height_unit), 35, attack_str)
    texts['attack'] = attack_text

    level_str = f'Next Level : {settings_data["next_level"]}'
    level_text = Text(screen, (left, 6 * height_unit), 35, level_str)
    texts['next_level'] = level_text

    return texts, settings_data, used_keys

def resetButtons():
    with open(DEFAULT_LOCATION) as default_settings:
        default_settings = json.load(default_settings)
        with open(SETTINGS_LOCATION, 'w') as settings_json:
            json.dump(default_settings, settings_json)
    return 'reset'

def settings(screen, max_fps):
    ''' Pause Screen function

    Produces the pause screen and allows interaction with buttons.
    '''
    # Not in process of changing keybinding
    changing = (False, None)

    height = screen.get_height()
    width = screen.get_width()
    height_unit = height // 9
    left = width // 4
    right = 3 * left
    mid = width // 2
    default_button = (128, 64)
    
    texts, settings_data, used_keys = refreshTexts(screen)

    # Title
    title = Text(screen, (mid, height_unit), 40, 'Settings', 'purple')
    
    # back
    back_pos = default_button[0] + 10, height - default_button[1] - 10
    back_button = Button(screen, 'Back', back_pos, (lambda : 'back'), 20)

    # back
    reset_pos = width - back_pos[0], back_pos[1]
    reset_button = Button(screen, 'Reset', reset_pos, resetButtons, 20)

    # Left
    left_button = Button(screen, 'Change', (right, 2*height_unit), (lambda : 'left'), 20)

    # Right
    right_button = Button(screen, 'Change', (right, 3*height_unit), (lambda : 'right'), 20)

    # Jump
    jump_button = Button(screen, 'Change', (right, 4*height_unit), (lambda : 'up'), 20)

    # Attack
    attack_button = Button(screen, 'Change', (right, 5*height_unit), (lambda : 'attack'), 20)

    # Next Level
    level_button = Button(screen, 'Change', (right, 6*height_unit), (lambda : 'next_level'), 20)

    # Music
    

    # Menu
    settings_menu = Menu(screen, title, False, left_button, right_button, 
                        jump_button, attack_button, level_button, back_button,
                        reset_button)
    

    # load clock
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(max_fps)

        # Get/action events
        for event in pygame.event.get():
            # Send each event to the start menu
            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                run = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    run = False
                elif changing[0]:
                    #print(settings_data[changing[1]])
                    #print(pygame.key.name(event.key))
                    new_key = pygame.key.name(event.key)
                    if new_key not in used_keys:
                        settings_data[changing[1]] = new_key
                        with open(SETTINGS_LOCATION, 'w') as settings_json:
                            json.dump(settings_data, settings_json)
                        texts, settings_data, used_keys = refreshTexts(screen)
                        changing = (False, None)

            
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                            (event.type == pygame.MOUSEBUTTONUP):
                
                button_press = settings_menu.do(event)
                #print(button_press)
                if button_press in texts.keys():
                    
                    if button_press != changing[1]:
                        if changing[1] != None:
                            # If previously have had selection
                            texts[changing[1]].colour = 'white'
                        changing = (True, button_press)
                        texts[button_press].colour = 'red'
                    elif changing[1] == button_press:
                        # Unsets if same
                        texts[changing[1]].colour = 'white'
                        changing = (False, None)
                    
                elif button_press == 'back':
                    run = False
                elif button_press == 'reset':
                    texts, settings_data, used_keys = refreshTexts(screen)
       
        # Display Pause Menu
        screen.fill('black')

        settings_menu.display()

        for key in texts.keys():
            texts[key].display()

        pygame.display.flip()