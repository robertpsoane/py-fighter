''' Background Class


'''
import pygame

##### TO BE PUT IN A JSON
stone_image = 'graphics/map_tiles/tile1.png'
grass_image = 'graphics/map_tiles/tile2.png'
#####


# Loading images for tiles
STONE = pygame.image.load(stone_image)
GRASS = pygame.image.load(grass_image)


class Background:
    def __init__(self, screen, screen_dims, cell):
        self.createGameMap(screen_dims, cell)
        self.cell = cell
        self.screen = screen
        self.dims = screen_dims

        self.generateMap()

    def createGameMap(self, dims, cell):
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

    def generateMap(self):
        ''' generateMap()

        Generates map group from map matrix - stored as self.map_group

        '''

        ### Create map_group
        map_group = pygame.sprite.Group()

        game_map = self.map_matrix
        for i in range(self.height_units):
            for j in range(self.width_units):
                if game_map[i][j] == '1':
                    cell = self.cell
                    position = (j * cell, i * cell)

                    # Add individual tile sprite to map group
                    map_group.add(Tile(self.screen, position, cell, '1'))
                elif game_map[i][j] == '2':
                    cell = self.cell
                    position = (j * cell, i * cell)
                    map_group.add(Tile(self.screen, position, cell, '2'))

        # Store map_group to self
        self.map_group = map_group

    def display(self):
        # Blit all tiles in map group
        for tile in self.map_group:
            tile.display()


class Tile(pygame.sprite.Sprite):
    ''' Tile

    Implements tile sprite.
    Input:
        - screen to blit on to
        - screen dims
        - cell size (32)
        - tile_type '1' or '2'

    Has a display function to blit to screen
    '''
    def __init__(self, screen, dims, cell, tile_type):
        # Init for sprite
        pygame.sprite.Sprite.__init__(self)

        self.type = tile_type
        self.screen = screen
        self.dims = dims

        if self.type == '1':
            self.image = STONE
        elif self.type == '2':
            self.image = GRASS

        self.rect = self.image.get_rect()
        self.rect.topleft = [dims[0], dims[1]]

    def display(self):
        self.screen.blit(self.image, self.rect)
