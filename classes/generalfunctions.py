'''
File for storing any general functions that get regularly reused

'''

import os
import pygame
from operator import itemgetter

HIGH_SCORE_LOCATION = 'other_data/highscores.txt'

def quitGame():
    '''
    Function to quit game
    '''
    pygame.quit()
    os._exit(0)

def loadScoreList():
    scores = []
    # Opening scores file and transferring scores from the file to a list.
    f = open(HIGH_SCORE_LOCATION, 'r')
    #temp = f.read().splitlines()

    for line in f:
        line = line.split('/')
        entry_list = [line[0], line[1][:-1]]
        scores.append(entry_list)
    f.close()

    for i in range(len(scores)):
        scores[i][1] = int(scores[i][1])
    scores.sort(key=itemgetter(1))
    return scores
