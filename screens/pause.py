''' Pause Screen

Pause screen - This screen is displayed on top of the game when player
presses escape during the game, and enters the pause menu.

Each button is attached to a function, resume and quitToMainMenu output 
a string which is interpreted by the screens loop, wheres quitgame just
kills the game.

The reason resume and main menu quits don't act themselves, is that they
can't access the controller and game loop without having it passed into
them (or making them global which may lead to weird bugs later on), as
the Menu class we've written doesn't have the ability to pass arguments
into button functions.

@author: Robert
'''

import pygame
import os

from classes.text import Text
from classes.menu import Button
from classes.menu import Menu


# Setup menu buttons

def resume():
    return 'resume'

def quitToMainMenu():
    return 'main_menu'

def quitGame():
    pygame.quit()
    os._exit(0)



def pauseScreen(screen, controller):
    ''' Pause Screen function

    Produces the pause screen and allows interaction with buttons.
    '''
    height = screen.get_height()
    width = screen.get_width()
    height_unit = height // 3
    mid_x, mid_y = width // 2, height // 2
    menu_height = 3 * height // 4
    width_unit = width // 6

    # Setup menu and buttons
    paused_text = Text(screen, (mid_x, height_unit), 60, 'PAUSED', 'purple')

    resume_button =  Button(screen, 'Resume', (width_unit, 2 * height_unit),
                                                                    resume)

    main_menu_button =  Button(screen, 'Main Menu',
                            (3 * width_unit, 2 * height_unit),
                                                quitToMainMenu)
                            
    quit_button =  Button(screen, 'Quit', (5 * width_unit,  2 * height_unit),
                                                                    quitGame)

    pause_menu = Menu(screen, paused_text, False, resume_button, 
                                    main_menu_button, quit_button)

    # load clock
    clock = pygame.time.Clock()

    paused = True
    while paused:
        clock.tick(controller.clock_delay)

        # Get/action events
        for event in pygame.event.get():
            # Send each event to the start menu
            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                paused = False
            elif (event.type == pygame.KEYDOWN) and \
                        (event.key == pygame.K_ESCAPE):
                paused = False
            
            # Here, we check whether the player has clicked the mouse,
            # if they have, we pass the click into the pause menu and it 
            # processes the click.  The button function returns a string
            # 'resume' for resume game, or 'main_menu' to quit to main
            # menu.
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                            (event.type == pygame.MOUSEBUTTONUP):
                button_press = pause_menu.do(event)
                #print(button_press)
                if button_press == 'resume':
                    paused = False
                elif button_press == 'main_menu':
                    controller.run = False
                    paused = False
       
        # Display Pause Menu
        pause_menu.display()

        pygame.display.flip()
        
        