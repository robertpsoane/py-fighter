''' Character Class


'''
import pygame

class Character(pygame.sprite.Sprite):
    
    def setup(self, character_data):
        # Unpacking some key JSON dictionary into variables
        self.speed = character_data['speed']
        self.gravity = character_data['gravity']
        
        self.spritesheet = pygame.image.load(img_data['path'])

        self.images = {
            'running': {
                'left': [],
                'right': []
            },
            'idle': 
        }


    
        
    
    
    
    def move(self,direction):
        if direction == 'l':
            pass
        elif direction == 'r':
            pass
        elif direction == 'u':
            pass

    