''' Weapon Class
- To have a subclass for each weapon.
@author: Shaylen Mistry (unless stated otherwise)
'''
import pygame
from classes.spritesheet import SpriteSheet
# from spritesheet import SpriteSheet
# arms spirtesheets
BASIC_ARMS_LOCATION = 'graphics/spritesheets/basic-arms.png'
SWORD_ARMS_LOCATION = 'graphics/spritesheets/sword-arms.png'
BOOMERANG_ARMS_LOCATION = 'graphics/spritesheets/boomerang-arms.png'

#static images
SWORD_LOCATION = 'graphics/weapons/sword.png'
BOOMERANG_LOCATION = 'graphics/weapons/boomerang.png'



class Weapon(pygame.sprite.Sprite):
    def __init__(self, owner, sprite_sheet_location):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.screen = owner.screen        
        self.owned = True

        # Loading Sprite Sheet
        image_types = owner.character_data['actions']
        image_directions = owner.character_data['directions']
        char_size = [32, 32]
        scaled_size = owner.scaled_size
        coords = owner.character_data
    
        self.loadSpriteSheets(image_types, image_directions, scaled_size,
                                char_size, coords, sprite_sheet_location)

        # Setting up initial image
        self.state = owner.state
        self.image = self.images[self.state[0]][self.state[1 ]]
        self.index = owner.image_index
        self.rect = self.image[self.index].get_rect()
        self.rect.centerx = self.owner.rect.centerx
        self.rect.centery = self.owner.rect.centery


    
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

    def display(self):
        ''' display function

        state takes form [action, direction], images[action][direction] gives a list of images
        '''

        # Get owner variables
        self.state = self.owner.state
        self.index = self.owner.image_index
        action, direction = self.state[0], self.state[1]

        # Select Image
        self.image = self.images[action][direction]

        if self.owned:
            # Rect position alive
            if self.owner.alive:
                self.rect.center = self.owner.rect.center
                self.screen.blit(self.image[self.index], self.rect)
            else:
                self.owned = False 
        else:
            pass
            # Dispaly static weapon at death position
            # Check for collision with a sprite with sprite.arms.droppable = False
            #
            # If collides - replace arms with self, and set self as owned by player
            


            
        '''
        # Update dropped weapon
        if owner.alive:
            self.rect_death = self.rect
            self.screen.blit(self.image[self.index], self.rect)
        
        if not self.owner.alive:
            self.owned = False
            self.rect_death.bottom = 100
            if self.owner.sate[0] != 'idle':
                if self.owner[1] == 'right':
                    self.rect.right -= 2
                if self.owner.state[1] == 'left':
                self.rect_death.right += 2
            self.screen.blit(self.weapon, self.rect_death)
        '''
        

class DroppableWeapon(Weapon):
    droppable = True
    def display(self):
        Weapon.display(self)
        if not self.owned:
            self.screen.blit(self.weapon, self.rect) 


class Sword(DroppableWeapon):
    sprite_sheet_location = SWORD_ARMS_LOCATION
    strength = 15
    projectile = False
    def __init__(self, owner):
        Weapon.__init__(self, owner, self.sprite_sheet_location)
    
        self.weapon = pygame.image.load(SWORD_LOCATION)
        self.weapon.set_colorkey((0, 255, 0))

class Boomerang(DroppableWeapon):
    sprite_sheet_location = BOOMERANG_ARMS_LOCATION
    strength = 15
    projectile = True
    def __init__(self, owner):
        Weapon.__init__(self, owner, self.sprite_sheet_location)

        self.weapon = pygame.image.load(BOOMERANG_LOCATION)
        self.weapon.set_colorkey((0, 255, 0))
        
    def throw(self, direction):
        return BoomerangAmmo(self.owner, self.owner.target_group, self.strength, direction)

class Arms(Weapon):
    sprite_sheet_location = BASIC_ARMS_LOCATION
    strength = 10
    projectile = False
    droppable = False
    def __init__(self, owner):
        Weapon.__init__(self, owner, self.sprite_sheet_location)

class BoomerangAmmo(pygame.sprite.Sprite):
    def __init__(self, owner, characters, strength, direction):
        pygame.sprite.Sprite.__init__(self)
        self.loadFrames()
        self.group = characters
        self.owner = owner
        self.strength = strength
        self.screen = self.owner.screen

        if direction == 'left':
            self.speed = -2
        else:
            self.speed = 2

        self.frame_rate = 10
        self.frame_counter = 0
        self.period = 1
        self.period_counter = 0

        self.rect.center = self.owner.rect.center

    def loadFrames(self):
        self.frames = []
        self.spritesheet = SpriteSheet(BOOMERANG_LOCATION)
        for i in range(4):
            frame = self.spritesheet.image_at((i, 0), (32, 32), (0, 255, 0))
            self.frames.append(frame)
        self.current_frame = 0
        self.num_frames = len(self.frames)
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
    
    def update(self):

        self.period_counter += 1
        if self.period_counter == self.period:
            self.rect.centerx += self.speed
            self.period_counter = 0
        self.frame_counter += 1

        if self.frame_counter == self.frame_rate:
            self.current_frame += 1
            self.frame_counter = 0
        
        
        if self.current_frame >= len(self.frames):
            self.current_frame = 0

        collisions = pygame.sprite.spritecollide(self, self.group, False)
        
        if collisions != None:
            for sprite in collisions:
                sprite.recoil(self.strength, 1)
                self.owner.score += self.strength
                self.kill()
            
            
    def display(self):
        self.image = self.frames[self.current_frame]
        self.screen.blit(self.image, self.rect)


WEAPON_TYPES = {
    'arms':Arms,
    'boomerang':Boomerang,
    'sword':Sword
}