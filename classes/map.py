''' Map Class

The class has the capability to generate a map and display it.
###At the moment the map is generated with a hard coded matrix.### TODO - Change to dynamically generated one

@author: Rokas Danevicius (unless stated otherwise)
'''

# Importing pygame.
import pygame
import random

# Load The tile paths in to variables
stone = 'graphics/map_tiles/tile1.png'
grass = 'graphics/map_tiles/tile2.png'
plat = 'graphics/map_tiles/plat32px.png'

# Load the images in to the program.
STONE = pygame.image.load(stone)
GRASS = pygame.image.load(grass)
PLATFORM = pygame.image.load(plat)


# Temporary hard coded map, will be changed to a dynamic map.
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
    '''This class is used to generate and display the map. The map is created with the use of a
    matrix. At the moment the matrix is hard coded in function createGameMap() above the class
    however this will changed to a method which generates the matrix dynamically. When the matrix
    is generated it is passed to a generateMap() method which reiterates through the matrix and
    checks the values of each element in it. Depending on the values of each element in the matrix
    the generateMap() method adds the position, tile type and the surface to which the tile should
    be printed on to the pygame.sprite.Group saved in map_group variable. Then the map_group is the
    passed to the Tile class writen by Robert Soane.'''

    def __init__(self, screen, dims, cell):

        self.screen = screen
        self.dims = dims
        self.cell = cell
        self.total_rows = 20
        self.columns = 25

        self.height_units = dims[1] // cell
        self.width_units = dims[0] // cell

        self.generateMap()

    def genMap(self):
        dirt_row = 1
        bottom_air = 10
        air_row = 3
        random_rows = 4
        tile_matrix = []

        top_air = [[0 for column in range(self.columns)] for row in range(air_row)]
        tile_matrix.extend(top_air)
        platforms = [[random.uniform(0, 1) for column in range(self.columns)] for row in
                     range(random_rows)]
        tile_matrix.extend(platforms)
        middle_air = [[0 for column in range(self.columns)] for row in range(dirt_row)]
        tile_matrix.extend(middle_air)
        top_dirt = [[2 for column in range(self.columns)] for row in range(dirt_row)]
        tile_matrix.extend(top_dirt)
        bottom_dirt = [[1 for column in range(self.columns)] for row in range(dirt_row)]
        tile_matrix.extend(bottom_dirt)
        bottom_air = [[0 for column in range(self.columns)] for row in range(bottom_air)]
        tile_matrix.extend(bottom_air)

        return tile_matrix

    def platformCheck(self, maplist, row, column):

        check = [[row, column], [row, column - 1], [row, column - 2], [row, column - 3],
                 [row, column - 4],
                 [row, column + 1], [row, column + 2], [row, column + 3], [row, column + 4],
                 [row - 1, column], [row - 1, column - 1], [row - 1, column - 2],
                 [row - 1, column - 3],
                 [row - 1, column - 4],
                 [row - 1, column + 1], [row - 1, column + 2], [row - 1, column + 3],
                 [row - 1, column + 4],
                 [row - 2, column], [row - 2, column - 1], [row - 2, column - 2],
                 [row - 2, column - 3],
                 [row - 2, column - 4],
                 [row - 2, column + 1], [row - 2, column + 2], [row - 2, column + 3],
                 [row - 2, column + 4]]

        for position in check:

            if position[1] > 24:
                return False
            elif maplist[position[0]][position[1]] == 3:
                return False

        return True

    def platformPlace(self, row, column):

        checking = [[row, column + 1], [row, column + 2], [row, column + 3], [row, column + 4]]

        for position in checking:
            if position[1] > 24:
                return False
        return True

    def readMap(self):
        tile_matrix = self.genMap()

        row = 0
        while row < self.total_rows:
            col = 0

            while col < self.columns:

                if (tile_matrix[row][col]) <= 0.5:
                    tile_matrix[row][col] = 0

                if 0.5 < (tile_matrix[row][col]) < 1:
                    if self.platformCheck(tile_matrix, row, col):
                        if self.platformPlace(row, col):
                            for x in range(random.randint(2, 4)):
                                tile_matrix[row][col + x] = 3
                    else:
                        tile_matrix[row][col] = 0

                col += 1

            row += 1
        return tile_matrix

    def randomiseMap(self):
        #self.map_group = []
        self.map_matrix = self.readMap()
        for i in self.map_matrix:
            for j in i:
                print(j, end=' ')
            print()

    def generateMap(self):
        '''
        Method which reiterates through the matrix and checks the values of each element in it.
        Depending on the values of each element in the  matrix the generateMap() method adds the
        position, tile type and the surface to which the tile should be printed on to the
        pygame.sprite.group saved in map_group variable .
        '''

        map_group = pygame.sprite.Group()
        self.map_matrix = self.readMap()

        for i in range(self.height_units):
            for j in range(self.width_units):
                # TODO: Can refactor this set of if statements into one if
                # statement

                if self.map_matrix[i][j] == 1:
                    cell = self.cell
                    position = (j * cell, i * cell)

                    # Add individual tile sprite to map group
                    map_group.add(Tile(self.screen, position, 1))
                elif self.map_matrix[i][j] == 2:
                    cell = self.cell
                    position = (j * cell, i * cell)
                    map_group.add(Tile(self.screen, position, 2))

                elif self.map_matrix[i][j] == 3:
                    cell = self.cell
                    position = (j * cell, i * cell)
                    map_group.add(Tile(self.screen, position, 3))

        # Store map_group to self
        self.map_group = map_group

    def display(self):
        # Blit all tiles in map group
        for tile in self.map_group:
            tile.display()


# Roberts Tile class
class Tile(pygame.sprite.Sprite):
    """ Tile

    Implements tile sprite.
    Input:
        - screen to blit on to
        - screen dims
        - tile_type '1' , '2' or '3'.

    Has a display function to blit to screen
    @author: Robert Soane
    """

    def __init__(self, screen, dims, tile_type):
        # Init for sprite
        pygame.sprite.Sprite.__init__(self)

        self.type = tile_type
        self.screen = screen
        self.dims = dims

        if self.type == 1:
            self.image = STONE
        if self.type == 2:
            self.image = GRASS
        if self.type == 3:
            self.image = PLATFORM

        self.rect = self.image.get_rect()
        self.rect.topleft = [dims[0], dims[1]]

    def display(self):
        '''
        Display method to blit the map to screen.
        '''


        self.screen.blit(self.image, self.rect)

        ###################################################
        # TODO DELETE THE FOLLOWING CODE - FOR TESTING ONLY
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill((0, 100, 100))
        surf.set_alpha(50)
        self.screen.blit(surf, self.rect)
        ###################################################

