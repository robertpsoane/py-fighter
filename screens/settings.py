import pygame
import os
import json

from classes.text import Text
from classes.menu import Button
from classes.menu import Menu


# Setup menu buttons
def changeLeft():
    pass

def changeRight():
    pass

def changeJump():
    pass

def changeAttack():
    pass

def changeNext():
    pass


def settings(screen, max_fps):
    ''' Pause Screen function

    Produces the pause screen and allows interaction with buttons.
    '''

    with open('json/settings.JSON') as settings_data:
        settings_data = json.load(settings_data)

    height = screen.get_height()
    width = screen.get_width()
    height_unit = height // 9
    left = width // 4
    right = 3 * left
    mid = width // 2

    texts = []

    # Title
    title = Text(screen, (mid, height_unit), 40, 'Settings', 'purple')
    
    # Left
    left_str = f'Move Left : {settings_data["left"]}'
    left_text = Text(screen, (left, 2 * height_unit), 35, left_str)
    texts.append(left_text)
    left_button = Button(screen, 'Change', (right, 2*height_unit), changeLeft, 20)

    # Right
    right_str = f'Move Right : {settings_data["right"]}'
    right_text = Text(screen, (left, 3 * height_unit), 35, right_str)
    texts.append(right_text)
    right_button = Button(screen, 'Change', (right, 3*height_unit), changeRight, 20)

    # Jump
    jump_str = f'Move jump : {settings_data["up"]}'
    jump_text = Text(screen, (left, 4 * height_unit), 35, jump_str)
    texts.append(jump_text)
    jump_button = Button(screen, 'Change', (right, 4*height_unit), changeJump, 20)

    # Attack
    attack_str = f'Attack : {settings_data["attack"]}'
    attack_text = Text(screen, (left, 5 * height_unit), 35, attack_str)
    texts.append(attack_text)
    attack_button = Button(screen, 'Change', (right, 5*height_unit), changeAttack, 20)

    # Next Level
    level_str = f'Next Level : {settings_data["next_level"]}'
    level_text = Text(screen, (left, 6 * height_unit), 35, level_str)
    texts.append(level_text)
    level_button = Button(screen, 'Change', (right, 6*height_unit), changeNext, 20)

    # Music
    

    # Menu
    settings_menu = Menu(screen, title, False, left_button, right_button, jump_button, attack_button, level_button)
    

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
            elif (event.type == pygame.KEYDOWN) and \
                        (event.key == pygame.K_ESCAPE):
                run = False
            
            # Here, we check whether the player has clicked the mouse,
            # if they have, we pass the click into the pause menu and it 
            # processes the click.  The button function returns a string
            # 'resume' for resume game, or 'main_menu' to quit to main
            # menu.
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                            (event.type == pygame.MOUSEBUTTONUP):
                button_press = settings_menu.do(event)
                #print(button_press)
                if button_press == 'resume':
                    paused = False
                elif button_press == 'main_menu':
                    controller.run = False
                    paused = False
       
        # Display Pause Menu

        screen.fill('black')

        settings_menu.display()

        for line in texts:
            line.display()

        pygame.display.flip()