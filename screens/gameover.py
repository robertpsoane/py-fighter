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



- Return to main menu
run = False






'''

import pygame
import os
from classes.generalfunctions import quitGame
from classes.text import Text
from classes.menu import Button
from classes.menu import Menu
from operator import itemgetter
from screens.scores import scoreBoard

HIGH_SCORE_LOCATION = 'other_data/highscores.txt'
background = pygame.image.load('graphics\menu\gamedead.png')

def gameOver(screen, score, delay):
    # load clock
    clock = pygame.time.Clock()

    width = screen.get_width()
    height = screen.get_height()

    scores = []
    sub_scores = []

    # Opening scores file and transferring scores from the file to a list.
    f = open(HIGH_SCORE_LOCATION, 'r', encoding='utf-8')
    temp = f.read().splitlines()

    for line in temp:
        scores.append(line)
    f.close()

    # Separating each score and name in to a sublist.
    for el in scores:
        sub = el.split(', ')
        sub_scores.append(sub)

    # Separating each name and score in a separate element in a sub list.
    res_score = [sub.split('/') for subl in sub_scores for sub in subl]

    for i in range(len(res_score)):
        res_score[i][1] = int(res_score[i][1])
    res_score.sort(key=itemgetter(1))

    # Creating a header for the score.
    score_header = Text(screen, (width // 2, height // 4), 30, f'HIGHEST SCORE')

    # Creating text object for the highest score of the game
    high_score = Text(screen, (width // 2, 190), 25,
                      f'{res_score[-1][0]} = {res_score[-1][-1]}')

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
    base_font = pygame.font.Font(None, 30)
    user_name = 'Write your name'
    input_rect = pygame.Rect(width // 2 - 85, 285, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    color = color_passive
    active = False

    def saveScore():
        '''
        Function which takes user name and current score and stores it in a text file.
        '''
        saves = open(HIGH_SCORE_LOCATION, 'a', encoding='utf-8')
        saved_score = user_name + '/' + str(score)
        saves.write(saved_score)
        saves.close()

    # Creating a button which will activate saveScore function.
    save_score = Button(screen, 'Save Score', (width // 2, 365), saveScore, 25, (200, 64))
    sample_menu = Menu(screen, menu_title, False, back_to_menu, score_board, exit_game, save_score)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name[0: -1]
                    else:
                        user_name += event.unicode


            # Do mouse up/down events
            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                (event.type == pygame.MOUSEBUTTONUP):

                button_press = sample_menu.do(event)

                if button_press == 'main_menu':
                    run = False

                if button_press == 'scoreboard':
                    scoreBoard(screen,delay,res_score)

        # Blit the background image to the screen.
        screen.blit(background, (0, 0))

        # If user is using the text box, the box will change color depending on the
        # boolean value of active variable.
        if active:
            color = color_active
        else:
            color = color_passive

        # Make a rect for the text box
        pygame.draw.rect(screen, color, input_rect)
        # Render the text inputted by the user.
        text_surface = base_font.render(user_name, True, (255, 255, 255))
        # Blit the text to screen
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        # Place the text on the rectangle
        input_rect.w = max(100, text_surface.get_width() + 10)
        # Display menu here - this will display all buttons included in
        # the menu
        # menu.display()
        # Text (apart from menu title text) needs to be displayed
        # separately
        score_header.display()
        sample_text.display()
        sample_menu.display()
        high_score.display()
        your_score.display()

        pygame.display.flip()
