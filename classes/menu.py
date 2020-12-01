''' Menu Class

Class to create menu in pygame.  Used initially for start menu.  Can be 
extended if required to create pause and other menues throughout the 
game.

@author: Robert (unless stated otherwise)
'''

import pygame
import webbrowser
from classes.text import Text

menu_background_location = 'graphics/menu/menu-background.png'
button_location = 'graphics/menu/button.png'

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
    def __init__(self, screen, text, position, size = (128, 64),
                            text_colour = 'white', highlight = 'yellow',
                            font_size = 35):
        # Storing attributes
        self.screen = screen
        self.text = text
        self.__position = position
        self.size = size
        self.text_colour = text_colour
        self.highlight = highlight
        self.font_size = font_size
        self.highlighted = False

        # Make edges attributes
        self.setEdgesAttributes()

        # Making text and images
        self.makeText()
        self.makeImage()

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
        if (self.left < pos_x < self.right) and (self.top < pos_y < self.bottom):
            self.highlighted = True
            self.text.colour = self.highlight
            self.actionIfPressed()
        elif self.highlighted:
            self.text.colour = self.text_colour

    def actionIfPressed(self):
        if pygame.mouse.get_pressed()[0]:
            self.function()
        
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
        
        self.background = pygame.image.load(menu_background_location)
        self.background_rect = pygame.Rect((0, 0, 1, 1))

        self.playMusic()
        
        # Quitting Bool to determine whether to quit game
        self.playing = True

    def display(self):
        self.screen.blit(self.background, self.background_rect)
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
            self.playMusic()
        elif option == '2':
            # Note: This will be updated to help link when help link 
            # exists
            webbrowser.open('https://sites.google.com/view/pyfighter/home',
                            new=2)
        elif option == '3':
            self.playing = False

    def playMusic(self):
        ### Setting up game music
        # - Music code inspired by code here:
        #   https://riptutorial.com/pygame/example/24563/example-to-add-music-in-pygame
        menu_background_path = 'audio/Indigo_Heart.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(menu_background_path)
        pygame.mixer.music.play(-1)
