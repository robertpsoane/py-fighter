''' SFX box

A class for providing specific sound effects.
The idea behind this class, is that by producing one class to handle all
sound effects, sound effects can be called from elsewhere in the code 
without having to deal with the pygame code.  

While this arguably creates extra complexity with the code, by putting
all sound effects into this small class, it allows us to add or change 
sound effects without having to go through the entire code base to 
change the location to the new sound.

I based my code on the sound effects implementation here
https://pythonprogramming.net/adding-sounds-music-pygame/

@author: Robert (Unless stated otherwise)
'''
import pygame

click_location = 'audio/sfx/click.wav'
punch_location = 'audio/sfx/punch.wav'
wind_location = 'audio/sfx/wind.wav'

class SFXBox:
    def __init__(self):
        ''' Inits the mixer and stores sounds to object
        '''
        pygame.mixer.init()

        self.click_sound = pygame.mixer.Sound(click_location)
        self.punch_sound = pygame.mixer.Sound(punch_location)
        self.wind_sound = pygame.mixer.Sound(wind_location)

    # The following functions play the sound effect
    def click(self):
        self.click_sound.play()
    
    def punch(self):
        self.punch_sound.play()

    def wind(self):
        self.wind_sound.play()

    