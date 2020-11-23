''' Menu Class

Class to create menu in pygame.  Used initially for start menu.  Can be 
extended if required to create pause and other menues throughout the game.

'''

import pygame
import webbrowser

class StartMenu:
    def __init__(self, screen, title_obj, play_obj, help_obj, quit_obj,
                game_function):
        ''' Start Menu
        Class which generates and contains start menu function.
        '''
        self.screen = screen
        self.title_obj = title_obj
        self.play_obj = play_obj
        self.help_obj = help_obj
        self.quit_obj = quit_obj
        self.play_game = game_function
        
        # Quitting Bool to determine whether to quit game
        self.playing = True

    def display(self):
        self.title_obj.display()
        self.play_obj.display()
        self.help_obj.display()
        self.quit_obj.display()

    def do(self, option):
        ''' do function
        Actions whatever action is called by user
        '''
        if option == '1':
            self.play_game()
        elif option == '2':
            # Note: This will be updated to help link when help link exists
            webbrowser.open('https://sites.google.com/view/pyfighter/home',
                            new=2)
        elif option == '3':
            self.playing = False
