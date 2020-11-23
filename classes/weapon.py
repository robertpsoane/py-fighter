''' Weapon Class
- To have a subclass for each weapon.
@author: Shaylen Mistry (unless stated otherwise)
'''
import pygame
from classes.spritesheet import SpriteSheet
# from spritesheet import SpriteSheet
# arms spirtesheets
BASIC_ARMS_LOCATION = 'graphics/spritesheets/basic-arms.png'

print()
# static images

class Weapon:
    def __init__(self, screen, image_types, image_directions, scaled_size, char_size,
                coords, sprite_sheet_location, status, index):
        pygame.sprite.Sprite.__init__(self)
        self.loadSpriteSheets(image_types, image_directions, scaled_size, char_size,
                coords, sprite_sheet_location)

        # Setting up initial image
        self.image = self.images[status[0]][status[1]]


    
    def loadSpriteSheets(self, image_types, image_directions, scaled_size, 
                        char_size, coords, sprite_sheet_location,
                        background_colour = (0, 255, 0)):
        ''' Assigns animation images to self


        '''
        self.spritesheet = SpriteSheet(sprite_sheet_location)
        self.images = {}
        for image_type in image_types:
            self.images[image_type] = {}
            for image_direction in image_directions:
                self.images[image_type][image_direction] = []
                for coord in coords[image_type][image_direction]:
                    specific_image = pygame.transform.scale(
                            self.spritesheet.image_at(coord, char_size),
                            scaled_size
                            )
                    specific_image.set_colorkey(background_colour)

                    self.images[image_type][image_direction] += [specific_image]

    def display(self, x, y, state, index):
        ''' display function

        state takes form [action, direction], images[action][direction] gives a list of images
        '''
        self.owner.rect.centerx
        action, direction = state[0], state[1]
        self.image = self.images[action][direction][index]
        self.screen.blit(self.image, self.rect)
        




class Sword(Weapon):
    pass


class Boomerang(Weapon):
    pass


class Arms(Weapon):
    sprite_sheet_location = BASIC_ARMS_LOCATION
    def __init__(self, image_types, image_directions, scaled_size, char_size,
                coords, status, index):

        Weapon.__init__(self, image_types, image_directions, scaled_size, 
                        char_size, coords, self.sprite_sheet_location, status, index)
    
