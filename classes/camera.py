''' Camera Class

The class which creates a camera view for the game which fallows the player.

@author: Rokas Danevicius (unless stated otherwise)
'''


class Camera:
    '''
    The class which creates a camera view for the game which fallows the player on the x axes.
    The class does so by updating the x value of each objects drawn of the game_display. The
    position of the camera view is determined by the position of player character position on x
    axes. The class is also able to fallow the player on y axes if one wishes to.
    '''


    def __init__(self, screen, x=0, y=0):

        # x and y values used to update the x or y values of other blited objects.
        self.x = x
        self.y = y

        # List used to save the name of character Class instances.
        self.sprites = []

        # Map width
        self.map_width = screen.get_width()
        self.map_view = self.map_width // 2


        # Create a variable to follow Players position in the map when camera is not working.
        self.world_x = x

    def addBack(self, background_object):
        ''' Access the variables of background class instance.'''
        self.background_scroll = background_object

    def addMap(self, map_obj):
        ''' Access the variables of Map class instance.'''
        self.map = map_obj

    def addPlayer(self, player):
        self.sprites = [player]

        # Locks the camera to the player sprite.
        self.player = self.sprites[0]

    def addWeapon(self, weapon):
        pass

    def add(self, sprite):
        ''' Access the variables of all Character class instance.'''
        self.sprites.append(sprite)
        # self.init_player = self.sprites[0]
        # self.init_position = self.init_player.position[0]

# TODO rename the init_position

    def scroll(self):
        ''' Method which updates the x values of objects which are blited to game_display'''

        # Creates a variable for the visible map width.
        map_width = self.map.dims[0] - self.map_view

        # Creating boarders for the camera view.
        # Stops the camera moving if the camera hits the left side of the level.
        if self.world_x > map_width:
            self.x = 0
            self.world_x = map_width

        # Stops the camera moving if the camera hits the right side of the level.
        elif self.world_x < 0:
            self.x = 0
            self.world_x = 0

        # Camera moves, the values of x values of objects that are not the player get updated.
        else:
            current_offset = (self.player.rect.centerx - self.map_view / 2)
            if self.world_x + current_offset > map_width:
                return
            if self.world_x + current_offset < 0:
                return
            # Moves the background objects. Updates their x value.
            self.background_scroll.move += self.x

            # Moves the Map sprite. Updates its x value.
            for tile in self.map.map_group:
                tile.rect.centerx -= self.x

            # Moves the player and NPC sprites. Updates their x values.
            for sprite in self.sprites:
                sprite.rect.centerx -= self.x

            self.x = (self.player.rect.centerx - self.map_view / 2)

            self.world_x += self.x






