import pygame


def createGameMap():
    game_map = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0',],
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

    return game_map


class Map:
    """Poopty Skoopty"""

    TILE_SIZE = 32

    def __init__(self, grass_image, dirt_image, game_display):
        self.grass_image = grass_image
        self.dirt_image = dirt_image
        self.game_display = game_display
        self.game_map = createGameMap()

    def generateMap(self):
        y = 0
        for row in self.game_map:
            tile_box = []
            x = 0
            for tile in row:
                if tile == '2':
                    self.game_display.blit(self.dirt_image, (x * Map.TILE_SIZE, y * Map.TILE_SIZE))
                if tile == '1':
                    self.game_display.blit(self.grass_image, (x * Map.TILE_SIZE, y * Map.TILE_SIZE))
                if tile != '0':
                    tile_rect = pygame.Rect(
                        x * Map.TILE_SIZE,
                        y * Map.TILE_SIZE,
                        Map.TILE_SIZE,
                        Map.TILE_SIZE
                    )
                    tile_box.append(tile_rect)
                x += 1
            y += 1

    def collisionTest(self, rect, tiles):
        self.rect = rect
        self.tiles = tiles
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
            return hit_list

    def objectMove(self, rectm, movementm, tilesm):
        self.movementm = movementm
        self.tilesm = tilesm
        collision_types = {'top: False', 'bottom: False', 'right: False', 'left: False'}
        self.rectm.x += movmentm[0]
        return rectm, collision_types
    def display(self):
        self.generateMap()
