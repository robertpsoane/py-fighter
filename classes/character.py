''' Character Class


'''
import pygame

class Character:
    
    def setup(self, img_data):
        self.spritesheet = pygame.image.load(img_data['path'])

    
        
    
    
    
    def move(self,direction):
        if direction == 'l':
            pass
        elif direction == 'r':
            pass
        elif direction == 'u':
            pass

    