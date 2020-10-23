''' Character Class


'''
import pygame
from classes.spritesheet import SpriteSheet

class Character(pygame.sprite.Sprite):
    
    def __init__(self, screen, x_position, y_position):
        # Declaring self to be a sprite
        pygame.sprite.Sprite.__init__(self)

        # Assigning self.character_data to local variable character_data
        # to make code more readable
        character_data = self.character_data

        ### Unpacking some important JSON dictionary into variables
        self.speed = character_data['speed']
        self.gravity = character_data['gravity']
        self.state = character_data['initialstate']
        self.refresh_rate = character_data['refresh']

        # Character Position
        self.position = [x_position, y_position]
        
        # Load sprite sheet and extract frames to dictionary
        self.loadSpriteSheets(character_data)


        # Adding screen to object
        self.screen = screen
        self.image = self.images[self.state[0]][self.state[1]]
        self.image_index = 0
        self.rect = self.image[self.image_index].get_rect()
        self.rect.center = self.position
        self.refresh_counter = 0
        
        

    def loadSpriteSheets(self, character_data):
        ''' loadSpriteSheets(self, character_data)
        Procedure which loads spritesheet from path given, and extracts each
        frame of the sprite and stores to dictionary self.images
        These can then be updated depending on this instances state
        '''
        self.spritesheet = SpriteSheet(character_data['path'])
        char_size = character_data['charsize']
        scaled_size = character_data['scaledsize']
        background_colour = character_data['background']
        
        image_types = character_data['actions']
        image_directions = character_data['directions']

        self.images = {}

        # Importing images into self.images dictionary
        for image_type in image_types:
            self.images[image_type] = {}
            for image_direction in image_directions:
                self.images[image_type][image_direction] = []
                for coords in character_data[image_type][image_direction]:
                    specific_image = pygame.transform.scale(
                            self.spritesheet.image_at(coords,char_size),
                            scaled_size
                            )
                    specific_image.set_colorkey(background_colour)
                    
                    self.images[image_type][image_direction] += [specific_image]


    def display(self):
        ''' Display function
        
        Specific display function for characters.  Keeps track of number of 
        times display has been called.  Depending on the refresh attribute, 
        every n times it switches to the next image.  This is to animate
        the image.
        '''
        # Displaying current image at current position
        self.screen.blit(self.image[self.image_index], self.rect)

        # Updating counter, and if necessary incrementing image
        self.refresh_counter += 1
        if self.refresh_counter % self.refresh_rate == 0:
            self.incrementImage()
        
        # Updating positions subject to gravity
        

    def incrementImage(self):
        ''' Increment Image functino
        Increments image by 1, and resets counting variable
        '''
        # Resetting refresh counter
        self.refresh_counter = 0

        # Incrementing image index
        self.image_index += 1

        # Returning to 0 when image index > length
        n_images = len(self.image)
        if self.image_index == n_images:
            self.image_index = 0
    
    
    def move(self,direction):
        if direction == 'l':
            pass
        elif direction == 'r':
            pass
        elif direction == 'u':
            pass

    