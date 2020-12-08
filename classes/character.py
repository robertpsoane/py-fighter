''' Character Class

Character class for py-fighter game.
Takes input of character data, screen, x position, and y position.

Has functions to make move.

- character_data takes the form of a Python dictionary with all key 
components and data for character.  This is usually stored in a JSON. We
have decided to implement like this as it allows us to add future 
characters or makesignificant changes to the characters without having 
to edit the python code.

character_data follows the following structure:

{
    "actions": ["running", "idle"],  <-- These lines should not be 
                                        edited
    "directions": ["left", "right"], <-- from the preset as changing 
                                        them may cause the game to break
    "running": {
        "left": [[0, 0], [0, 1], [0, 2], [0, 3],
                [0, 0], [0, 4], [0, 5], [0, 6]],
        "right": [[2, 0], [2, 1], [2, 2], [2, 3],
                [2, 0], [2, 4], [2, 5], [2, 6]]
        },

    "idle": {
        "left": [[0, 0], [1, 0]],
        "right": [[2, 0], [3, 0]]
        },

        ^ These nested lists give the coordinates within the grid (in ^
            order) of where the images that make up the given action can
            be found in the sprite sheet.  There should be one 
            dictionary for each action, containing a list for each 
            direction

    "path": "graphics/spritesheets/basic-character.png", <-- File path 
                                                            of the
    "background": [0, 255, 0], <-- Background colour        spritesheet
    "gridsize": [4, 9], <-- Grid size of sprite sheet (zero-indexed)
    "charsize": [32, 32], <-- Size of character in pixels
    "scaledsize": [128, 128], <-- Size to scale character to in pixels
    "speed": 1, <-- Speed of character in pixels per frame
    "gravity": 1, <-- Gravitationaly speed in pixels per frame
    "refresh": 10, <-- Number of frames between character refresh
    "initialstate": ["running", "right"] <-- State the character is 
                                            initially spawned in (eg 
                                            direction facing)
}

We get this from two different sources - the spritesheet JSON which 
gives a mapping between grid coordinates and the corresponding images
on the spritesheet, and the character specific config which contains 
data about the specific character.

The main source of inspiration for this class and its sub class was the
website on producing a chess game:
https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/#a-simple-sprite-sheet
This site shows how to blit images to a screen, and ways to split up
a sprites sheet.

I didn't take any inspiration for animating the sprite across frames
I just assumed I could put the images in a data structure and iterate
over them


@author: Robert (Unless stated otherwise)
'''
import pygame
import json
from classes.spritesheet import SpriteSheet
from classes.weapon import *


with open('json/spritesheet.JSON') as sprite_sheet_json:
            SPRITESHEET_JSON = json.load(sprite_sheet_json)


