''' NPC Class


@author: Robert (Unless stated otherwise)
'''
import pygame
import json
from classes.character import Character

class NPC(Character):

    ''' NPC Class - Used to display and animate computer controlled 
    characters on the screen.  A type needs to be chosen to match the 
    enemy json in the json folder.

    The NPC uses some very basic logic to give the NPCs some apparent 
    autonomy. With each display of the screen,
    '''
    max_uses = -1
    def __init__(self, screen, background, x_position, y_position,
                npc_type = 'basic', arm_type = 'arms', sleep_on_load = True):
        # Loading player data json, and converitng to python dictionary
        json_location = f'json/{npc_type}_enemy.JSON'
        try:
            with open(json_location) as character_json:
                character_data = json.load(character_json)
        except:
            err_string = "Bad Enemy Name.  Please input an enemy which has \
                            a corresponding JSON"
            raise Exception(err_string)

        # Initialising Character class
        Character.__init__(self, character_data, background, screen, 
                                    x_position, y_position, arm_type)

        # Setup sleep variable
        self.asleep = sleep_on_load

        # Attack delay - a delay of a number of frames to give player 
        # opportunity of attacking first
        if self.arms.projectile:
            self.attack_delay = 100
        else:
            self.attack_delay = 15
        self.attack_counter = 0

        # Kill NPC if falls off map
        self.max_depth = screen.get_size()[1]

        # Wake distance (pixels) - used to determine distance target 
        # needs to be after which NPC wakes.
        # This should go somewhere else, like a JSON perhaps? 
        # TODO: Decide!
        self.wake_distance = 200

    def addTarget(self, target_group):
        ''' addTarget - Used to lock NPC onto a target to attack
        '''
        Character.addTarget(self, target_group)
        # Sorry this line is messy! was playing in the debugger and 
        # found it works
        self.target = target_group.sprites()[0]


        # TODO: Redo c2c_widtrh and methods which use it
        # Centre to centre width
        self.c2c_width = 0.5 * (self.width + self.target.width)
        self.c2c_height = 0.5 * (self.height + self.target.height)

    def update(self):
        ''' NPC update function

        This function examines position of target, makes move based on 
        target, then uses parent classes update funciton
        '''
        if self.position[1] > self.max_depth:
            self.kill()
        # Deciding on and actioning any moves
        self.decideMoves()

        Character.update(self)
        

    
    def display(self):
        ''' NPC display function.

        This function examines position of target, makes move based on
        target, then displays to the screen.
        '''

        # Calling parent display function
        Character.display(self)

    def stillAsleep(self):
        ''' Still asleep function

        Checks if character is still asleep, and can be wokenn.  If 
        still asleep, returns True, else returns False.
        '''

        if self.asleep:
            if self.withinWakeDistance():
                self.asleep = False
                return False
            else:
                return True
        return False

    def decideMoves(self):
        ''' decideMoves - forms the basis for our 'AI'
        Check x and y position of target, and x and y position of self.
        Use simple comparison of positions to decide whether or not to 
        attack
        '''
        
        # If asleep, don't check for moves
        if self.stillAsleep():
            return

        # Getting positions as local variables to make code read easier
        self_x, self_y, target_x, target_y = self.getPositionsAsLocal()

        # Difference in x and y positions
        x_dif = self_x - target_x
        y_dif = self_y - target_y

        if self.arms.projectile:
            if -10 < y_dif < 10:
                if self.attack_counter == self.attack_delay:
                    self.attack_counter = 0
                    self.attacking = True
                    boom = self.arms.throw(self.state[1])
                    self.thrown_projectiles.add(boom)
                else:
                    self.attack_counter += 1
        else:
            # If possible, attack
            if pygame.sprite.collide_rect(self, self.target) \
                            and self.isFacingTarget(self.target):
                
                if self.attack_counter == self.attack_delay:
                    self.attack_counter = 0
                    self.attacking = True
                    self.attack(self.target)
                else:
                    self.attack_counter += 1
        
        # move in right direction
        if x_dif > self.c2c_width:
            self.startMove('l')
        elif x_dif <  -1 * self.c2c_width:
            self.startMove('r')
        elif (not self.is_jumping) and y_dif > self.c2c_width:
            self.startMove('u')
    
    def withinWakeDistance(self):
        ''' withinWakeDistance - returns whether target is within NPCs 
        wake
        distance
        '''
        # Getting positions as local variables to make code read easier
        self_x, self_y, target_x, target_y = self.getPositionsAsLocal()

        # x and y differences
        x_diff, y_diff = self_x - target_x, self_y - target_y

        # Squared differences
        sqr_diff = (x_diff ** 2) + (y_diff ** 2)
        sqr_wake_distance = self.wake_distance ** 2
        if sqr_diff < sqr_wake_distance:
            return True
        else:
            return False


    def getPositionsAsLocal(self):
        ''' getPositionsAsLocal - returns positions of self and target

        returns selfs x, y and targets x, y

        This function is used solely to return positions of self and 
        target to make the code more readable as we don't need to carry 
        round self.target.postition[0], etc
        '''
        self_x = self.rect.centerx
        self_y = self.rect.centery
        target_x = self.target.rect.centerx
        target_y = self.target.rect.centery
        return self_x, self_y, target_x, target_y
