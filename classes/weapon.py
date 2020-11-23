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
    def __init__(self, image_types, image_directions, scaled_size, char_size,
                coords, sprite_sheet_location):
        pygame.sprite.Sprite.__init__(self)
        self.loadSpriteSheets(image_types, image_directions, scaled_size, char_size,
                coords, sprite_sheet_location)

    
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

                


class Sword(Weapon):
    pass


class Boomerang(Weapon):
    pass


class Arms(Weapon):
    sprite_sheet_location = BASIC_ARMS_LOCATION
    def __init__(self, image_types, image_directions, scaled_size, char_size,
                coords):

        Weapon.__init__(self, image_types, image_directions, scaled_size, 
                        char_size, coords, self.sprite_sheet_location)
    
