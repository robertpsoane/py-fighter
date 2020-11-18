'''
@author: Rokas Danevicius (unless stated otherwise)
'''


class Camera:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.sprites = []

    def addMap(self, map_obj):
        self.map = map_obj

    def add(self, sprite):
        self.sprites.append(sprite)
        self.init_player = self.sprites[0]
        self.init_position = self.init_player.position[0]

    """
    def cameraTrack(self):
        self.init_position += 2

    def cameraMove(self, direction):
        if direction == 'r':
            self.cameraTrack()
        if direction == "l":
            self.init_position += -1 * 2
    """


    def scroll(self):

        if self.init_position <= 100 or self.init_position >= 800:


            self.player = self.sprites[0]
            self.x += 0

        else:
            for tile in self.map.map_group:
                tile.rect.centerx -= self.x

            for sprite in self.sprites:
                sprite.rect.centerx -= self.x

            self.player = self.sprites[0]
            self.x += (self.player.rect.centerx - self.x - 200)
            self.init_position -= self.x


