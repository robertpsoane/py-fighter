''' Game Over Screen

This screen is shown at end of game.
Takes name, adds name and score to other_data/highscores.txt





Game over screen needs:
- Text saying Game Over
- Input to take name if score within the top 10
- Output of top 10 - stored in other_data/highscores.txt,
    - name/score format
- Button to return to main menu
- Button to quit

- Remember to call 'close' on file after making changes to it



- Quit Game
pygame.quit()
os._exit(0)

- Return to main menu
run = False






'''

import pygame
import os
from classes.generalfunctions import quitGame
from classes.text import Text
from classes.menu import Button
from classes.menu import Menu

HIGH_SCORE_LOCATION = 'other_data/highscores.txt'

def randomFunc():
    print('ahhhhhhhh')

def gameOver(screen, score, delay):
    # load clock
    clock = pygame.time.Clock()

    width = screen.get_width()
    height = screen.get_height()

    sample_text = Text(screen, (width // 2, height // 2), 20, f'score = {score}')
    
    menu_title = Text(screen, (width // 2, height // 4), 50, 'Game Over', 'Purple')
    sample_button = Button(screen, 'Press me', (400, 500), (lambda : 'main_menu'))
    
    sample_menu = Menu(screen, menu_title, False, sample_button)

    run = True
    while run:
        clock.tick(delay)

        # Get/action events
        for event in pygame.event.get():
            # Send each event to the start menu
            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                quitGame()
                
            # Do mouse up/down events
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                (event.type == pygame.MOUSEBUTTONUP):
                
                button_press = sample_menu.do(event)

                if button_press == 'main_menu':
                    run = False

        screen.fill('black')

        # Display menu here - this will display all buttons included in 
        # the menu
        # menu.display()
        # Text (apart from menu title text) needs to be displayed 
        # separately

        sample_text.display()
        sample_menu.display()

        pygame.display.flip()

        


                    