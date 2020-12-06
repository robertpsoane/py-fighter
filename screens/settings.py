import pygame
import os
import json

from classes.text import Text
from classes.menu import Button
from classes.menu import Menu

SETTINGS_LOCATION = 'json/settings.JSON'
DEFAULT_LOCATION = 'json/default_settings.JSON'
with open('json/background_music.JSON') as music_locations:
    MUSIC_LOCATIONS = json.load(music_locations)


class SettingsMenu:

    def __init__(self, screen, max_fps):
        self.run = True
        
        self.screen = screen
        self.max_fps = max_fps
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.height_unit = self.height // 9
        self.left = self.width // 4
        self.right = 3 * self.left
        self.mid = self.width // 2
        self.default_button = (128, 64)

        # Make texts:
        self.refreshTexts()
        self.makeMenu()
        self.runSettings()


    def loadSettings(self):
        with open(SETTINGS_LOCATION) as settings_data:
            self.settings_data = json.load(settings_data)

    def refreshTexts(self):
        self.loadSettings()

        texts = {}

        self.used_keys = [
            self.settings_data["left"],
            self.settings_data["right"],
            self.settings_data["up"],
            self.settings_data["attack"],
            self.settings_data["next_level"]
        ]
        
        screen = self.screen

        left_str = f'Move Left : {self.settings_data["left"]}'
        left_text = Text(screen, (self.left, 2 * self.height_unit), 35, left_str)
        texts['left'] = left_text

        right_str = f'Move Right : {self.settings_data["right"]}'
        right_text = Text(screen, (self.left, 3 * self.height_unit), 35, right_str)
        texts['right'] = right_text

        jump_str = f'Jump : {self.settings_data["up"]}'
        jump_text = Text(screen, (self.left, 4 * self.height_unit), 35, jump_str)
        texts['up'] = jump_text

        attack_str = f'Attack : {self.settings_data["attack"]}'
        attack_text = Text(screen, (self.left, 5 * self.height_unit), 35, attack_str)
        texts['attack'] = attack_text

        level_str = f'Next Level : {self.settings_data["next_level"]}'
        level_text = Text(screen, (self.left, 6 * self.height_unit), 35, level_str)
        texts['next_level'] = level_text

        self.texts = texts

        self.changing = (False, None)

    def resetButton(self):
        with open(DEFAULT_LOCATION) as default_settings:
            default_settings = json.load(default_settings)
            with open(SETTINGS_LOCATION, 'w') as settings_json:
                json.dump(default_settings, settings_json)
        
        self.refreshTexts()
        self.makeMusicButton()
        self.compileMenu()

    def backButton(self):
        self.run = False

    def changeMusic(self):
        music_index = self.settings_data['music']
        music_index += 1
        n_tracks = len(MUSIC_LOCATIONS['tracks'])
        if music_index >= n_tracks:
            music_index = 0
        self.settings_data['music'] = music_index
        self.saveSettings()
        self.makeMusicButton()
        self.compileMenu()
        
    def saveSettings(self):
        with open(SETTINGS_LOCATION, 'w') as settings_json:
            json.dump(self.settings_data, settings_json)

    def makeNormalButtons(self):
        
        screen = self.screen
        
        # Back Button - breaks loop and returns to main menu
        back_pos = self.default_button[0] + 10, self.height - self.default_button[1] - 10
        self.back_button = Button(screen, 'Back', back_pos, self.backButton, 20)

        # Reset Button
        reset_pos = self.width - back_pos[0], back_pos[1]
        self.reset_button = Button(screen, 'Reset', reset_pos, self.resetButton, 20)

        # Left
        self.left_button = Button(screen, 'Change', (self.right, 2*self.height_unit), (lambda : 'left'), 20)

        # Right
        self.right_button = Button(screen, 'Change', (self.right, 3*self.height_unit), (lambda : 'right'), 20)

        # Jump
        self.jump_button = Button(screen, 'Change', (self.right, 4*self.height_unit), (lambda : 'up'), 20)

        # Attack
        self.attack_button = Button(screen, 'Change', (self.right, 5*self.height_unit), (lambda : 'attack'), 20)

        # Next Level
        self.level_button = Button(screen, 'Change', (self.right, 6*self.height_unit), (lambda : 'next_level'), 20)

    def makeMusicButton(self):
        # Music
        music_name = MUSIC_LOCATIONS['tracks'][self.settings_data['music']]
        music_str = f'Music : {music_name}'
        reset_pos = self.reset_button.rect.center
        back_pos = self.back_button.rect.center
        music_position = (reset_pos[0] + back_pos[0]) // 2, \
                        (reset_pos[1] + back_pos[1]) // 2
        self.music_button = Button(self.screen, music_str, music_position, self.changeMusic, 20, (256, 64))
    
    def compileMenu(self):
        # Menu
        self.settings_menu = Menu(self.screen, self.title, False, self.left_button, self.right_button, 
                            self.jump_button, self.attack_button, self.level_button, self.back_button,
                            self.reset_button, self.music_button)

    def makeMenu(self):

        # Title
        self.title = Text(self.screen, (self.mid, self.height_unit), 40, 'Settings', 'purple')
        
        self.makeNormalButtons()
        self.makeMusicButton()
        self.compileMenu()

    def runSettings(self):
        # load clock
        clock = pygame.time.Clock()

        while self.run:
            clock.tick(self.max_fps)

            # Get/action events
            for event in pygame.event.get():
                # Send each event to the start menu
                if event.type == pygame.QUIT:
                    # Detecting user pressing quit button, if X pressed,
                    # break loop and quit screen.
                    self.run = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        self.run = False
                    elif self.changing[0]:
                        #print(settings_data[changing[1]])
                        #print(pygame.key.name(event.key))
                        new_key = pygame.key.name(event.key)
                        if new_key not in self.used_keys:
                            self.settings_data[self.changing[1]] = new_key
                            self.saveSettings()
                            self.refreshTexts()
                            

                
                elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                                (event.type == pygame.MOUSEBUTTONUP):
                    
                    button_press = self.settings_menu.do(event)
                    #print(button_press)
                    if button_press in self.texts.keys():
                        if button_press != self.changing[1]:
                            if self.changing[1] != None:
                                # If previously have had selection
                                self.texts[self.changing[1]].colour = 'white'
                            self.changing = (True, button_press)
                            self.texts[button_press].colour = 'red'
                        elif self.changing[1] == button_press:
                            # Unsets if same
                            self.texts[self.changing[1]].colour = 'white'
                            self.changing = (False, None)
        
            # Display Pause Menu
            self.screen.fill('black')

            self.settings_menu.display()

            for key in self.texts.keys():
                self.texts[key].display()

            pygame.display.flip()





 