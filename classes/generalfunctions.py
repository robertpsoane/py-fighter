'''
File for storing any general functions that get regularly reused

'''

import os
import pygame


def quitGame():
    '''
    Function to quit game
    '''
    pygame.quit()
    os._exit(0)