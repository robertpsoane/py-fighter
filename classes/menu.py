''' Menu Class

Class to create menu in pygame.  Used initially for start menu.  Can be 
extended if required to create pause and other menues throughout the 
game.

@author: Robert (unless stated otherwise)
'''

import pygame
from classes.text import Text

button_location = 'graphics/menu/button.png'


class Menu:
    def __init__(self, screen, title_obj, background_location, *buttons):
        ''' Start Menu
        Class which generates and contains start menu function.
        '''
        self.screen = screen
        self.title_obj = title_obj
        self.unpackButtons(buttons)
        
        self.background = pygame.image.load(background_location)
        self.background_rect = pygame.Rect((0, 0, 1, 1))

        # Quitting Bool to determine whether to quit game
        self.playing = True

    def display(self):
        self.screen.blit(self.background, self.background_rect)
        self.title_obj.display()
        # self.play_obj.display()
        # self.help_obj.display()
        for button in self.buttons:
            button.display()

    def do(self, event):
        ''' do function
        Actions whatever action is called by user
        
        if option == '1':
            self.play_game()
            self.playMusic()
        elif option == '2':
            # Note: This will be updated to help link when help link 
            # exists
            webbrowser.open('https://sites.google.com/view/pyfighter/home',
                            new=2)
        elif option == '3':
            self.playing = False
        '''
        if event.type == pygame.QUIT:
            # Detecting user pressing quit button, if X pressed,
            # break loop and quit screen.
            self.playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if self.checkPress(button, event.pos):
                    button.mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            for button in self.buttons:
                if self.checkPress(button, event.pos) and button.mouse_down:
                    button.press()
                button.mouse_down = False
                
    def checkPress(self, button, pos):
        x0, x1, y0, y1 = button.coords
        if (x0 < pos[0] < x1) and (y0 < pos[1] < y1):
            return True
        return False

    def unpackButtons(self, buttons):
        self.buttons = []
        for button in buttons:
            self.buttons.append(button)



class Button:
    ''' Button Class

    Creates an automatically highlighted button using the Text class
    from the text module.

    The buttons display function checks whether cursor is covering it.
    If the button is being covered, it highlights the text (yellow by
    default) and if clicked it calls the given function.

    I have used property decorators to deal with button position, as in
    the Text class so that the button can easily be moved on screen if 
    required
    '''
    def __init__(self, screen, text, position, func, size = (128, 64),
                            text_colour = 'white', highlight = 'yellow',
                            font_size = 35):
        # Storing attributes
        self.screen = screen
        self.text = text
        self.__position = position
        self.func = func
        self.size = size
        self.text_colour = text_colour
        self.highlight = highlight
        self.font_size = font_size
        self.highlighted = False
        self.mouse_down = False

        # Make edges attributes
        self.setEdgesAttributes()

        # Making text and images
        self.makeText()
        self.makeImage()

    def press(self):
        self.func()

    def makeText(self):
        self.text = Text(self.screen, self.position, self.font_size,
                            self.text, self.text_colour)
    
    def makeImage(self):
        self.image = pygame.transform.scale(
            pygame.image.load(button_location),
            self.size
        )
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        over_button = (self.left < pos_x < self.right) and (self.top < pos_y < self.bottom)
        if over_button:
            self.highlighted = True
            self.text.colour = self.highlight
        elif self.highlighted:
            self.text.colour = self.text_colour
            self.highlighted = False
      
    def display(self):
        self.update()
        self.screen.blit(self.image, self.rect)
        self.text.display()

    def setEdgesAttributes(self):
        self.left = self.position[0] - (self.size[0] // 2)
        self.right = self.position[0] + (self.size[0] // 2)
        self.top = self.position[1] - (self.size[1] // 2)
        self.bottom = self.position[1] + (self.size[1] // 2)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_pos):
        self.__position = new_pos
        self.setEdgesAttributes()
        self.text.position = self.position
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

    @property
    def coords(self):
        return (self.left, self.right, self.top, self.bottom)


