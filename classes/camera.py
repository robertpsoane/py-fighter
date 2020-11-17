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

    def scroll(self):

        for tile in self.map.map_group:
            tile.rect.centerx -= self.x

        for sprite in self.sprites:
            sprite.rect.centerx -= self.x

        self.player = self.sprites[0]
        self.x += (self.player.rect.centerx-self.x-200)

