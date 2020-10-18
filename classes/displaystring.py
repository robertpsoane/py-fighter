''' Display String Class

Class to display string output to screen.

Will be expanded to include methods to later update string displayed.

'''

import pygame

class DisplayString:
    def __init__(self, screen, x_position, y_position, font_size,
                input_string, colour = (255,255,255)):
        ''' __init__ function
        Stores variables passed in to object.
        Generates a text object using initial text given.  This can then be
        displayed using pygame.  Uses the printer.tff font by default.
        '''

        # Initialising pygame
        pygame.init()

        # Storing position data to self
        self.screen = screen
        self.x_pos = x_position
        self.y_pos = y_position
        self.text = input_string

        # Setting up font using pygame
        self.font = pygame.font.Font('graphics/fonts/printer.ttf',font_size)
        self.surf = self.font.render(self.text, True, colour)
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def display(self):
        ''' display function
        Used to blit text to string.  Implemented as a procedure within the 
        DisplayString class to improve readability of code.
        '''
        self.screen.blit(self.surf, self.rect)