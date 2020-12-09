''' High Score Screen

This screen is shown at end of game after pressing on scoreboard button.
Takes data from other_data/highscores.txt and creates a score board of top 10 players.

Used Roberts Text, Menu and Button functions

@author: Rokas
'''

import pygame
from classes.generalfunctions import quitGame
from classes.generalfunctions import loadScoreList
from classes.text import Text
from classes.menu import Button
from classes.menu import Menu

# Loading the background image in to a variable.
background = pygame.image.load('graphics/menu/scoreboard.png')

def scoreBoard(screen, delay):
    '''
    Function which creates a screen where a score bored is displayed by
    using the values from highscores.txt.
    '''

    # establishing a clock for the screen
    clock = pygame.time.Clock()

    # Creating width and height variables.
    width = screen.get_width()
    height = screen.get_height()

    # loading a list from game over screen with the newest scores.
    score_list = loadScoreList()

    if len(score_list) < 10:
        n_scores = len(score_list)
    else:
        n_scores = 10

    # Creating text objects for n highest scores.
    Header = Text(screen, (width // 2, height // 8), 50, 
                        f'TOP {n_scores} SCORES', 'purple')
    score_objects = []
    for k in range(n_scores):
        index = - 1 * (k + 1)
        score_objects.append(
            Text(screen, (width // 2, 120 + (k * 40)), 35, 
            f'{score_list[index][0]} = {score_list[index][1]}')
        )
    
    # Creating a button for going back to the game over screen.
    back = Button(screen, 'Back', (400, 585), (lambda: 'go_back'), 25, 
                                                            (126, 64))
    menu = Menu(screen, Header, False, back)

    # Creating a loop for the scoreboard screen.
    run = True
    while run:
        clock.tick(delay)

        for event in pygame.event.get():
            # Send each event to the start menu

            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                quitGame()

            # Checking if the Back button is being pressed.
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                (event.type == pygame.MOUSEBUTTONUP):

                button_press = menu.do(event)

                if button_press == 'go_back':
                    run = False

        # Bliting background image.
        screen.blit(background, (0, 0))

        # Bliting text objects and button to screen.
        
        for score_object in score_objects:
            score_object.display()
        menu.display()
        pygame.display.flip()

