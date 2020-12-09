''' Player Class

Player class of py-fighter game.
Inherits from Character.  Initialises by loading basic_character JSON 
and initialising as Character.

This is distinct from the NPC class, as the NPC class will have a basic 
AI built in to attack the player, whereas the player is fairly simple.

@author: Robert (Unless stated otherwise)
'''
import pygame
import json
from classes.character import Character
from classes.weapon import Arms

class Player(Character):

    ''' Player Class - Used to display and animate human controlled 
    characters on the screen.
    '''
    
    max_uses = 5

    def __init__(self, screen, background, x_position, y_position, 
                                                arm_type = 'arms'):
        # Loading player data json, and converitng to python dictionary
        with open('json/basic_character.JSON') as player_json:
            character_data = json.load(player_json)

        # Initialising Character class
        Character.__init__(self, character_data, background, screen, 
                                    x_position, y_position, arm_type)

    def attack(self):
        ''' attack function

        Checks for any enemies in target group who have collided and 
        attacks them
        '''
        self.attacking = True
        if self.arms.projectile:
            boom = self.arms.throw(self.state[1])
            self.thrown_projectiles.add(boom)
        else:
            collision_enemies = pygame.sprite.spritecollide(self, 
                                            self.target_group, False)
            for collision_enemy in collision_enemies:
                if self.isFacingTarget(collision_enemy):
                    Character.attack(self, collision_enemy)
    
    def update(self):
        ''' Update
        Updates using parent classes update function, then ensures still
        on screen
        '''
        #print(self.score)
        Character.update(self)
        # Preventing from going off edges
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
    