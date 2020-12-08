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

HIGH_SCORE_LOCATION = 'other_data/highscores.txt'


def randomFunc():
    print('ahhhhhhhh')


def gameOver(screen, score, delay):
    # load clock
    clock = pygame.time.Clock()

    width = screen.get_width()
    height = screen.get_height()

    scores = []
    sub_scores = []

    # Opening scores file and transfering scores from the file to a list.
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

    print(res_score)

    score_header = Text(screen, (width // 2, height // 3), 30, f'HIGHEST SCORE')
    high_score = Text(screen, (width // 2, 250), 25,
                      f'{res_score[-1][0]} = {res_score[-1][-1]}')
    your_score = Text(screen, (width // 2, 300), 30, f'YOUR SCORE')
    sample_text = Text(screen, (width // 2, 335), 25, f'{score}')


    menu_title = Text(screen, (width // 2, height // 4), 50, 'Game Over', 'Purple')
    back_to_menu = Button(screen, 'Main menu', (400, 500), (lambda: 'main_menu'), 25, (200, 64))
    exit_game = Button(screen, 'Quit', (600, 500), quitGame, 25, (200, 64))
    all_scores = Button(screen, 'New game', (600, 500), quitGame, 25, (200, 64))

    sample_menu = Menu(screen, menu_title, False, back_to_menu, exit_game, all_scores)

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

        score_header.display()
        sample_text.display()
        sample_menu.display()
        high_score.display()
        your_score.display()

        pygame.display.flip()
