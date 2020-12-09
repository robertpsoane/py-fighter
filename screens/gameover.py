''' Game Over Screen

This screen is shown at end of game.
Takes name, adds name and score to other_data/highscores.txt

Text object for user to input name - idea taken from here: 
https://www.youtube.com/watch?v=Rvcyf4HsWiw




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
            '9', '0', '-'}


def gameOver(screen, score, delay):
    
    def saveScore():
        '''
        Function which takes user name and current score and stores it in a text file.
        '''
        saves = open(HIGH_SCORE_LOCATION, 'a')
        saved_score = f'{player_name.text}/{score.text}\n'
        saves.write(saved_score)
        saves.close()
    
    # load clock
    clock = pygame.time.Clock()

    # Generate useful positions
    width = screen.get_width()
    height = screen.get_height()
    mid = width // 2
    left = width // 5
    right = 4 * left
    height_unit = height // 20

    # Load previous scores and calculate highscore
    scores = loadScoreList()
    if (len(scores) > 0) and (scores[-1][-1] >= score):
        highscore_string = f'{scores[-1][0]} : {scores[-1][-1]}'        
    else:
        highscore_string = f'You! : {score}'

    # Text input is active
    active = True
    started = False

     # Creating text for the main header.
    menu_title = Text(screen, (mid, 2 * height_unit), 70, 'Game Over', 'Purple')

    # Creating a header for the score.
    score_header = Text(screen, (mid, 4 * height_unit), 30, f'HIGHSCORE')

    # Creating text object for the highest score of the game
    high_score = Text(screen, (mid, 5 * height_unit), 25, highscore_string)

    # Creating text object for the current score of the game
    your_score = Text(screen, (mid, 7 * height_unit), 30, f'YOUR SCORE')
    
    # Creating object for the current score.
    score = Text(screen, (mid, 8 * height_unit), 25, f'{score}')

    player_name_center = (mid, 9 * height_unit)
    player_name = Text(screen, player_name_center, 30, '[Enter Name Here]', 'yellow')

    save_score = Button(screen, 'Save Score', (mid, 11 * height_unit), (lambda : 'save'), 25, (200, 64))
        


    # Creating a button for scoreboard.
    score_board = Button(screen, 'Scoreboard', (left, 18.5*height_unit//1), (lambda: 'scoreboard'), 25, (200, 64))

    # Creating a button for main menu.
    back_to_menu = Button(screen, 'Main menu', (mid, 18.5*height_unit//1), (lambda: 'main_menu'), 25, (200, 64))

    # Creating a button to exit the game
    exit_game = Button(screen, 'Quit', (right, 18.5*height_unit//1), quitGame, 25, (200, 64))


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
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        player_name.text = player_name.text[0: -1]
                        player_name.position = player_name.position
                    elif pygame.key.name(event.key) in ALPHABET:
                        if not started:
                            player_name.text = ''
                            started = True
                        player_name.text += event.unicode
                        player_name.position = player_name_center[0], \
                                                player_name_center[1]
                        player_name.makeRect()



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
        score.display()
        high_score.display()
        your_score.display()

        

        pygame.display.flip()
