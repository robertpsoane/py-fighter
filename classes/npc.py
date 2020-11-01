''' NPC Class


'''

class NPC:
    def __init__(self, screen, x_position, y_position):
        # Loading player data json, and converitng to python dictionary
        with open('json/basic_enemy.JSON') as player_json:
            character_data = json.load(player_json)

        # Initialising Character class
        Character.__init__(self, character_data, screen, x_position, y_position)