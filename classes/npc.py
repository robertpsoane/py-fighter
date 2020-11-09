''' NPC Class


'''

import json
from classes.character import Character

class NPC(Character):

    ''' NPC Class - Used to display and animate computer controlled characters
    on the screen.  A type needs to be chosen to match the enemy json in the 
    json folder.
    '''

    def __init__(self, screen, background, x_position, y_position, type = 'basic'):
        # Loading player data json, and converitng to python dictionary
        json_location = f'json/{type}_enemy.JSON'
        try:
            with open(json_location) as player_json:
                character_data = json.load(player_json)
        except:
            err_string = "Bad Enemy Name.  Please input an enemy which has a corresponding JSON"
            raise Exception(err_string)
        # Initialising Character class
        Character.__init__(self, character_data, background, screen, x_position, y_position)
    
    def addTarget(self,target):
        ''' addTarget - Used to lock NPC onto a target to attack
        '''
        Character.addTarget(self, target)

        # Centre to centre width
        self.c2c_width = 0.5 * (self.width + self.target.width)
    
    def display(self):
        ''' NPC display function.

        This function examines position of target, makes move based on target,
        then displays to the screen.
        '''
        # Deciding on and actioning any moves
        self.decideMoves()

        # Calling parent display function
        Character.display(self)

    def decideMoves(self):
        # Getting positions
        self_x = self.position[0]
        self_y = self.position[1]
        target_x = self.target.position[0]
        target_y = self.target.position[1]

        # Difference in x positions
        x_dif = self_x - target_x
        y_dif = self_y - target_y

        if x_dif > self.c2c_width:
            self.startMove('l')
        elif x_dif <  -1 * self.c2c_width:
            self.startMove('r')