class Character(pygame.sprite.Sprite):

    ''' Character Class - Used to display and animate sprites from
    sprite sheets on screen.  Usually won't be initialised directly, 
    rather its two child classes (Player and NPC) will be called.
    '''

    def __init__(self, character_data, background, screen,
                                    x_position, y_position, arm_type = 'arms'):
        ''' Init Character
        Function takes and unpacks relevat information from the 
        characters JSON dictionary
        '''
        # Initi for sprite
        pygame.sprite.Sprite.__init__(self)

        # Assigning character data to self.charactar_data
        self.character_data = character_data
        self.addSpritesheetJSON()

        # Putting object to screen
        self.screen = screen

        ### Unpacking some important JSON dictionary into variables
        self.speed = character_data['speed']
        self.gravity = character_data['gravity']
        self.jump_speed = character_data['jump_speed']
        self.state = character_data['initialstate']
        self.refresh_rate = character_data['refresh']

        ### Health and stats data
        self.alive = True
        self.__max_health = character_data['initial_health_points']
        self.__health = self.__max_health
        self.strength = character_data['initial_strength']

        # Character Position
        self.position = [x_position, y_position]

        # Load sprite sheet and extract frames to dictionary
        self.loadSpriteSheets(character_data)

        # Adding screen to object
        self.image = self.images[self.state[0]][self.state[1]]
        self.image_index = 0
        self.plot_rect = self.image[self.image_index].get_rect()
        self.plot_rect.center = self.position

        self.rect = pygame.Rect((0, 0, self.width, self.height))
        self.rect.center = self.plot_rect.center

        self.feet_rect = pygame.Rect((0, 0, self.width, self.height // 10))
        self.feet_rect.bottomleft = self.rect.bottomleft

        # setup score
        self.score = 0

        # Get Character Arms TODO MAY need updating to reflect some 
        # enemies having own arms/other arms
        self.arms = WEAPON_TYPES[arm_type](self)
        self.healthbar = HealthBar(self)

        # Important move variables
        self.refresh_counter = 0
        self.x_y_moving = False
        self.recoil_status = (False, 0)

        # Storing dimension variables to self
        self.screen_dims = (screen.get_width(), screen.get_height())

        # Referencing important background variables
        self.changeMap(background)

        ##### TO GO TO JSON
        self.is_falling = False
        self.is_jumping = False
        self.attacking = False
        self.init_attacking = False
        self.jumps_in_action = 0
        self.max_jumps_in_action = 2
        self.attack_frame_counter = 0

        self.thrown_projectiles = pygame.sprite.Group()
    
    def changeMap(self, background):
        ''' changeMap(background) - used to update to new map

        Function to update player with new background.  Call this on 
        player when new map produced, map refers to class containing 
        sprite group of tiles, and map_matrix
        '''
        self.background = background
        self.map_matrix = background.map_matrix
        self.tiles_group = background.map_group
        self.tile_rect = []
        for tile in self.tiles_group:
            self.tile_rect.append(tile.rect)

    def addSpritesheetJSON(self):
        ''' addSpritesheetJSON

        Loads spritesheet interpretation data from SPRITESHEET_JSON
        '''
        for key in SPRITESHEET_JSON.keys():
            self.character_data[key] = SPRITESHEET_JSON[key]

    def loadSpriteSheets(self, character_data):
        ''' loadSpriteSheets(self, character_data)

        Procedure which loads spritesheet from path given, and extracts 
        each frame of the sprite and stores to dictionary self.images
        These can then be updated depending on this instances state
        '''
        self.spritesheet = SpriteSheet(character_data['path'])
        char_size = character_data['charsize']
        scale_factor = character_data['scale_factor']
        scaled_size = [char_size[0] * scale_factor, 
                        char_size[1] * scale_factor]
        self.scaled_size = scaled_size
        background_colour = character_data['background']

        image_types = character_data['actions']
        image_directions = character_data['directions']

        graphic_dims = character_data['graphic_dims']
        self.width = graphic_dims[0] * scale_factor
        self.height = graphic_dims[1] * scale_factor

        self.images = {}

        # Importing images into self.images dictionary
        # This interacts with spritesheet code from https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/#a-simple-sprite-sheet
        # to load sprites into a dictinoary
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

                    self.images[image_type][image_direction] += \
                                                            [specific_image]

    def changeArms(self, arm_type):
        self.arms = self.arms = WEAPON_TYPES[arm_type](self)

    def addTarget(self, target_group):
        ''' Adds group of enemies to player
        '''
        self.target_group = target_group

    def spriteCollision(self, other):
        if pygame.sprite.collide_rect(self, other):
            print('COLLISION')
        else:
            print('NO COLLISION')

    def attack(self, target, type = 1):
        ''' Attack function - Attacks player assigned to it 

        Causes player being attacked to recoil in opposite direction, 
        and lose health.
        '''
        if self.rect[0] < target.rect[0]:
            direction = 1
        else:
            direction = -1
        self.arms.attack(direction, target)
        
        

    def isFacingTarget(self, target):
        '''
        Function to check whether self is facing a particular enemy
        '''
        if self.state[1] == 'left' and \
            (self.rect.centerx > target.rect.centerx):
            return True
        elif self.state[1] == 'right' and \
            (self.rect.centerx < target.rect.centerx):
            return True
        return False


    def recoil(self, force, direction):
        ''' Recoil function - Loses health from attack and sets recoil 
        counter

        Recoil counter processed in display function.  Each frame pushes 
        character back while recoiling.
        '''
        self.health -= force
        self.score -= force // 5
        self.recoil_status = (True, direction)
        self.recoil_counter = 5 


    def update(self):
        ''' Update function

        Updates position of characters subject to state.
        '''

        # Check if attacking, if attacking change state to attacking for one 
        # frame
        if (self.attacking) and (self.init_attacking == False):
            self.pre_attack_action, self.pre_attack_direction = self.state
            self.updateState('attack', self.pre_attack_direction)
            self.init_attacking = True
            #self.incrementImage()
        elif self.init_attacking:
            self.attack_frame_counter += 1    

        if self.attack_frame_counter == self.refresh_rate:
            self.attack_frame_counter = 0
            self.attacking = False
            self.init_attacking = False
            self.updateState(self.pre_attack_action, self.pre_attack_direction)

        # Update verticle subject to jumping
        #if self.state[0] == 'jumping':
        if self.is_jumping:
            self.applyJump()
        else:
            if not self.collisionWithGround() :
                self.is_falling = True

            # Updating position subject to gravity
            if self.is_falling:
                self.applyGravity()

        # Updating subject to recoil.  If character is recoiling, move 
        # in recoil direction
        if self.recoil_status[0]:
            if self.recoil_counter == 0:
                self.recoil_status = (False, 0)
            self.moveX(15 * self.recoil_status[1])
            self.recoil_counter = self.recoil_counter - 1

        
        #self.collidesWithAny()

        # Update x/y subject to status
        if self.x_y_moving:

            if self.state[1] == 'right':
                self.moveX(self.speed)
                
            if self.state[1] == 'left':

                move_speed = -1 * self.speed
                self.moveX(move_speed)


    def syncRects(self):
        self.feet_rect.bottomleft = self.rect.bottomleft
        self.plot_rect.center = self.rect.center

    def display(self):
        ''' Display function

        Updates image if required, and displays image(s) to screen
        '''
        # Update state image TODO CHANGE image code
        self.image = self.images[self.state[0]][self.state[1]]

        # Updating counter, and if necessary incrementing image
        self.refresh_counter += 1
        if self.refresh_counter == self.refresh_rate:
            self.incrementImage()

        # Catch frames changed mid refresh
        if self.image_index >= len(self.image):
            self.incrementImage()

        self.syncRects()

        # ###################################################
        # # TODO DELETE THE FOLLOWING CODE - FOR TESTING ONLY
        # surf = pygame.Surface((self.rect.width, self.rect.height))
        # surf.fill((100, 100, 0))
        # self.screen.blit(surf, self.rect)

        # surf = pygame.Surface((self.feet_rect.width, self.feet_rect.height))
        # surf.fill((0, 100, 100))
        # self.screen.blit(surf, self.feet_rect)
        # ###################################################

        # Displaying current image at current position
        self.screen.blit(self.image[self.image_index], self.plot_rect)

        # Display arms and health bar
        #print(self.arms)
        self.arms.display()
        self.healthbar.display()

    def collisionWithGround(self):
        ''' Collision Detection
        Detects collision with the ground - if colliding with ground,
        returns True

        Based on code from Python Basics YouTube series
        https://www.youtube.com/watch?v=bQnEQvyS1Ns - Approx 4 minutes 
        in, and the pygame documentation.

        Initially this was implemented with pygame.sprite.spritecollide
        with the tiles_group, however this caused issues with any point 
        of a sprite colliding with a tile causing it to cease to fall.
        This means you could get characters awkwardly suspended by their
        heads.  Instead we used pygame.Rect.collidelist
        '''
        
        if self.feet_rect.collidelist(self.tile_rect) != -1:
            self.is_falling = False
            self.is_jumping = False
            self.jumps_in_action = 0
            self.stopMove()
            return True
        else:
            return False

    def applyGravity(self):
        ''' applyGravity
        Updates position subject to gravity.
        If self is falling, then move
        down by gravity.  Then checks for collisions with tiles to 
        update falling status.
        '''
        # Updating positions subject to gravity
        self.moveY(self.gravity)
        self.collisionWithGround()

    def applyJump(self):
        ''' Applys Jump to player after jump has been pressed
        '''
        jump = self.jump_speed // self.jumpcount
        self.moveY( -1 * jump)
        self.jumpcount = self.jumpcount * 2
        if (jump == 1) or (jump == 0):
            self.is_falling = True
            self.is_jumping = False
            #self.state[0] = 'falling'

    def incrementImage(self):
        ''' Increment Image function
        Increments image by 1, and resets counting variable
        '''
        # Resetting refresh counter
        self.refresh_counter = 0

        # Incrementing image index
        self.image_index += 1

        # Returning to 0 when image index > length
        n_images = len(self.image)
        if self.image_index >= n_images:
            self.image_index = 0

    def updateState(self, action, direction):
        ''' updateState(action, direction)
        function to update state of character
        '''
        self.state = [action, direction]
        self.refresh_counter = 0
        self.image_index = 0

    def moveX(self, step):
        ''' moveX(step)
        Function to move character step pixels in the X direction
        '''
        self.rect.centerx += step

    def moveY(self, step):
        ''' moveY(step)
        Function to move character step pixels in the Y direction.
        - Note: the y axis is flipped from what we might naturally 
                assume, 0 is at the top and not the bottom
        '''
        self.rect.centery += step

    def startMove(self,direction):
        ''' startMove(direction)
        Input 'l' or 'r' for horizontal movement, 'u' for jump
        '''
        if self.state[0] == 'idle':
            self.state[0] = 'running'
        if direction == 'l':
            # Moving one speed step left
            self.x_y_moving = True
            self.state[1] = 'left'
        elif direction == 'r':
            # Moving right
            self.x_y_moving = True
            self.state[1] = 'right'
        elif direction == 'u':
            #self.state[0] = 'jumping'
            if (self.jumps_in_action < self.max_jumps_in_action):
                self.is_jumping = True
                self.jumpcount = 1
                self.jumps_in_action += 1
            

    def stopMove(self, direction = 'none'):
        ''' stopMove()
        Returns state to idle when no longer moving.  Purpose of 
        function is to stop running animation.
        '''
        if self.state == ['running', direction]:
            self.updateState('idle', direction)
            self.x_y_moving = False
        elif self.is_falling:
            if self.x_y_moving == True:
                self.state[0] = 'running'
            else:
                self.updateState('idle', self.state[1])
        elif self.state[0] == 'attack':
            self.pre_attack_action == 'idle'
            self.x_y_moving = False

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new):
        self.__health = new
        if self.health <= 0:
            self.alive = False
            #self.kill()
            return
        self.healthbar.updateHealth()

    @property
    def max_health(self):
        return self.__max_health

    @max_health.setter
    def max_health(self, new):
        self.healthbar.max_health = new
        self.health += new - self.max_health
        self.__max_health = new

class HealthBar:
    ''' Health Bar class
    
    Manages a graphical representation of each characters health.
    Positioned above the characters head.  When health > 50% in green,
    When health > 20 in Orange, else in red.
    Works by extracting current character 
    '''
    def __init__(self, character):
        ''' __init__ function

        Loads character data and sets up initial health bar above 
        characters head
        '''
        # Extracting Character variables
        self.character = character
        self.max_health = character.max_health
        self.health = character.health
        self.screen = self.character.screen

        # Get character position variables
        self.char_height = self.character.rect.height
        self.char_width = self.character.rect.width
        self.y_shift = (self.char_height // 2) + self.char_height // 10
        self.generatePositions()

        # Get Health bar dims
        self.height = self.char_height // 15
        self.init_width = self.char_width
        self.width = self.char_width
        

        # Setting up surface variables
        self.back_surf = pygame.Surface((self.width, self.height))
        self.back_surf.fill((0, 0, 0))
        self.back_rect = pygame.Rect((  self.x, self.y,
                                        self.width, self.height))

        self.front_surf = pygame.Surface((self.width, self.height))
        self.front_surf.fill((35, 121, 7))
        self.front_rect = pygame.Rect(( self.x, self.y, 
                                        self.width, self.height))
        
    def display(self):
        ''' display

        Gets up to date healthbar positions from character and blits 
        fore and background healthbars
        '''
        self.generatePositions()

        # Blit background surface
        self.back_rect.center = (self.x, self.y)
        self.screen.blit(self.back_surf, self.back_rect)

        # Blit foreground surface
        self.front_rect.topleft = self.back_rect.topleft
        self.screen.blit(self.front_surf, self.front_rect)

        #print(f'{self.health} / {self.max_health} ')

    def generatePositions(self):
        ''' generate positions
        
        Generates x and y positions of health bar from characters
        '''
        self.x = self.character.rect.centerx
        self.y = self.character.rect.centery - self.y_shift

    def updateHealth(self):
        ''' Called by character when it loses (or gains) health.  This 
        updates the surfaces in the health bar that get blitted to the 
        screen
        '''
        self.health = self.character.health
        self.width = int(((self.health) / self.max_health) \
                            * self.init_width )
        self.front_surf = pygame.Surface((self.width, self.height))
        percentage = self.width / self.init_width
        if percentage > 0.5:
            colour = (35, 121, 7) # Deep green
        elif percentage > 0.2:
            colour = (255, 180, 0) # Orange
        else:
            colour = (255, 0, 0) # Red
        self.front_surf.fill(colour)
