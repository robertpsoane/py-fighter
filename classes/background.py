''' Background Class

The Class creates and blits a background which is then capable of parallax scrolling once
camera Class starts updating the x values of each background object. The idea for the parallax
background was take from here: https://www.youtube.com/watch?v=5q7tmIlXROg
The class also randomises the images of the background.

@author: Rokas Danevicius (unless stated otherwise)
'''


import pygame
import random

# Creating information for each object which will be displayed on the background.

# The information is stored in a list of lists.
# as an example [increment, [x_position, y_position]].
# First parameter stores the increment of the scroll.
# The increment will be used to control the speed of the scroll for that particular object.
# x_position is where the object will be blited on x axes.
# y_position is where the object will be blited on y axes.



# Load the images used by the objects also scale the images to fit the size of the map.
back1 = pygame.image.load('graphics/background_sprite/back_1.png')
back1 = pygame.transform.scale(back1, (192, 192))

back2 = pygame.image.load('graphics/background_sprite/back_2.png')
back2 = pygame.transform.scale(back2, (192, 192))

back3 = pygame.image.load('graphics/background_sprite/back_3.png')
back3 = pygame.transform.scale(back3, (192, 192))

back4 = pygame.image.load('graphics/background_sprite/back_4.png')
back4 = pygame.transform.scale(back4, (192, 192))

super_back1 = pygame.image.load('graphics/background_sprite/back_super_1.png')
super_back1 = pygame.transform.scale(super_back1, (128 * 2, 128 * 2))

super_back2 = pygame.image.load('graphics/background_sprite/back_super_2.png')
super_back2 = pygame.transform.scale(super_back2, (128 * 2, 128 * 2))


class Background:
    """ Class reiterates through a matrix containing the increment and x/y positions of each object
    and blits an image using those values. The idea for the parallax background was take
    from here: https://www.youtube.com/watch?v=5q7tmIlXROg"""


    def __init__(self, screen):
        # Variable which temporarily stores information about a single object
        # when iteration is happening.
        self.objects = []
        # Gets the surface to which the background will be displayed.
        self.display = screen
        # Variable which gets updated with x scroll value from the Camera class.
        self.move = 0
        self.convertRandom()

    def objectRandom(self):

        background_objects = [[0.25, [0, 0], random.randint(0, 1)],
                              [0.25, [256, 0], random.randint(0, 1)],
                              [0.5, [0, 64], random.randint(0, 3)],
                              [0.5, [192, 64], random.randint(0, 3)],
                              [0.5, [384, 64], random.randint(0, 3)],
                              [0.5, [576, 64], random.randint(0, 3)]]
        return background_objects

    def convertRandom(self):
        '''
        Converting the randomly generated int values in the list of lists
        to loaded images which will be blited.
        '''

        # Create the list of lists with sublists containing a random int value.
        self.background_objects = self.objectRandom()

        # Checking the random values and assigning an image variable instead of it.
        for image in self.background_objects:
            if image[0] == 0.5 and image[2] == 0:
                image[2] = back1
            if image[0] == 0.5 and image[2] == 1:
                image[2] = back2
            if image[0] == 0.5 and image[2] == 2:
                image[2] = back3
            if image[0] == 0.5 and image[2] == 3:
                image[2] = back4
            if image[0] == 0.25 and image[2] == 0:
                image[2] = super_back1
            if image[0] == 0.25 and image[2] == 1:
                image[2] = super_back2


    def displayQ(self):
        ''' Method which blits the background to the display'''

        # Reiterating through "background_objects" matrix to get all of the values for
        # each individual background object.

        for background_object in self.background_objects:

            # x value of each object gets updated by the camera scroll stored in self.move
            # value when the camera scroll() method is active.
            # The speed of the scrolling gets determined by the increment which is
            # stored in background_object[0]
            self.objects = (background_object[1][0] - self.move * background_object[0],
                            background_object[1][1])

            # Blit the background images to the screen.
            self.display.blit(background_object[2], self.objects)



