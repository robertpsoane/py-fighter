''' Display String Class

Class to display string output to screen.

Can be expanded to include methods to later update string displayed.

Based on code in documentation: https://www.pygame.org/docs/ref/font.html

I used this article for help with using @property setters.
https://www.datacamp.com/community/tutorials/property-getters-setters?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1006965&gclid=Cj0KCQiAzZL-BRDnARIsAPCJs70-ZtDSBvtA2CwIwzeCHEkTeOUqXFRxOSjL7FOKNb1asCXRpVBG9oEaAkBjEALw_wcB
(I implemented proerty setters mainly because I wanted to learn how to
use them after reading about them, however I also realised they could be
useful when implementing the button if we want to highlight the text)

@author: Robert
'''

import pygame

font = 'graphics/fonts/8-bit/8bitOperatorPlus8-Regular.ttf'

class Text:
    def __init__(self, screen, position, font_size,
                input_string = '', colour = (255,255,255)):
        ''' __init__ function
        Stores variables passed in to object.
        Generates a text object using initial text given.  This can then
        be displayed using pygame.  Uses the 
        8bitOperatorPlus8-Regular.tff font by default.
        '''

        # Initialising pygame
        pygame.init()

        # Storing position data to self
        self.screen = screen
        self.__position = position
        self.__text = input_string
        self.__colour = colour

        # Setting up font using pygame
        self.font = pygame.font.Font(font, font_size)
        self.makeSurf()
        self.makeRect()
        
        
    def display(self):
        ''' display function
        Used to blit text to string.
        '''
        self.screen.blit(self.text_surf, self.rect)

    def makeSurf(self):
        self.text_surf = self.font.render(self.text, False, self.colour)

    def makeRect(self):
        self.rect = self.text_surf.get_rect()
        self.rect.center = self.position

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour_val):
        self.__colour = colour_val
        self.text_surf = self.font.render(self.text, False, self.colour)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        self.__text = new_text
        self.text_surf = self.font.render(self.text, False, self.colour)
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_pos):
        self.__position = new_pos
        self.rect.center = self.position

    @property
    def x(self):
        return self.__position[0]
    
    @x.setter
    def x(self, new_x):
        self.position = [new_x, self.position[1]]

    @property
    def y(self):
        return self.__position[1]
    
    @y.setter
    def y(self, new_y):
        self.position = [self.position[0], new_y]