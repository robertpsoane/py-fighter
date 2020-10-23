''' Player Class


'''
from classes.character import Character

class Player(Character):
    def __init__(self, screen, x_position, y_position):
        ### Setting up mapping from sprite sheet to images
        ### This will become a JSON
        running = {
            'left': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 0),
                    (0, 4), (0, 5), (0, 6)],
            'right': [(2, 0), (2, 1), (2, 2), (2, 3), (2, 0),
                    (2, 4), (2, 5), (2, 6)]
        }

        idle = {
            'left': [(0, 0), (1, 0)],
            'right': [(2, 0), (3, 0)]
        }
        
        self.character_data = {
            'actions': ['running','idle'],
            'directions': ['left','right'],
            'running': running,
            'idle': idle,
            'path': 'graphics/spritesheets/basic-character.png',
            'background': (0, 255, 0),
            'gridsize': (4, 9),
            'charsize': (32, 32),
            'scaledsize': (128, 128),
            'speed': 1,
            'gravity': 1,
            'refresh': 10,
            'initialstate': ['running','right']

        }

        Character.__init__(self, screen, x_position, y_position)

    