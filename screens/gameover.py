''' Game Over Screen

This screen is shown at end of game.
Takes name, adds name and score to other_data/highscores.txt

@author: Robert



Game over screen needs:
- Text saying Game Over
- Input to take name if score within the top 10
- Output of top 10 - stored in other_data/highscores.txt,
    - name/score format
- Button to return to main menu
- Button to quit

- Remember to call 'close' on file after making changes to it



- Return to main menu
run = False






'''

import pygame
import os

from classes.generalfunctions import quitGame
from classes.generalfunctions import loadScoreList
from classes.text import Text
from classes.menu import Button
from classes.menu import Menu
from screens.scores import scoreBoard

HIGH_SCORE_LOCATION = 'other_data/highscores.txt'

BACKGROUND_LOCATION = 'graphics\menu\gamedead.png'

ALPHABET = {'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 
            'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 
            'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 
            's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 
            'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0'}


def gameOver(screen, score, delay):
    # load clock
    clock = pygame.time.Clock()

    width = screen.get_width()
    height = screen.get_height()

    scores= loadScoreList()

    # Creating a header for the score.
    score_header = Text(screen, (width // 2, height // 4), 30, f'HIGHSCORE')

    # Creating text object for the highest score of the game
    high_score = Text(screen, (width // 2, 190), 25,
                      f'{scores[-1][0]} = {scores[-1][-1]}')

    # Creating text object for the current score of the game
    your_score = Text(screen, (width // 2, 235), 30, f'YOUR SCORE')

    # Creating object for the current score.
    sample_text = Text(screen, (width // 2, 265), 25, f'{score}')

    # Creating a button for scoreboard.
    score_board = Button(screen, 'Scoreboard', (150, 580), (lambda: 'scoreboard'), 25, (200, 64))

    # Creating text for the main header.
    menu_title = Text(screen, (width // 2, height // 6), 50, 'Game Over', 'Purple')

    # Creating a button for main menu.
    back_to_menu = Button(screen, 'Main menu', (400, 580), (lambda: 'main_menu'), 25, (200, 64))

    # Creating a button to exit the game
    exit_game = Button(screen, 'Quit', (650, 580), quitGame, 25, (200, 64))

    

    # Creating a text object where a user can store his name.
    # Idea taken from here: https://www.youtube.com/watch?v=Rvcyf4HsWiw
    active = True
    player_name = Text(screen, (width // 2 - 85, 285), 30, '', 'yellow')

    def saveScore():
        '''
        Function which takes user name and current score and stores it in a text file.
        '''
        saves = open(HIGH_SCORE_LOCATION, 'a')
        saved_score = f'{player_name.text}/{str(score)}\n'
        saves.write(saved_score)
        saves.close()
        

    # Creating a button which will activate saveScore function.
    save_score = Button(screen, 'Save Score', (width // 2, 365), (lambda : 'save'), 25, (200, 64))
    menu = Menu(screen, menu_title, BACKGROUND_LOCATION, back_to_menu, score_board, exit_game, save_score)
    saved_menu = Menu(screen, menu_title, BACKGROUND_LOCATION, back_to_menu, score_board, exit_game)

    # Game over screen loop which checks for inputs of buttons and user text input.
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

            # Check if the text box is pressed on.
            # If so user can input text in to the box and
            # save it to the variable user_name.
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        player_name.text = player_name.text[0: -1]
                        player_name.position = player_name.position
                    elif pygame.key.name(event.key) in ALPHABET:
                        player_name.text += event.unicode
                        player_name.position = player_name.position


            # Do mouse up/down events
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                (event.type == pygame.MOUSEBUTTONUP):

                button_press = menu.do(event)

                if button_press == 'main_menu':
                    run = False

                elif button_press == 'scoreboard':
                    scoreBoard(screen,delay)

                elif button_press == 'save':
                    saveScore()
                    active = False
                    menu = saved_menu
                    player_name.colour = 'white'

        # Blit the background image to the screen.
        screen.fill('black')

        # Make a rect for the text box
        #pygame.draw.rect(screen, color, input_rect)
        # Render the text inputted by the user.
        #text_surface = base_font.render(user_name, True, (255, 255, 255))
        # Blit the text to screen
        #screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        # Place the text on the rectangle
        #input_rect.w = max(100, text_surface.get_width() + 10)
        # Display menu here - this will display all buttons included in
        # the menu
        # menu.display()
        # Text (apart from menu title text) needs to be displayed
        # separately

        
        menu.display()
        player_name.display()

        score_header.display()
        sample_text.display()
        high_score.display()
        your_score.display()

        

        pygame.display.flip()
