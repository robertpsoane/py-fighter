''' Pause Screen

@author: Robert
'''

import pygame

from classes.text import Text

def pauseScreen(screen):

    paused_text = Text(screen, (500, 200), 60, 'PAUSED', 'purple')
    
    paused = True
    while paused:

        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                paused = False
            
                    
        # Display Pause
        paused_text.display()

        pygame.display.flip()
        
        