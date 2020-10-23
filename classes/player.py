''' Player Class


'''
import json
from classes.character import Character

class Player(Character):
    def __init__(self, screen, x_position, y_position):
        # Loading player data json, and converitng to python dictionary
        with open('json/basic_character.JSON') as player_json:
            self.character_data = json.load(player_json)

        # Initialising Character class
        Character.__init__(self, screen, x_position, y_position)

    