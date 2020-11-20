'''
@author: Rokas Danevicius (unless stated otherwise)
'''

# TODO: Document code before merging with master
# TODO: Currently no display function in Map - players can detect collisions
# but you can't see the images yet
import pygame

from classes.camera import Camera

# Load The tile paths in to variables
stone = 'graphics/map_tiles/tile1.png'
grass = 'graphics/map_tiles/tile2.png'
plat = 'graphics/map_tiles/plat32px.png'

# Load the images.
STONE = pygame.image.load(stone)
GRASS = pygame.image.load(grass)
PLATFORM = pygame.image.load(plat)


# Temporary hard coded map
def createGameMap():
    map_matrix = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0', ],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2',
         '2', '2', '2', '2', '2', '2', '2'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
         '1', '1', '1', '1', '1', '1', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0']]

    return map_matrix


class Map:
    '''Poopty Skoopty'''

    # TODO: TILE_SIZE should not be class variable but should be passed in
    # when Map class initiated - doesn't matter what its called, but thats
    # what cell was doing on the other branch when I got it working. Please
    # add the variable to the config file and it can be passed into controller
    # and then Map when initiated
    TILE_SIZE = 32

    def __init__(self, screen, dims, cell):
        self.grass_image = GRASS
        self.dirt_image = STONE
        self.plat_image = PLATFORM
        self.screen = screen
        self.dims = dims
        self.cell = cell

        self.height_units = dims[1] // cell
        self.width_units = dims[0] // cell

        ## the create map_matrix bit could probably go within the generateMap
        ## function, as it is needed each time we get a new map?
        ## I know my hacked together version had it differently but not
        ## probably better to change it :)
        self.createGameMapDYNAMIC(dims, cell)
        self.generateMap()

    # Reads through the map matrix and blits the tiles on game_display, also adds them to map group.
    def generateMap(self):
        map_group = pygame.sprite.Group()
        game_map = createGameMap()

        for i in range(self.height_units):
            for j in range(self.width_units):
                # TODO: Can refactor this set of if statements into one if
                # statement

                if game_map[i][j] == '1':
                    cell = self.cell
                    position = (j * cell, i * cell)

                    # Add individual tile sprite to map group
                    map_group.add(Tile(self.screen, position, '1'))
                elif game_map[i][j] == '2':
                    cell = self.cell
                    position = (j * cell, i * cell)
                    map_group.add(Tile(self.screen, position, '2'))

                elif game_map[i][j] == '3':
                    cell = self.cell
                    position = (j * cell, i * cell)
                    map_group.add(Tile(self.screen, position, '3'))

        # Store map_group to self
        self.map_group = map_group

    def display(self):
        # Blit all tiles in map group
        for tile in self.map_group:
            tile.display()

    # TODO: If you choose to keep this function, rename it something more
    # sensible than DYNAMIC :) I just named it that so its clear its a
    # separat function for th patch
    def createGameMapDYNAMIC(self, dims, cell):
        ''' Dynamic Creating Game Map

        Dynamically generates a map matrix for a map of a given size and cell
        size
        '''

        # Feel free to replace, just using to quickly get patch working.
        # The hard coded game map isn't the right size for the game screen at
        # the moment, so instead of counting elements I used a dynamic
        # function

        # Dynamically generate game map matrix
        height_units = dims[1] // cell
        width_units = dims[0] // cell
        ground_start = height_units - 4

        map_matrix = []
        for i in range(height_units):
            row = []
            for j in range(width_units):
                if i < ground_start:
                    row.append('0')
                elif i == ground_start:
                    row.append('2')
                else:
                    row.append('1')
            map_matrix.append(row)

        self.height_units = height_units
        self.width_units = width_units
        self.map_matrix = map_matrix


# Roberts Tile class
class Tile(pygame.sprite.Sprite):
    """ Tile

    Implements tile sprite.
    Input:
        - screen to blit on to
        - screen dims
        - tile_type '1' or '2'

    Has a display function to blit to screen
    """

    def __init__(self, screen, dims, tile_type):
        # Init for sprite
        pygame.sprite.Sprite.__init__(self)

        self.type = tile_type
        self.screen = screen
        self.dims = dims

        if self.type == '1':
            self.image = STONE
        if self.type == '2':
            self.image = GRASS
        if self.type == '3':
            self.image = PLATFORM

        self.rect = self.image.get_rect()
        self.rect.topleft = [dims[0], dims[1]]

    def display(self):
        self.screen.blit(self.image, self.rect)
