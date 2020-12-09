''' Map Class

The class has the capability to generate a map with random platforms and
display it. The idea of storing a map in to matrix is
take from here: https://www.youtube.com/watch?v=HCWI2f7tQnY&t=58s
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

class Map:
    '''
    This class is used to generate and display the map. The map is 
    created with the use of a matrix. At the moment the matrix is hard 
    coded in function createGameMap() above the class however this will 
    changed to a method which generates the matrix dynamically. When the
    matrix is generated it is passed to a generateMap() method which 
    reiterates through the matrix and checks the values of each element 
    in it. Depending on the values of each element in the matrix the 
    generateMap() method adds the position, tile type and the surface to
    which the tile should be printed on to the pygame.sprite.Group saved
    in map_group variable. Then the map_group is the passed to the Tile
    class writen by Robert Soane. The idea of storing a map in to matrix
    is take from here: https://www.youtube.com/watch?v=HCWI2f7tQnY&t=58s
    '''

    def __init__(self, screen, dims, cell):

        self.screen = screen
        self.dims = dims
        self.cell = cell
        self.total_rows = 20
        self.columns = 25

        self.height_units = dims[1] // cell
        self.width_units = dims[0] // cell

        self.generateMap()

    def randomMatrix(self):
        '''
        The method creates a matrix which contains rows with fixed and
        randomised values.
        '''

        # Create iteration values for different rows containing specific
        # values.
        dirt_row = 1
        bottom_air = 10
        air_row = 3
        random_rows = 4

        # Empty list which will be filled up with rows containing 
        # different values.
        tile_matrix = []

        # Creates rows which will represent the air at the top part of 
        # the map.
        top_air = [[0 for column in range(self.columns)]
                        for row in range(air_row)]
        tile_matrix.extend(top_air)

        # Creates rows containing random possibilities which will 
        # represent platforms in the map.
        platforms = [[random.uniform(0, 1) for column in range(self.columns)]
                        for row in range(random_rows)]
        tile_matrix.extend(platforms)

        # Creates a row to represent an empty portion of the map between
        # the platform and ground layer.
        middle_air = [[0 for column in range(self.columns)]
                                for row in range(dirt_row)]
        tile_matrix.extend(middle_air)

        # Creates a row which represent the first ground layer of the 
        # map.
        top_dirt = [[2 for column in range(self.columns)]
                                for row in range(dirt_row)]
        tile_matrix.extend(top_dirt)

        # Creates a row which represents the second layer of the ground 
        # in the map.
        bottom_dirt = [[1 for column in range(self.columns)]
                                for row in range(dirt_row)]
        tile_matrix.extend(bottom_dirt)

        # Creates a row which represents the non visible map par of air 
        # under the ground.
        bottom_air = [[0 for column in range(self.columns)]
                                for row in range(bottom_air)]
        tile_matrix.extend(bottom_air)

        # Returns the full matrix with all of the rows added together.
        return tile_matrix

    def platformCheck(self, maplist, row, column):
        '''
        The method checks if the place where the game wants to place a 
        platform is valid. This method checks if there are any platforms
        that are two close vertically, horizontally and diagonally. If 
        the previous platforms are to close the method returns False 
        telling the game that a platform cant be placed there.
        '''

        # A list of list containing the locations which will be checked 
        # for already existing platforms.
        check = [[row, column], [row, column - 1], [row, column - 2], 
                [row, column - 3], [row, column - 4], [row, column + 1],
                [row, column + 2], [row, column + 3], [row, column + 4],
                [row - 1, column], [row - 1, column - 1], 
                [row - 1, column - 2], [row - 1, column - 3],
                [row - 1, column - 4], [row - 1, column + 1],
                [row - 1, column + 2], [row - 1, column + 3],
                [row - 1, column + 4], [row - 2, column], 
                [row - 2, column - 1], [row - 2, column - 2],
                [row - 2, column - 3], [row - 2, column - 4],
                [row - 2, column + 1], [row - 2, column + 2],
                [row - 2, column + 3], [row - 2, column + 4]]

        # The for loop which iterates through all of the check positions.
        for position in check:

            # Prevents the loop from checking positions in the map 
            # matrix which do not exist.
            if position[1] > 24:
                return False

            # Check if the position is valid and there are no other 
            # platforms near by. If there is platform the method returns
            # False else it gives True.
            elif maplist[position[0]][position[1]] == 3:
                return False

        return True

    def platformPlace(self, row, column):
        ''' This method checks if the platform about to be placed wont 
        extend over the boundaries of the map. Which out the check we 
        would get an index error
        if the platform about the be placed would be next to an edge of
        the map'''

        # A list of lists which contains the positions to check if the 
        # platform is about to be placed over the maps edge.
        checking = [[row, column + 1], [row, column + 2], [row, column + 3],
                                                            [row, column + 4]]

        # For loop which caries out the check by iterating through the 
        # "checking" list of lists If the position with the given check 
        # value is bigger then the map length which in this case is 24 
        # elements of the map matrix it returns false and the platform 
        # is not placed there.

        for position in checking:
            if position[1] > 24:
                return False
        return True


    def readMap(self):
        '''
        This method iterates through the tile matrix provided by 
        "randomMatrix()" method. This method ignores all of the values 
        in the matrix which are "1" or above "1". By doing so all of the
        values that are not random stay the same and represent the non 
        changing tiles of the map. Everything which is bellow the value 
        of "1" will be changed to either "0" which is the air tile or 
        "3" which is a platform. This is determined by the while loop in
        this method. If the while loop receives an object from the
        matrix containing a value bellow "0.5" it assigns the object a 
        value of "0" which represents the air. If the value is between 
        "0.5" and "1" the loop give the value of "3" to the object which
        represents a platform.
        '''
        tile_matrix = self.randomMatrix()

        row = 0
        while row < self.total_rows:
            col = 0

            while col < self.columns:

                # If the while loop receives an object
                # from the matrix containing a value
                # bellow "0.5" it assigns
                # the object a value of "0"
                # which represents the air.
                if (tile_matrix[row][col]) <= 0.5:
                    tile_matrix[row][col] = 0

                # If the value is between "0.5" and "1" the loop give 
                # the value of "3" to the object which represents a 
                # platform.
                if 0.5 < (tile_matrix[row][col]) < 1:

                    # This is where we check if the platform can be 
                    # placed.
                    if self.platformCheck(tile_matrix, row, col):
                        if self.platformPlace(row, col):
                            for x in range(random.randint(2, 4)):
                                tile_matrix[row][col + x] = 3
                    # If the platform check are false there will be air 
                    # instead of the platform.
                    else:
                        tile_matrix[row][col] = 0

                col += 1

            row += 1
        return tile_matrix


    def generateMap(self):
        '''
        Method which reiterates through the matrix and checks the values
        of each element in it. Depending on the values of each element
        in the  matrix the generateMap() method adds the position, tile
        type and the surface to which the tile should be printed on to 
        the pygame.sprite.group saved in map_group variable .
        '''

        map_group = pygame.sprite.Group()
        self.map_matrix = self.readMap()

        for i in range(self.height_units):
            for j in range(self.width_units):
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

    found rect.inflate_ip on pygame documentation

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
            self.rect = self.image.get_rect()
            self.rect.topleft = [dims[0], dims[1]]

        if self.type == 2:
            self.image = GRASS
            self.rect = self.image.get_rect()
            self.rect.topleft = [dims[0], dims[1]]

        if self.type == 3:
            self.image = PLATFORM
            self.rect = self.image.get_rect()
            # Making platform rect smaller
            new_rect_height = - self.rect.height + 1 * (self.rect.height // 5)
            self.rect.inflate_ip(0, new_rect_height)
            self.rect.topleft = [dims[0], dims[1]]



    def display(self):
        '''
        Display method to blit the map to screen.
        '''
        self.screen.blit(self.image, self.rect)
