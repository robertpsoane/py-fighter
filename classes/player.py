''' Player Class

Player class of py-fighter game.
Inherits from Character.  Initialises by loading basic_character JSON and 
initialising as Character.

This is distinct from the NPC class, as the NPC class will have a basic AI
built in to attack the player, whereas the player is fairly simple.

'''
import pygame
import json
from classes.character import Character

class Player(Character):

    ''' Player Class - Used to display and animate human controlled characters
    on the screen.
    '''

    def __init__(self, screen, background, x_position, y_position):
        # Loading player data json, and converitng to python dictionary
        with open('json/basic_character.JSON') as player_json:
            character_data = json.load(player_json)

        # Initialising Character class
        Character.__init__(self, character_data, background, screen, x_position, y_position)

    def addTarget(self, target_group):
        self.target_group = target_group

    def attack(self):
        collision_enemies = pygame.sprite.spritecollide(self, self.target_group, False)
        for collision_enemy in collision_enemies:
            Character.attack(self, collision_enemy)
    