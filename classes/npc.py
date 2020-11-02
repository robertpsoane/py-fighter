''' NPC Class


'''

import json
from classes.character import Character

class NPC(Character):
    def __init__(self, screen, x_position, y_position, type = 'basic'):
        # Loading player data json, and converitng to python dictionary
        json_location = 'json/{}_enemy.JSON'
        try:
            with open(json_location) as player_json:
                character_data = json.load(player_json)
        except:
            err_string = "Bad Enemy Name.  Please input an enemy which has a corresponding JSON"
            raise Exception(err_string)
        # Initialising Character class
        Character.__init__(self, character_data, screen, x_position, y_position)