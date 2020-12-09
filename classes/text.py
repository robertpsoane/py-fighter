''' Display String Class

Class to display string output to screen.

Based on code in documentation: https://www.pygame.org/docs/ref/font.html

I used this article for help with using @property setters.
https://www.datacamp.com/community/tutorials/property-getters-setters?ut
m_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&
utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&u
tm_creative=229765585186&utm_targetid=dsa-429603003980&utm_loc_interest_
ms=&utm_loc_physical_ms=1006965&gclid=Cj0KCQiAzZL-BRDnARIsAPCJs70-ZtDSBvt
A2CwIwzeCHEkTeOUqXFRxOSjL7FOKNb1asCXRpVBG9oEaAkBjEALw_wcB

I implemented property setters mainly because I read about them and 
wanted to implement them to fully get my head around how they work, 
however I believe this is a good use case for property decorators.
The reason for this is:
- We want to be able to update the colour or string of the text.  The 
text needs re-rendering with the new colour or string.  By updating it 
in a setter function, this avoids having to re-render the surface each
time we call instantiate teh object.  We are only re-rendering when we
make a change
- This allows us to access and change the position of the coordinates
at any time without creating inconsitencies

@author: Robert
'''

import pygame

font = 'graphics/fonts/8-bit/8bitOperatorPlus8-Regular.ttf'

class Text:
    def __init__(self, screen, position, font_size,
                input_string = '', colour = (255,255,255)):
        ''' Text

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
        ''' Renders our string to a surface
        '''
        self.text_surf = self.font.render(self.text, False, self.colour)

    def makeRect(self):
        ''' Makes rectangle from surface
        '''
        self.rect = self.text_surf.get_rect()
        self.rect.center = self.position

    # Colour property - stores the colour of the text in a private 
    # attribute.  This property can be updated using the setter, this 
    # updates the private attribute, and re-generates the surface
    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour_val):
        self.__colour = colour_val
        self.text_surf = self.font.render(self.text, False, self.colour)

    # text property - stores the string in a private attribute.  When 
    # changing the string, we we-render the surface with the new string
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        self.__text = new_text
        self.text_surf = self.font.render(self.text, False, self.colour)
    
    # The following position code ensures the x and y coordinates can be
    #  changed independently, or with the position, for example if we 
    # want to make text move across the screen.
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