# TODO: Document code before merging with master

import pygame

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
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
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

    def __init__(self, screen, screen_dims):
        self.grass_image = GRASS
        self.dirt_image = STONE
        self.plat_image = PLATFORM
        self.screen = screen 
        self.dims = screen_dims

        ## the create map_matrix bit could probably go within the generateMap
        ## function, as it is needed each time we get a new map?
        ## I know my hacked together version had it differently but not 
        ## probably better to change it :)
        self.map_matrix = createGameMap()
        self.generateMap()

    # Reads through the map matrix and blits the tiles on game_display, also adds them to map group.
    def generateMap(self):
        map_group = pygame.sprite.Group()
        y = 0
        for row in self.map_matrix:
            x = 0
            for tile in row:
                if tile == '3':
                    position = (row * Map.TILE_SIZE, tile * Map.TILE_SIZE)
                    self.screen.blit(self.plat_image, (x * Map.TILE_SIZE, y * Map.TILE_SIZE))
                    map_group.add(Tile(self.screen, position, '3'))
                if tile == '2':
                    position = (row * Map.TILE_SIZE, tile * Map.TILE_SIZE)
                    self.screen.blit(self.dirt_image, (x * Map.TILE_SIZE, y * Map.TILE_SIZE))
                    map_group.add(Tile(self.screen, position, '2'))
                if tile == '1':
                    position = (tile * Map.TILE_SIZE, tile * Map.TILE_SIZE)
                    self.screen.blit(self.grass_image, (x * Map.TILE_SIZE, y * Map.TILE_SIZE))
                    map_group.add(Tile(self.screen, position, '1'))

                x += 1
            y += 1
        self.map_group = map_group


# Roberts Tile class
class Tile(pygame.sprite.Sprite):
    """ Tile

    Implements tile sprite.
    Input:
        - screen to blit on to
        - screen dims
        - cell size (32)
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
