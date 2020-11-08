''' Character Class

Character class for py-fighter game.
Takes input of character data, screen, x position, and y position.

Has functions to make move.

- character_data takes the form of a Python dictionary with all key components 
and data for character.  This is usually stored in a JSON. We have decided
to implement like this as it allows us to add future characters or make 
significant changes to the characters without having to edit the python code.

character_data follows the following structure:

{
    "actions": ["running", "idle"],  <-- These lines should not be edited
    "directions": ["left", "right"], <-- from the preset as changing them may
                                        cause the game to break
    "running": {
        "left": [[0, 0], [0, 1], [0, 2], [0, 3], [0, 0], [0, 4], [0, 5], [0, 6]],
        "right": [[2, 0], [2, 1], [2, 2], [2, 3], [2, 0], [2, 4], [2, 5], [2, 6]]
        },  

    "idle": {
        "left": [[0, 0], [1, 0]],
        "right": [[2, 0], [3, 0]]
        },

        ^ These nested lists give the coordinates within the grid (in order) ^
            of where the images that make up the given action can be found
            in the sprite sheet.  There should be one dictionary for each action,
            containing a list for each direction

    "path": "graphics/spritesheets/basic-character.png", <-- File path of the
    "background": [0, 255, 0], <-- Background colour        spritesheet
    "gridsize": [4, 9], <-- Grid size of sprite sheet (zero-indexed)
    "charsize": [32, 32], <-- Size of character in pixels
    "scaledsize": [128, 128], <-- Size to scale character to in pixels
    "speed": 1, <-- Speed of character in pixels per frame
    "gravity": 1, <-- Gravitationaly speed in pixels per frame
    "refresh": 10, <-- Number of frames between character refresh
    "initialstate": ["running", "right"] <-- State the character is initially
                                            spawned in (eg direction facing)
}

Future Plans:
- Gravity/falling
- Jump function
- Health functionality
- Attack functionality
- Recoil functionality


'''
import pygame
from classes.spritesheet import SpriteSheet

class Character(pygame.sprite.Sprite):
    
    def __init__(self, character_data, screen, x_position, y_position):
        # Declaring self to be a sprite
        pygame.sprite.Sprite.__init__(self)

        # Assigning character data to self.charactar_data
        self.character_data = character_data

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
    
    def updateState(self, action, direction):
        ''' updateState(action, direction)
        function to update state of character
        '''
        self.state = [action, direction]

    def moveX(self, step):
        ''' moveX(step)
        Function to move character step pixels in the X direction
        '''
        self.position[0] += step
        self.rect.center = self.position

    def moveY(self, step):
        ''' moveY(step)
        Function to move character step pixels in the Y direction.
        - Note: the y axis is flipped from what we might naturally assume,
                0 is at the top and not the bottom
        '''
        self.position[1] += step
        self.rect.center = self.position

    
    def startMove(self,direction):
        ''' startMove(direction)
        Input 'l' or 'r' for horizontal movement, 'u' for jump
        '''
        if direction == 'l':
            # Moving one speed step left
            self.moveX(self.speed)
            self.state = ['running', 'left']
        elif direction == 'r':
            # Moving one speed step right
            self.moveX(-1 * self.speed)
            self.state = ['running', 'right']
        elif direction == 'u':
            pass
    
    def stopMove(self):
        ''' stopMove()
        Returns state to idle when no longer moving.  Purpose of function is 
        to stop running animation.

        WILL NEED CHANGING WHEN WEAPONS ARE IMPLEMENTED! Will need to choose 
        state based on weapon!
        '''
        self.state[0] = 'idle'
    

    
