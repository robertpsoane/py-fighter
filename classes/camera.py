'''
@author: Rokas Danevicius (unless stated otherwise)
'''


class Camera:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.sprites = []
        self.world_x = x

    def addBack(self, background_object):
        self.background_scroll = background_object

    def addMap(self, map_obj):
        self.map = map_obj

    def add(self, sprite):
        self.sprites.append(sprite)
        self.init_player = self.sprites[0]
        self.init_position = self.init_player.position[0]

# TODO rename the init_position

    def scroll(self):

        map_width = self.map.dims[0] - 400

        if self.world_x > map_width:
            self.x = 0
            self.world_x = map_width
        elif self.world_x < 0:
            self.x = 0
            self.world_x = 0
        else:

            self.background_scroll.move += self.x

            for tile in self.map.map_group:
                tile.rect.centerx -= self.x

            for sprite in self.sprites:
                sprite.rect.centerx -= self.x

            self.player = self.sprites[0]

            self.x = (self.player.rect.centerx - 400 / 2)


            self.world_x += self.x




