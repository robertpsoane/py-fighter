import pygame

background_objects = [[0.25, [0, 0]], [0.25, [256, 0]], [0.5, [0, 64]], [0.5, [192, 64]],
                      [0.5, [384, 64]], [0.5, [576, 64]]]

back1 = pygame.image.load('graphics/background_sprite/back_1.png')
back1 = pygame.transform.scale(back1, (192, 192))

super_back1 = pygame.image.load('graphics/background_sprite/back_super_1.png')
super_back1 = pygame.transform.scale(super_back1, (128 * 2, 128 * 2))


class Background:

    def __init__(self, screen, objects=0):
        self.objects = objects
        self.display = screen
        self.move = 0

    def displayQ(self):



        for background_object in background_objects:
            self.objects = (background_object[1][0] - self.move * background_object[0],
                            background_object[1][1])
            if background_object[0] == 0.5:
                self.display.blit(back1, self.objects)
            if background_object[0] == 0.25:
                self.display.blit(super_back1, self.objects)



