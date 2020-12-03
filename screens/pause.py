''' Pause Screen

@author: Robert
'''

import pygame

from classes.text import Text

def pauseScreen(screen):
    height = screen.get_height() // 2
    width = screen.get_width() // 2
    paused_text = Text(screen, (width, height), 60, 'PAUSED', 'purple')
    
    paused = True
    while paused:

        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                paused = False
            
                    
        # Display Pause
        paused_text.display()

        pygame.display.flip()
        
        